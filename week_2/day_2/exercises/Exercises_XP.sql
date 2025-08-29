-- Exercises 1:

-- 1
select * from items order by price;

-- 2
select * from items where price >= 80 order by price DESC;

-- 3
select first_name, last_name from customers order by first_name limit 3

-- 4
select last_name from customers order by last_name DESC;


-- Exercises 2:

select * from customer;

select (first_name || ' ' || last_name) AS full_name from customer;

SELECT DISTINCT create_date from customer;

select * from customer order by first_name DESC;

SELECT film_id, title, description, release_year, rental_rate from film order by rental_rate;

select address, phone from address where district = 'Texas';

select * from film where film.film_id between 15 and 150

SELECT film_id, title, description, release_year, length, rental_rate from film WHERE title = 'Baby Driver';

select film.title,payment.amount from film
inner join inventory
on inventory.film_id = film.film_id
INNER join rental
on rental.inventory_id = inventory.inventory_id
INNER join payment on payment.rental_id = rental.rental_id
ORDER by payment.amount
limit 10;

select film.title,payment.amount,ren from film
inner join inventory
on inventory.film_id = film.film_id
INNER join rental
on rental.inventory_id = inventory.inventory_id
INNER join payment on payment.rental_id = rental.rental_id
ORDER by payment.amount
OFFSET 10 rows
fetch next 10 rows only;


select (customer.first_name || ' ' || customer.last_name) as full_name, payment.amount, payment.payment_date from customer
INNER join payment
on payment.customer_id = customer.customer_id


select  country.country, city.city from country
join city
on city.country_id = country.country_id
group by  city.city ,country.country
order by country.country

-- by othman

SELECT country.country, STRING_AGG(city.city, ', ' ORDER BY city.city) AS cities
FROM country
JOIN city ON city.country_id = country.country_id
GROUP BY country.country
ORDER BY country.country;

select customer.customer_id, customer.first_name, customer.last_name, payment.amount,payment.payment_date from customer
join payment
on payment.customer_id = customer.customer_id
join staff
on staff.staff_id = payment.staff_id
ORDER by staff.staff_id
