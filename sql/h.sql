select
    count(first_name),
    count(DISTINCT first_name)
from
    employees;


select
    avg(salary)
from employees;

select
    avg(salary)
from 
    employees
where
    department_id = 80;

-- max()
select
    e.first_name,
    e.last_name,
    e.salary
from
    employees e
where
    e.salary = (select max(salary) from employees);
    
update employees
set
    salary = 8300
where
    employee_id = 206;

-- 8300

-- �����Լ��� where������ ��� �Ұ�

select * from employees;
