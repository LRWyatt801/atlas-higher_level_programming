-- Lists all cities contained in database

SELECT cities.id, cities.name, states.name
FROM cities
ORDER BY cities.id ASC;