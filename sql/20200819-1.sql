/*
    ��(view)
    : ���������� �������� �ʴ� ������ ���̺�
    : �ϳ� �̻��� ���̺��� ��ȸ�ϴ� SELECT���� ������ ��ü
    ���� �뵵
    :����(SELECT���� �������� �ؼ��ϰ��� �� �� ���
    :���ȼ�(���̺��� Ư�� ���� �����ϰ� ���� ���� �� ���)
    ���� ����
    CREATE VIEW ���̸�(�÷�1, �÷�2, ...)
    AS SELECT��
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


-- v_emp2 �䰡 ������ replace(����)�ϰ� ������  create(���� ����)
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

-- �б� ����
CREATE VIEW v_emp_readonly(emp_id, first_name, annual_sal)
AS
SELECT employee_id, first_name, ((salary * nvl(commission_pct, 0)) + salary)*12
from employees
WITH read only;

-- ���̺��� ������ �� �����
-- CREATE OR REPLACE VIEW_
CREATE VIEW v_join(���, �̸�, �μ���ȣ, �μ���, �Ի���)
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

-- 10���� �Ի��ڵ��� ���̵�� �̸��� ��ȸ
-- �׸��� ������ 100000�̻�޴� ���, �μ����̵�� 50, ��å ST_CLERK
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


