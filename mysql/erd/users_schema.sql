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

SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%M/%e/%Y"), DATE_FORMAT(updated_at, "%M/%e/%Y"), TIME_FORMAT(updated_at, "%h:%i %p")
FROM users
WHERE id = 4;

UPDATE users SET first_name = "Sam", last_name = "Nulland", email = "SN8987@gmail.com", updated_at = NOW() WHERE id = 4;