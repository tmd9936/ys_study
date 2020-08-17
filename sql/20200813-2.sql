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

-- 집계함수는 where절에서 사용 불가

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
    

-- abs()는 절대값
select abs(-23) from dual; -- dual은 오라클에서 제공하는 dummy 테이블

-- 반올림
select round(0.123), round(0.542) from dual;

-- 소수점 뒤 6번째 자리 수가 반올림
select round(0.12345678, 6) from dual;

-- trunc(n1, n2) truncate 잘라내다, 소수점 자리를 제거
select trunc(1234.121212) from dual;
-- 소수점 2번째 자리부터 잘라냄
select trunc(1234.121212, 2) from dual;

-- ceil() : 올림, floor() : 내림
select ceil(32.8) from dual;
select ceil(32.3) from dual;

select floor(32.9) from dual;
select floor(32.1) from dual;

-- power() 승

select power(4, 5) power1 from dual;

-- mod() 나머지 연산자
select mod(7, 4) mod1 from dual;

-- sqrt() 제곱근
select sqrt(2) sqrt1, sqrt(3) sqrt2 from dual;