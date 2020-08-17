-- ��¥ ���� �Լ�

-- sysdate : ���� �ý����� ��¥
select sysdate from dual;

-- months_between() ��¥������ �Ⱓ
select months_between(sysdate, '2020/01/01') from dual;

-- last_day : ������ ��¥�� �ش� ���� ��������¥�� ����
select last_day(sysdate) from dual;

-- 50�� �μ��� ������� �ٹ� ���� ���� �ľ�
select 
    first_name, 
    months_between(sysdate, hire_date)
from
    employees
where  
    department_id = 50;
    
-- add_months() : ���� �޷� ���� ������ ���� ��¥�� ����
select add_months(sysdate, 7) from dual;

-- next_day() :
select next_day(sysdate, '�Ͽ���') "���� �Ͽ���" from dual; -- ���� �Ͽ���
select next_day(sysdate, '������') "���� ������" from dual;    
 
select next_day(sysdate - 8, '�Ͽ���') "���� �Ͽ���" from dual; -- ���� �Ͽ���    
select next_day(sysdate, '������') "���� ������" from dual;    

-- to_char() : ��Ʈ�� ������ ����
select first_name, to_char(e.hire_date) from employees e;

-- nvl() : �� ���� �ٸ� ������ ����
select first_name, nvl(e.commission_pct, 0) from employees e;

-- case() : elseif���� ���� ��Ȱ �Լ�
select first_name, department_id,
    case when department_id = 20 then '�����ú�'
    when department_id = 60 then '�����'
    when department_id = 90 then '������ȹ��'
    else ''
    end "�μ���"
from employees;