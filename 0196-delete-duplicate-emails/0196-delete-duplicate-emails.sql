# Write your MySQL query statement below
DELETE
FROM Person
WHERE id NOT IN (
    SELECT sub.min_id
    FROM (
        SELECT email, MIN(Id) AS min_id
        FROM Person
        GROUP BY email
    ) sub
);