-- 1. Retrieve all films with a rating of G or PG, which are not currently rented
--    (they have been returned or never borrowed).
SELECT DISTINCT f.film_id, f.title, f.rating
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
WHERE f.rating IN ('G', 'PG')
  AND r.rental_id IS NULL;


-- 2. Create a new table for waiting list for children's movies.
--    Assumption: Python program will handle add/remove of rows.
CREATE TABLE kids_waiting_list (
    wait_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    child_name VARCHAR(100) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);

-- 3. Retrieve the number of people waiting for each children’s DVD.
SELECT f.film_id, f.title, COUNT(w.wait_id) AS waiting_count
FROM film f
JOIN kids_waiting_list w ON f.film_id = w.film_id
GROUP BY f.film_id, f.title
ORDER BY waiting_count DESC;

-- Example test inserts (simulate children waiting).
INSERT INTO kids_waiting_list (film_id, child_name)
VALUES (1, 'Alice'), (1, 'Bob'), (2, 'Charlie');