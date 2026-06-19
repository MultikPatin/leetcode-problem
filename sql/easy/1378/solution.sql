select unique_id, u.name
from EmployeeUNI as eu
         right join Employees as u on u.id = eu.id