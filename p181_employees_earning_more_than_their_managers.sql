select a.Name Employee
  from Employee a, Employee b
 where a.ManagerId = b.Id
   and a.Salary > b.Salary
