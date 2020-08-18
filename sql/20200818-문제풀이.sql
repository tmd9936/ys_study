-- emp ���̺��� Ŀ�̼��� �ִ� ����� �̸��� Ŀ�̼��� ����ϴ� ����� �ۼ��Ͻÿ�
select first_name, last_name, commission_pct
from employees
where commission_pct is not null;

-- �ְ��� ����� �̸��� �Ի糯¥�� ����ϴ� ��ɹ��� �ۼ��Ͻÿ�
select first_name, last_name, hire_date 
from employees
where hire_date = (select min(hire_date) from employees);

-- ���� �ֱ� �Ի��� ����� first�̸��� �Ի� ��¥�� ����ϴ� ��ɹ��� �ۼ��Ͻÿ�.
select first_name, last_name, hire_date
from employees
where hire_date = (select max(hire_date) from employees);

-- �ִ� �޿��� �޴� ����� first �̸��� �޿��� ����ϴ� ��ɹ��� �ۼ��Ͻÿ�.
select first_name, salary
from employees
where salary=(select max(salary) from employees);

-- �μ��� ������� ��� �޿��� ���ϴ� ��ɹ��� �ۼ��Ͻÿ�.
select count(*), round(avg(salary)), department_id
from employees
group by department_id;

-- ������� 10�� ������ �μ�_ID�� ������� ����ϴ� ����� �ۼ��Ͻÿ�.(��, null���� ����)
select count(*), department_id
from employees e1
where department_id is not null 
    and (select count(*) from employees e2 
            where e2.department_id = e1.department_id) <=10
group by department_id;

-- ���� �� ���̺��� �����Ͽ� ����� ���� �μ���� ��å���� ����ϴ� ����� �ۼ��Ͻÿ�
select e.first_name, e.last_name, d.department_name, j.job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id;

-- ��� �޿����� ���Թ޴� ������� ��ܰ� ��å�� ����ϴ� ����� �ۼ��Ͻÿ�.
select e.first_name, e.last_name, j.job_title
from employees e, jobs j
where e.salary < (select avg(salary) from employees);

-- ���̵� 100���� �μ����� ������ ���� �޴� ����� ���̵�� �μ����̵�, ������ ����ϴ� �����
-- �ۼ��Ͻÿ�
-- 100�� ��� �������?

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

-- emp ���̺�� ���� emp2 ���̺��� �����ϴ� ��ɹ��� �ۼ��Ͻÿ�.
create table employees2
as select * from employees;

alter table employees2 drop column manager_id;

create table emp(
    job varchar(20) not null,
    constraint chk_job check(job in('���','�븮','����','����','����'))
);

insert into emp
values('�븮');

drop table emp;

select department_id, count(*) from employees
where department_id is not null
group by department_id
having count(*) <= 10;

