-- selects the number of records with same score in table
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
GROUP BY as number DESC;
