/* 서브 쿼리 - 실무에서 많이 사용하는 쿼리 방법 */
 -- 평균 급여보다 적은 급여를 받는 사원을 조회하시오
select first_name, last_name,salary
from employees
where salary < 6462;

select first_name, last_name,salary
from employees
where salary < round(avg(salary)); -- where절에서 집계함수 사용불가

-- 서브쿼리를 적용해서 조회하기
select first_name, last_name,salary
from employees
where salary < (select round(avg(salary)) from employees);

select * from locations; 

select location_id
from locations
where state_province is null;

select * from departments;

select * from departments
where location_id in(
select location_id
from locations
where state_province is null
);

-- 결과값이 여러 개로 나오는 경우
select location_id
from locations
where country_id ='US';

-- in 연산자를 사용하는 예
select * from departments
where location_id in(
select location_id
from locations
where country_id ='US'
);

-- 위의 코드를 다음과 같이 바꿔서 표현
select * from departments
where location_id in(1400, 1500, 1600, 1700);

-- [문제 1] 월급이 가장 적은 사원의 이름과 직책명을 조회
select emp.first_name, job.job_title
from employees emp, jobs job
where emp.salary = (select min(salary) from employees)
and emp.job_id = job.job_id;

-- [문제 2] 평균 급여보다 많이 받는 사원들의 명단과 직책을 조회
select avg(salary) from employees;
select emp.first_name, job.job_title
from employees emp, jobs job
where (select round(avg(salary)) from employees) < emp.salary
and emp.job_id = job.job_id;
