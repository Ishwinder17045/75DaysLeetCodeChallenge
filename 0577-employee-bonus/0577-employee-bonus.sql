# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
left join Bonus b 
on e.empid = b.empid
where bonus < 1000 OR bonus is null;