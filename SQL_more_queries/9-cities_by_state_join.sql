-- Lists all cities contained in database

SELECT id, name, (
	SELECT name FROM states WHERE id = cities.state_id
)
FROM cities
ORDER BY cities.id ASC;