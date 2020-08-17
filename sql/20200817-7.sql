/* join 일반적으로 '내부join' 방식을 의미한다. */
select * from employees;
select * from locations;
desc department;

-- 두개의 테이블 조인
select emp.department_id, emp.first_name, emp.last_name, dep.department_name
from employees emp, departments dep
where emp.department_id = dep.department_id;

-- 세개의 테이블 조인
-- 직원의 이름, 이메일, 부서아이디, 부서명, 직급명을 조회
select emp.first_name, emp.last_name, emp.email, emp.department_id, dep.department_name, job.job_title
from employees emp, departments dep, jobs job
where emp.department_id = dep.department_id
and emp.job_id = job.job_id;

-- 네개의 테이블 조인
-- 직원의 이름, 이메일, 부서아이디, 부서명, 직급아이디, 직급명, 근무위치를 조회
select emp.last_name, emp.email, emp.department_id, dep.department_name,
job.job_id, job.job_title, loc.city
from employees emp, departments dep, jobs job, locations loc
where emp.department_id = dep.department_id
and emp.job_id = job.job_id
and dep.location_id = loc.location_id;

-- 일반 조건과 결합 : Seattle에서 근무하는 직원들의 이름, 이메일, 부서명, 직책명, Seattle을 조회
select emp.last_name, emp.email, dep.department_name, job.job_title, loc.city
from employees emp, locations loc, jobs job, departments dep
where dep.location_id = loc.location_id
and emp.department_id = dep.department_id
and emp.job_id = job.job_id
and city = 'Seattle'; -- 일반 조건 포함

/* 셀프 조인 자신의 테이블을 두개의 테이블 처럼 사용하는 것 */
select * from employees;

select emp1.employee_id, emp1.first_name, emp2.employee_id 상사id, emp2.first_name 상사이름
from employees emp1, employees emp2
where emp1.manager_id = emp2.employee_id;


/* 외부 조인 */
-- 내부 조인으로 했을 때
select emp.employee_id, emp.first_name, dep.department_name
from employees emp, departments dep
where emp.department_id = dep.department_id;

-- 외부 조인으로 했을 때
select emp.employee_id, emp.first_name, dep.department_name
from employees emp, departments dep
-- 왼쪽을 기준으로 오른쪽이 늘어남 Left Outer join
--where emp.department_id = dep.department_id(+);
-- 오른쪽을 기준으로 왼쪽이 늘어남 Left Outer join
where emp.department_id(+) = dep.department_id;


-- [문제] 모든 사원의 사원ID와 first_name, 부서명, 근무 도시를 출력
select emp.employee_id, emp.first_name, dep.department_name, loc.city
from employees emp, departments dep, locations loc
where emp.department_id = dep.department_id (+)
and dep.location_id = loc.location_id (+);

-- [문제] 모든 사원의 사원ID와 first_name 그리고 상사ID와 상사이름을 출력
select emp1.employee_id 사원id, emp1.first_name 사원이름, emp2.employee_id 상사id, emp2.first_name 상사이름
from employees emp1, employees emp2
where emp1.manager_id = emp2.employee_id(+);

select * from employees;