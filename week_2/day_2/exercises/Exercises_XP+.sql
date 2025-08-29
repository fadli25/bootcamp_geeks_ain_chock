select title, rating from film
GROUP by rating, title
order by rating;


select title, rating,length,rental_rate from film
where rating in ('G','PG-13') and length > 2 and rental_rate < 3
GROUP by rating, title,length,rental_rate
order by title;


UPDATE customer
set first_name = 'Zakaria',
	last_name = 'Fadli',
	email = 'zakaria.fadli@gmail.com'
where customer.customer_id = 524

UPDATE address
set address.address = '23 Ain chock'
where (select * from customer where customer_id = 549)

