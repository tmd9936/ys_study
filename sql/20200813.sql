-- * 모든 열 보기
desc employees;

select * from employees;

select * from employees where last_name = 'Smith';

select *
from employees e
right join jobs j on e.job_id = j.job_id;

select 
    employee_id,
    salary
from employees
where
    last_name = 'Ernst';
    
select 
    job_id,
    sum(salary) sum_s
from
    employees
group by 
    job_id
having sum(salary) > 9000
order by sum_s;

select 
    e.employee_id as "사원 id",
    e.salary as "월급"
from
    employees e;

-- distinct 중복 제거
select 
    DISTINCT job_id
from
    employees;

-- 연산자 (산술, 비교, 논리 

select 
    e.first_name,
    e.last_name,
    e.salary
from
    employees e
where
    e.salary >= 5000;

select
    e.last_name,
    e.salary,
    e.hire_date
from
    employees e
where
    e.hire_date > '2003/12/31'
order by 
    e.hire_date;

-- 논리 연산자(and, or, not)

-- 부서번호가 50이면서 job_id가 sh_clerk인 직원의 이름과 job_id

select
    first_name,
    last_name,
    job_id,
    department_id
from
    employees
where
    job_id = 'SH_CLERK' and department_id = 50;


select
    last_name,
    department_id,
    manager_id
from  
    employees
where
    department_id = 50 or manager_id = 100;
    

select
    first_name,
    last_name,
    department_id
from
    employees
where
    department_id <> 50;
    
-- 급여가 4000 ~ 8000 사이의 직워느이 이름과 급여를 출력

select
    first_name,
    last_name,
    salary
from 
    employees
where
    salary >= 4000 and salary <= 8000
order by salary;


select 
    e.last_name || ' ' || e.first_name ,
    e.email,
    j.job_title,
    e2.last_name || ' ' || e2.first_name as "manager"
from
    employees e
join jobs j
    on e.job_id = j.job_id
join employees e2
    on e2.manager_id = e.manager_id;
    
-- first name이 D로 시작하는 사원
select 
    first_name,
    last_name 
from 
    employees
where 
    first_name like 'D%';

select 
    first_name,
    last_name 
from 
    employees
where 
    first_name like '%d';

-- firsh_name 앞에서 세번째 글자가 a로 시작하는 사원 조회
select
    first_name,
    last_name
from 
    employees
where
    first_name like '__a%';

select
    first_name,
    last_name,
    commission_pct
from 
    employees
where
    commission_pct is not null;

/*
    오름차순 정렬(ascending sort)
*/
select 
    employee_id,
    first_name
from
    employees
order by employee_id asc;

select 
    employee_id,
    first_name
from
    employees
order by employee_id desc;

