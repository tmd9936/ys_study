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

select min(salary) from employees;

select 
    e1.first_name, 
    e1.last_name,
    e1.salary
from 
    employees e1
where
    e1.hire_date = (select min(hire_date) from employees);
    

-- abs()�� ���밪
select abs(-23) from dual; -- dual�� ����Ŭ���� �����ϴ� dummy ���̺�

-- �ݿø�
select round(0.123), round(0.542) from dual;

-- �Ҽ��� �� 6��° �ڸ� ���� �ݿø�
select round(0.12345678, 6) from dual;

-- trunc(n1, n2) truncate �߶󳻴�, �Ҽ��� �ڸ��� ����
select trunc(1234.121212) from dual;
-- �Ҽ��� 2��° �ڸ����� �߶�
select trunc(1234.121212, 2) from dual;

-- ceil() : �ø�, floor() : ����
select ceil(32.8) from dual;
select ceil(32.3) from dual;

select floor(32.9) from dual;
select floor(32.1) from dual;

-- power() ��

select power(4, 5) power1 from dual;

-- mod() ������ ������
select mod(7, 4) mod1 from dual;

-- sqrt() ������
select sqrt(2) sqrt1, sqrt(3) sqrt2 from dual;