-- Create users table (Bonus)
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

-- Create product_orders table
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create items table
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE,
    product_name VARCHAR(150) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

-- Function: total price for a given order
CREATE OR REPLACE FUNCTION get_order_total(orderId INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT COALESCE(SUM(price),0) INTO total
    FROM items
    WHERE order_id = orderId;

    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- Bonus: total price for a given order of a given user
CREATE OR REPLACE FUNCTION get_user_order_total(userId INT, orderId INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT COALESCE(SUM(i.price),0) INTO total
    FROM items i
    INNER JOIN product_orders po ON po.order_id = i.order_id
    WHERE po.order_id = orderId
      AND po.user_id = userId;

    RETURN total;
END;
$$ LANGUAGE plpgsql;
