-- selects the number of records with same score in table

<<<<<<< HEAD
SELECT score, COUNT(*) as number
=======
SELECT score, COUNT(score) as count
>>>>>>> 3aa248e06c1f8b675087484ceae26883b2891f06
FROM second_table
GROUP BY score
GROUP BY number DESC;
