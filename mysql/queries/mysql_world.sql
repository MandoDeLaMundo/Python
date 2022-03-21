SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY percentage DESC;

SELECT countries.name, COUNT(*) AS cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY cities DESC;

SELECT cities.name AS city, cities.population AS population, country_id
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
GROUP BY cities.population
ORDER BY cities.population DESC; 

SELECT countries.name AS name, languages.language AS language, languages.percentage AS percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
GROUP BY languages.percentage
ORDER BY languages.percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75;

SELECT countries.name AS country_name, cities.name AS city_name, cities.district AS district, cities.population AS population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

SELECT countries.region, COUNT(*) AS countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;
