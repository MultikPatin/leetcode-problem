select e.name as Employee
from Employee as e
         join Employee as m on m.id = e.managerId and e.salary > m.salary