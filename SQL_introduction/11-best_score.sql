-- Lists all records with a score >= 10 in table "second_table"
-- Ordered in DESC

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;