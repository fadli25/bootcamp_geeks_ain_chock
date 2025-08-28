-- 1

select * from students
order by last_name
limit 4;

-- 2

select * from students
order by birth_date desc
limit 1;

-- 3

select * from students
offset 2
limit 3

