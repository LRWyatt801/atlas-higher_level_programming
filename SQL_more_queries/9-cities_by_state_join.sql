-- Lists all cities contained in database

SELECT cities.id, cities.name, states.name WHERE states.id = cities.state_id
FROM cities, states
ORDER BY cities.id ASC;