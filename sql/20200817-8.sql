/* ���� ���� - �ǹ����� ���� ����ϴ� ���� ��� */
 -- ��� �޿����� ���� �޿��� �޴� ����� ��ȸ�Ͻÿ�
select first_name, last_name,salary
from employees
where salary < 6462;

select first_name, last_name,salary
from employees
where salary < round(avg(salary)); -- where������ �����Լ� ���Ұ�

-- ���������� �����ؼ� ��ȸ�ϱ�
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

-- ������� ���� ���� ������ ���
select location_id
from locations
where country_id ='US';

-- in �����ڸ� ����ϴ� ��
select * from departments
where location_id in(
select location_id
from locations
where country_id ='US'
);

-- ���� �ڵ带 ������ ���� �ٲ㼭 ǥ��
select * from departments
where location_id in(1400, 1500, 1600, 1700);

-- [���� 1] ������ ���� ���� ����� �̸��� ��å���� ��ȸ
select emp.first_name, job.job_title
from employees emp, jobs job
where emp.salary = (select min(salary) from employees)
and emp.job_id = job.job_id;

-- [���� 2] ��� �޿����� ���� �޴� ������� ��ܰ� ��å�� ��ȸ
select avg(salary) from employees;
select emp.first_name, job.job_title
from employees emp, jobs job
where (select round(avg(salary)) from employees) < emp.salary
and emp.job_id = job.job_id;
