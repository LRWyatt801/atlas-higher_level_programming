-- lists all records in "second_table" only when name has a value

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;