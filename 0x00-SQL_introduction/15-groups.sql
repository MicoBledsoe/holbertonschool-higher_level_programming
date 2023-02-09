-- selects the number of records with same score in table

SELECT score, COUNT(score) as count
FROM second_table
GROUP BY score;
