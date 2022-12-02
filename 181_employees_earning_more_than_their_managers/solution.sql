SELECT A.name as Employee FROM Employee as A
LEFT JOIN Employee as B
ON A.managerId = B.id
WHERE A.salary > B.salary
