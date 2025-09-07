select * from film;

-- 1

SELECT 
    r.rental_id,
    f.title,
	f.rental_duration,
    (r.return_date - r.rental_date) AS rental_out
FROM rental r
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN film f ON f.film_id = i.film_id;



-- 2

SELECT 
    c.first_name,
	c.last_name,
    (r.return_date - r.rental_date) AS rental_out
from customer c
inner join rental r on c.customer_id = c.customer_id
INNER JOIN inventory i ON i.inventory_id = r.inventory_id
INNER JOIN film f ON f.film_id = i.film_id;

select film.title,film.description, a.first_name || ' ' || a.last_name as name from film
inner join film_actor
on film.film_id = film_actor.film_id
inner join actor a 
on a.actor_id = film_actor.actor_id
where a.first_name = 'Joe' and a.last_name = 'Swank' and film.description ilike '%action%'


-- Exercise 2:

-- 1

select count (s.store_id),city.city,country.country from store s
inner join address a
on a.address_id = s.address_id
inner join city
on city.city_id = a.city_id
inner join country
on country.country_id = city.country_id
group by country.country,city.city
