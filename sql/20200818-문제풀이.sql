-- emp 테이블에서 커미션이 있는 사원의 이름과 커미션을 출력하는 명령을 작성하시오
select first_name, last_name, commission_pct
from employees
where commission_pct is not null;

-- 최고참 사원의 이름과 입사날짜를 출력하는 명령문을 작성하시오
select first_name, last_name, hire_date 
from employees
where hire_date = (select min(hire_date) from employees);

-- 가장 최근 입사한 사원의 first이름과 입사 날짜를 출력하는 명령문을 작성하시오.
select first_name, last_name, hire_date
from employees
where hire_date = (select max(hire_date) from employees);

-- 최대 급여를 받는 사원의 first 이름과 급여를 출력하는 명령문을 작성하시오.
select first_name, salary
from employees
where salary=(select max(salary) from employees);

-- 부서별 사원수와 평균 급여를 구하는 명령문을 작성하시오.
select count(*), round(avg(salary)), department_id
from employees
group by department_id;

-- 사원수가 10명 이하인 부서_ID와 사원수를 출력하는 명령을 작성하시오.(단, null값은 제외)
select count(*), department_id
from employees e1
where department_id is not null 
    and (select count(*) from employees e2 
            where e2.department_id = e1.department_id) <=10
group by department_id;

-- 위의 세 테이블을 조인하여 사원이 속한 부서명과 직책명을 출력하는 명령을 작성하시오
select e.first_name, e.last_name, d.department_name, j.job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id;

-- 평균 급여보다 적게받는 사원들의 명단과 직책을 출력하는 명령을 작성하시오.
select e.first_name, e.last_name, j.job_title
from employees e, jobs j
where e.salary < (select avg(salary) from employees);

-- 아이디가 100번인 부서보다 월급을 많이 받는 사원의 아이디와 부서아이디, 월급을 출력하는 명령을
-- 작성하시오
-- 100의 모든 사원보다?

-- max
select employee_id, department_id, salary
from employees
where salary > (select max(salary) from employees where department_id = 100)
order by employee_id;

-- all
select employee_id, department_id, salary
from employees
where salary > all(select salary from employees where department_id = 100)
order by employee_id;

-- emp 테이블과 같은 emp2 테이블을 생성하는 명령문을 작성하시오.
create table employees2
as select * from employees;

alter table employees2 drop column manager_id;

create table emp(
    job varchar(20) not null,
    constraint chk_job check(job in('사원','대리','과장','차장','부장'))
);

insert into emp
values('대리');

drop table emp;

select department_id, count(*) from employees
where department_id is not null
group by department_id
having count(*) <= 10;

