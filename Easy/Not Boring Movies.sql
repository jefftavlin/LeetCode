# Write your MySQL query statement below
SELECT *
from cinema
WHERE MOD(id, 2) > 0 AND description NOT LIKE 'boring'
ORDER BY rating DESC
