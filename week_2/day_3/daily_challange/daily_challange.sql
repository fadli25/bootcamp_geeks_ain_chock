-- Product Orders & Items
-- =========================

-- 1. Create tables product_orders and items
CREATE TABLE product_orders (
  order_id SERIAL PRIMARY KEY,
  order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE items (
  item_id SERIAL PRIMARY KEY,
  item_name VARCHAR(100) NOT NULL,
  price NUMERIC(10,2) NOT NULL,
  order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE
);

-- 2. One-to-many relationship:
--    One order can have many items, but each item belongs to one order (already done via FK).

-- 3. Function to return total price for a given order
CREATE OR REPLACE FUNCTION get_order_total(orderId INT)
RETURNS NUMERIC AS $$
  SELECT COALESCE(SUM(price),0)
  FROM items
  WHERE order_id = orderId;
$$ LANGUAGE SQL;


-- =========================
-- BONUS : Add Users
-- =========================

-- 1. Create users table
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL
);

-- 2. One-to-many relationship between users and product_orders
ALTER TABLE product_orders
ADD COLUMN user_id INT REFERENCES users(user_id) ON DELETE CASCADE;

-- 3. Function to return total price for a given order of a given user
CREATE OR REPLACE FUNCTION get_user_order_total(userId INT, orderId INT)
RETURNS NUMERIC AS $$
  SELECT COALESCE(SUM(i.price),0)
  FROM items i
  JOIN product_orders po ON i.order_id = po.order_id
  WHERE po.user_id = userId
    AND po.order_id = orderId;
