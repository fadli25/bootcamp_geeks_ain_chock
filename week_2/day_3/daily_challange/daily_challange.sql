-- ========== Part I ==========

-- 1. Create Customer table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- 2. Create CustomerProfile table (One-to-One relationship)
CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

-- 3. Insert customers
INSERT INTO Customer (first_name, last_name)
VALUES ('John', 'Doe'),
       ('Jerome', 'Lalu'),
       ('Lea', 'Rive');

-- 4. Insert customer profiles using subqueries
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (TRUE, (SELECT id FROM Customer WHERE first_name = 'John')),
       (FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome'));

-- 5. Queries

-- a) The first_name of the LoggedIn customers
SELECT c.first_name
FROM Customer c
JOIN CustomerProfile p ON c.id = p.customer_id
WHERE p.isLoggedIn = TRUE;

-- b) All customers first_name and isLoggedIn (even without profile)
SELECT c.first_name, p.isLoggedIn
FROM Customer c
LEFT JOIN CustomerProfile p ON c.id = p.customer_id;

-- c) The number of customers that are not LoggedIn
SELECT COUNT(*) AS not_logged_in_count
FROM Customer c
LEFT JOIN CustomerProfile p ON c.id = p.customer_id
WHERE p.isLoggedIn = FALSE OR p.isLoggedIn IS NULL;


-- ========== Part II ==========

-- 1. Create Book table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- 2. Insert books
INSERT INTO Book (title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
       ('Harry Potter', 'J.K Rowling'),
       ('To kill a mockingbird', 'Harper Lee');

-- 3. Create Student table with constraint (age <= 15)
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

-- 4. Insert students
INSERT INTO Student (name, age)
VALUES ('John', 12),
       ('Lera', 11),
       ('Patrick', 10),
       ('Bob', 14);

-- 5. Create Library (junction table Many-to-Many)
CREATE TABLE Library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date),
    FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Insert records using subqueries
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
),
(
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
),
(
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
),
(
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

-- 7. Queries

-- a) Select all columns from junction table
SELECT * FROM Library;

-- b) Select the name of the student and the title of the borrowed books
SELECT s.name, b.title, l.borrowed_date
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

-- c) Select the average age of children that borrowed 'Alice in Wonderland'
SELECT AVG(s.age) AS avg_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- d) Delete a student and check what happens in junction table
DELETE FROM Student WHERE name = 'Patrick';
-- Because of ON DELETE CASCADE, any borrow records for Patrick are also deleted.