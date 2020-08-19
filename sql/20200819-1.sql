/*
    뷰(view)
    : 물리적으로 존재하지 않는 가상의 테이블
    : 하나 이상의 테이블을 조회하는 SELECT문을 저장한 객체
    뷰의 용도
    :편리성(SELECT문의 복잡함을 해소하고자 할 때 사용
    :보안성(테이블의 특정 열을 노출하고 싶지 않을 떄 사용)
    뷰의 형식
    CREATE VIEW 뷰이름(컬럼1, 컬럼2, ...)
    AS SELECT문
*/
CREATE VIEW v_emp(emp_id, first_name, job_id, hire_date, dept_id)
AS
SELECT employee_id, first_name, job_id, hire_date, department_id
FROM employees
WHERE job_id = 'ST_CLERK';

select * from v_emp;

CREATE VIEW v_emp1(emp_id, first_name, job_id, hire_date, dept_id)
AS
SELECT employee_id, first_name, job_id, hire_date, department_id
FROM employees
WHERE job_id = 'SH_CLERK';


-- v_emp2 뷰가 있으면 replace(갱신)하고 없으면  create(새로 만듦)
CREATE OR REPLACE VIEW v_emp2(emp_id, first_name, job_id, hire_date, dept_id)
AS
SELECT employee_id, first_name, job_id, hire_date, department_id
FROM employees
WHERE job_id = 'SH_CLERK';



CREATE OR REPLACE VIEW v_emp2(emp_id, first_name, job_id, hire_date, dept_id)
AS
SELECT nvl(employee_id, null), first_name, job_id, hire_date, department_id
FROM employees
WHERE job_id = 'SH_CLERK';

desc v_emp2;

select * from v_emp2;

UPDATE v_emp2 SET first_name = 'Kelly'
where first_name = 'Kim';

select * from employees 
where employee_id = 188;

SELECT employee_id, first_name, ((salary * nvl(commission_pct, 0)) + salary)*12
from employees;

CREATE VIEW v_emp_salary(emp_id, first_name, annual_sal)
AS
SELECT employee_id, first_name, ((salary * nvl(commission_pct, 0)) + salary)*12
from employees;

-- 읽기 전용
CREATE VIEW v_emp_readonly(emp_id, first_name, annual_sal)
AS
SELECT employee_id, first_name, ((salary * nvl(commission_pct, 0)) + salary)*12
from employees
WITH read only;

-- 테이블을 조인한 뷰 만들기
-- CREATE OR REPLACE VIEW_
CREATE VIEW v_join(사번, 이름, 부서번호, 부서명, 입사일)
AS
SELECT 
    emp.employee_id, 
    emp.first_name || ' ' || emp.last_name, 
    emp.department_id,
    dept.department_name,
    emp.hire_date
FROM employees emp, departments dept
WHERE emp.department_id = dept.department_id;

select * from v_join;

-- 10년전 입사자들의 아이디와 이름을 조회
-- 그리고 연봉은 100000이상받는 사원, 부서아이디는 50, 직책 ST_CLERK
CREATE OR REPLACE VIEW v_sample1(emp_id, name, dpt_id, hire_date, year_salary)
AS
SELECT
    employee_id,
    first_name || ' ' || last_name,
    department_id,
    hire_date,
    (salary + (salary * nvl(commission_pct, 0)))*12
FROM employees
WHERE
    (sysdate - hire_date)/365 >= 10
    and (salary + (salary * nvl(commission_pct, 0)))*12 >= 40000
    and department_id = 50 and job_id = 'ST_CLERK';

select * from employees;


