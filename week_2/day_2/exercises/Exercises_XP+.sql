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

-- Exercise 2
-- 1
update students
set brith_dates = '02/11/1998'
where last_name = 'Benichou'and first_name in ('Marc','Lea')


-- 2

update students
set last_name = 'Guez'
where last_name = 'Grez'

-- Delete

delete from students
where first_name = 'Lea' and last_name = 'Benichou'

-- count

-- 1

select count (*) from students
-- 2
select count (*) from students where birth_dates > '1/01/2000'

-- insert / alter

-- 1

alter table students
add column math_grade integer;

-- 2

update students
set math_grade = 80
where student_id = 1

-- 3

update students
set math_grade = 90
where student_id = 2;

-- 4

update students
set math_grade = 90
where student_id in (2,4);

-- 5

update students
set math_grade = 40
where student_id = 6;
select count(*) from students where math_grade > 83

-- 6

insert into students
values
('Omer','Simpson','02/11/1998',70)

-- 7
select first_name, last_name, count(math_grade) as total_grade
from students
group by first_name, last_name;

-- sum
-- 1

select sum(math_grade) from students;

-- Exercise 3

-- Part 1

-- 1

create table purchases (
    id serial primary key,
    customer_id integer references students(student_id),
    item_id integer references items(item_id),
    quantity_purchased numeric
);

-- 2

insert into purchases (customer_id, item_id, quantity_purchased)
values
(3, 3, 1),
(5, 2, 10),
(1, 1, 2);


-- Part 2

-- 1

-- 1.1

select * from purchases;

-- 1.2

select * from from purchases
inner join customers on purchases.customer_id = customers.student_id;

-- 1.3

select * from purchases
inner join customers on purchases.customer_id = customers.student_id
where customers.customer_id = 5;

-- 1.4

select * from purchases
inner join customers on purchases.customer_id = customers.student_id
inner join items on purchases.item_id = items.item_id
where items.desk in ('large','small')

-- 2

select customers.first_name, customers.last_name, purchases.item_id, purchases.quantity_purchased
from purchases
inner join items on purchases.item_id = items.item_id

-- 3
insert into purchases (customer_id, item_id, quantity_purchased)
values (2, NULL, 5);

-- This will work only if the item_id column in purchases allows NULL values.
-- If item_id is defined as NOT NULL or the referenced items table does not have a row with NULL as item_id, 
-- the insert will fail due to the foreign key constraint or NOT NULL constraint.