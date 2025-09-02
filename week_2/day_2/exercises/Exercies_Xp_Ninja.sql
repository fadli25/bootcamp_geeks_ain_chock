-- 1.
SELECT first_name, last_name, email
FROM customers
ORDER BY last_name ASC, first_name ASC
LIMIT 2 OFFSET (
    SELECT COUNT(*) FROM customers
) - 2;

-- 2.
DELETE FROM purchases
WHERE customer_id = (
    SELECT id FROM customers WHERE first_name = 'Scott'
);

-- 3.
SELECT * FROM customers WHERE first_name = 'Scott';

-- 4.
SELECT 
    purchases.id AS purchase_id,
    COALESCE(customers.first_name, '') AS first_name,
    COALESCE(customers.last_name, '') AS last_name,
    purchases.product,
    purchases.amount
FROM purchases
LEFT JOIN customers ON purchases.customer_id = customers.id;

-- 5.
SELECT 
    purchases.id AS purchase_id,
    customers.first_name,
    customers.last_name,
    purchases.product,
    purchases.amount
FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.id;