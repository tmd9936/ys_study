/* group by �� */

select 
    DISTINCT department_id 
from 
    employees;

select department_id from employees
group by department_id;

-- �μ��� �޿��� �հ�

select department_id, sum(salary) from employees
group by department_id
order by department_id;

-- �μ��� ������� �μ��� �� �޿�, �μ��� ��� �޿�

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

-- �μ��� ���޺� ������� ��� �޿��� ��ȸ�Ͻÿ�.

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
    to_char(sum(salary), '999,999') "�ѱ޿�",
    to_char(avg(salary), '999,999') "��ձ޿�"
from 
    employees
where
    department_id = 80
group by 
    department_id, job_id
order by 
    department_id, job_id;


