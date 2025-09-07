-- 1

select * from language

-- 2

select f.title, f.description, l.name from film f
inner join language l
on l.language_id = f.language_id

-- 3

select f.title, f.description, l.name from language l
right join film f
on l.language_id = f.language_id

-- 4

create table new_film(
id serial primary key,
name text
)

insert into new_film(name)
values
('Chamber Italian'),
('Grosse Wonderful'),
('Airport Pollock'),
('Bright Encounters')

create table customer_review(
review_id serial primary key,
film_id integer references film(film_id) on delete cascade,
language_id integer references language(language_id),
title varchar(100),
score int check (score >= 1 and score <= 10),
review_text text,
last_update date
)

INSERT INTO customer_review (
    film_id, language_id, title, score, review_text, last_update
) VALUES
(1, 1, 'Amazing Movie', 9, 'Great story and acting.', CURRENT_DATE),
(2, 2, 'Not bad', 7, 'It was okay, but could be better.', CURRENT_DATE),
(3, 1, 'Loved it', 10, 'One of my favorites!', CURRENT_DATE);

drop table customer_review

-- 7

delete from film
where film_id =1

-- Exercise 2:

select name from language
group by name

-- 1

update film
set language_id = 5
where film_id = 1

drop table customer_review


