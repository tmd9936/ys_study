/* join �Ϲ������� '����join' ����� �ǹ��Ѵ�. */
select * from employees;
select * from locations;
desc department;

-- �ΰ��� ���̺� ����
select emp.department_id, emp.first_name, emp.last_name, dep.department_name
from employees emp, departments dep
where emp.department_id = dep.department_id;

-- ������ ���̺� ����
-- ������ �̸�, �̸���, �μ����̵�, �μ���, ���޸��� ��ȸ
select emp.first_name, emp.last_name, emp.email, emp.department_id, dep.department_name, job.job_title
from employees emp, departments dep, jobs job
where emp.department_id = dep.department_id
and emp.job_id = job.job_id;

-- �װ��� ���̺� ����
-- ������ �̸�, �̸���, �μ����̵�, �μ���, ���޾��̵�, ���޸�, �ٹ���ġ�� ��ȸ
select emp.last_name, emp.email, emp.department_id, dep.department_name,
job.job_id, job.job_title, loc.city
from employees emp, departments dep, jobs job, locations loc
where emp.department_id = dep.department_id
and emp.job_id = job.job_id
and dep.location_id = loc.location_id;

-- �Ϲ� ���ǰ� ���� : Seattle���� �ٹ��ϴ� �������� �̸�, �̸���, �μ���, ��å��, Seattle�� ��ȸ
select emp.last_name, emp.email, dep.department_name, job.job_title, loc.city
from employees emp, locations loc, jobs job, departments dep
where dep.location_id = loc.location_id
and emp.department_id = dep.department_id
and emp.job_id = job.job_id
and city = 'Seattle'; -- �Ϲ� ���� ����

/* ���� ���� �ڽ��� ���̺��� �ΰ��� ���̺� ó�� ����ϴ� �� */
select * from employees;

select emp1.employee_id, emp1.first_name, emp2.employee_id ���id, emp2.first_name ����̸�
from employees emp1, employees emp2
where emp1.manager_id = emp2.employee_id;


/* �ܺ� ���� */
-- ���� �������� ���� ��
select emp.employee_id, emp.first_name, dep.department_name
from employees emp, departments dep
where emp.department_id = dep.department_id;

-- �ܺ� �������� ���� ��
select emp.employee_id, emp.first_name, dep.department_name
from employees emp, departments dep
-- ������ �������� �������� �þ Left Outer join
--where emp.department_id = dep.department_id(+);
-- �������� �������� ������ �þ Left Outer join
where emp.department_id(+) = dep.department_id;


-- [����] ��� ����� ���ID�� first_name, �μ���, �ٹ� ���ø� ���
select emp.employee_id, emp.first_name, dep.department_name, loc.city
from employees emp, departments dep, locations loc
where emp.department_id = dep.department_id (+)
and dep.location_id = loc.location_id (+);

-- [����] ��� ����� ���ID�� first_name �׸��� ���ID�� ����̸��� ���
select emp1.employee_id ���id, emp1.first_name ����̸�, emp2.employee_id ���id, emp2.first_name ����̸�
from employees emp1, employees emp2
where emp1.manager_id = emp2.employee_id(+);

select * from employees;