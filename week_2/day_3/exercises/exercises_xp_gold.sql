-- ========== Exercise 1 : DVD Rentals ==========

-- 1. Get a list of all rentals which are out (have not been returned).
SELECT r.rental_id, r.rental_date, f.title, c.first_name, c.last_name
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL;

-- 2. Get a list of all customers who have not returned their rentals (grouped).
SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS unreturned_count
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(r.rental_id) > 0;

-- 3. Get a list of all the Action films with Joe Swank.
SELECT f.film_id, f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE cat.name = 'Action'
  AND a.first_name = 'Joe'
  AND a.last_name = 'Swank';

-- 4. Shortcut: creating a VIEW for frequently used rentals out.
CREATE VIEW rentals_out AS
SELECT r.rental_id, r.rental_date, f.title, c.first_name, c.last_name
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL;


-- ========== Exercise 2 – Happy Halloween ==========

-- 1. How many stores there are, and in which city and country they are located.
SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- 2. How many hours of viewing time there are in total in each store –
--    sum of length of every inventory item in each store,
--    excluding not yet returned.
SELECT s.store_id, SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 1440.0, 2) AS total_days
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN film f ON i.film_id = f.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
WHERE r.rental_id IS NULL
GROUP BY s.store_id;

-- 3. A list of all customers in the cities where the stores are located.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT ci.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
);

-- 4. A list of all customers in the countries where the stores are located.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT co.country_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
);

-- 5. Safe list: movies NOT Horror and NOT containing scary words.
SELECT SUM(f.length) AS safe_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS safe_hours,
       ROUND(SUM(f.length) / 1440.0, 2) AS safe_days
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
WHERE cat.name <> 'Horror'
  AND LOWER(f.title) NOT LIKE '%beast%'
  AND LOWER(f.title) NOT LIKE '%monster%'
  AND LOWER(f.title) NOT LIKE '%ghost%'
  AND LOWER(f.title) NOT LIKE '%dead%'
  AND LOWER(f.title) NOT LIKE '%zombie%'
  AND LOWER(f.title) NOT LIKE '%undead%';

-- 6. General list: all movies with total time in hours and days.
SELECT SUM(f.length) AS general_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS general_hours,
       ROUND(SUM(f.length) / 1440.0, 2) AS general_days
FROM film f;