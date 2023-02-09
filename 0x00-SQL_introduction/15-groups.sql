-- selects the number of records with same score in table

SELECT score, COUNT(*) as COUNT
FROM second_table
GROUP BY score;
