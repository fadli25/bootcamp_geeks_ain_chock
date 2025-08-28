select * from students;

select first_name, last_name from students;

select first_name , last_name from students where id = 2;

select first_name , last_name from students where last_name = 'Benichou' and first_name = 'Marc';

select first_name , last_name from students where last_name = 'Benichou' or first_name = 'Marc';

select first_name , last_name from students where first_name like '%a%';

select first_name , last_name from students where first_name like 'a%';

select first_name , last_name from students where first_name like '%a';

select first_name , last_name from students where last_name like '%a_';

select first_name , last_name from students where id in (1,3);

select first_name , last_name from students where birth_date >= '1/01/2000'