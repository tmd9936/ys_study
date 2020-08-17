/*  DDL(Data definition Language)
    : Create��, Alter��, Drop��, Truncate��

*/

desc employees;

create table employees2(
    employee_id number(10),
    name varchar(20),
    salary number(7,2) -- �Ҽ��� ���ڸ��� ����
);

desc employees2;

-- ���� ���̺�� �Ȱ��� ������ ����
create table employees3
as
select * from employees2;

-- Į�� �߰�
alter table employees3 add(
    manager_id varchar2(20)
);

desc employees3;

-- Į�� ����
alter table employees3 modify(
    manager_id varchar2(10)
);

-- Į�� ����
alter table employees3 drop column manager_id;

-- ���̺� ������ ������ ����
drop table employees3;

desc employees2;

-- ������ ������ ���ڵ尡 ������.
truncate table employees2;

select * from employees2;

