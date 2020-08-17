select sysdate from dual;

select to_char(sysdate, 'yyyy-mm-dd') from dual;

/* to_date() */
select to_date('20200814', 'yyyy-mm-dd') from dual; -- �ȹٲ�
select to_date('2020/08/14', 'yyyy-mm-dd') from dual; -- �ȹٲ�

-- oracle�� ȯ�溯�� ��ȸ
select * from v$nls_parameters;

-- ��¥ ���� ����
alter session set nls_date_format = 'YYYY-MM-DD';

-- ��¥ ���� Ȯ��
select * from employees;

select to_date('20201111', 'yyyy/mm/dd') from dual;

select to_char(sysdate, 'hh24:MI:SS') from dual;

