INSERT INTO users(first_name, last_name, email)
VALUES ('Jonathan', 'Nichols', 'jnichols@gmail.com'),
('Nicholas', 'Johnson', 'njohnson@yahoo.com'),
('Eat', 'Yogurt', 'eyoguur@hotmail.com');


SELECT * FROM users;

SELECT *
FROM users
WHERE email = 'jnichols@gmail.com';

SELECT *
FROM users
WHERE id = 3;

UPDATE users
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE
FROM users
WHERE id = 2;

SELECT *
FROM users
ORDER BY first_name;

SELECT *
FROM users
ORDER BY first_name DESC;