/* group by 절 */

select 
    DISTINCT department_id 
from 
    employees;

select department_id from employees
group by department_id;

-- 부서별 급여의 합계

select department_id, sum(salary) from employees
group by department_id
order by department_id;

-- 부서별 사원수와 부서별 총 급여, 부서별 평균 급여

select
    e.department_id,
    d.department_name,
    count(*), 
    sum(e.salary), 
    ceil(avg(e.salary))
from
    employees e
left join departments d
    on e.department_id = d.department_id
group by
    e.department_id, d.department_name
order by
    e.department_id;

-- 부서별 직급별 사원수와 평균 급여를 조회하시오.

select
    department_id,
    job_id,
    count(salary),
    ceil(avg(salary)),
    sum(salary)
from
    employees
group by
    department_id, job_id
order by
    department_id, job_id;

select 
    department_id, 
    job_id, 
    to_char(sum(salary), '999,999') "총급여",
    to_char(avg(salary), '999,999') "평균급여"
from 
    employees
where
    department_id = 80
group by 
    department_id, job_id
order by 
    department_id, job_id;


