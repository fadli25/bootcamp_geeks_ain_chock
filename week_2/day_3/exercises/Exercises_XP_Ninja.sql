
-- Films available (not rented now):
SELECT f.film_id, f.title, f.rating
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r 
       ON i.inventory_id = r.inventory_id 
       AND r.return_date IS NULL   -- means still rented
WHERE f.rating IN ('G', 'PG')
  AND r.rental_id IS NULL;        -- no active rental

-- ==========================================
-- 2. Create a waiting list table
-- ==========================================

DROP TABLE IF EXISTS waiting_list;

CREATE TABLE waiting_list (
    wait_id SERIAL PRIMARY KEY,
    child_name VARCHAR(100) NOT NULL,
    film_id INT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES film(film_id)
);

-- Example inserts (simulate kids waiting for movies):
INSERT INTO waiting_list (child_name, film_id) 
VALUES 
('Alice', 1),
('Bob', 1),
('Charlie', 2);

-- ==========================================
-- 3. Retrieve the number of people waiting 
--    for each children’s DVD
-- ==========================================

SELECT f.film_id, f.title, COUNT(w.wait_id) AS waiting_count
FROM film f
LEFT JOIN waiting_list w ON f.film_id = w.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.film_id, f.title
ORDER BY waiting_count DESC;

-- ==========================================
-- End of file
-- ==========================================
