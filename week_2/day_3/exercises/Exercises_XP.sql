

-- 1. Rentals that are still out (not returned)
SELECT rental_id, rental_date, inventory_id, customer_id
FROM rental
WHERE return_date IS NULL;

-- 2. Customers who have not returned rentals (grouped)
SELECT c.customer_id, c.first_name, c.last_name, COUNT(*) AS unreturned_rentals
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY unreturned_rentals DESC;

-- 3. Action films with Joe Swank
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE c.name = 'Action'
  AND a.first_name = 'JOE'
  AND a.last_name = 'SWANK';

-- (Optional) Shortcut: create a view for unreturned rentals
CREATE OR REPLACE VIEW unreturned_rentals AS
SELECT r.rental_id, r.customer_id, r.inventory_id, r.rental_date
FROM rental r
WHERE r.return_date IS NULL;


-- ===============================
-- Exercise 2 : Happy Halloween
-- ===============================

-- 1. Stores and their city/country
SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- 2. Total viewing time per store (only returned films)
SELECT i.store_id,
       SUM(f.length) AS total_minutes,
       SUM(f.length) / 60 AS total_hours
FROM inventory i
JOIN film f ON i.film_id = f.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY i.store_id;

-- 3. Customers in the same cities as the stores
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city IN (
  SELECT ci2.city
  FROM store s
  JOIN address a2 ON s.address_id = a2.address_id
  JOIN city ci2 ON a2.city_id = ci2.city_id
);

-- 4. Customers in the same countries as the stores
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country IN (
  SELECT co2.country
  FROM store s
  JOIN address a2 ON s.address_id = a2.address_id
  JOIN city ci2 ON a2.city_id = ci2.city_id
  JOIN country co2 ON ci2.country_id = co2.country_id
);

-- 5. Safe list (exclude Horror + scary words) and sum viewing time
SELECT SUM(f.length) AS total_minutes,
       SUM(f.length) / 60 AS total_hours,
       SUM(f.length) / 1440 AS total_days
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name <> 'Horror'
  AND f.title NOT ILIKE '%beast%'
  AND f.title NOT ILIKE '%monster%'
  AND f.title NOT ILIKE '%ghost%'
  AND f.title NOT ILIKE '%dead%'
  AND f.title NOT ILIKE '%zombie%'
  AND f.title NOT ILIKE '%undead%';
