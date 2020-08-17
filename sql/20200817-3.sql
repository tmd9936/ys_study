/*
    ���Ἲ ��������(constraints)
    : DB�� ��� �ִ�  �������� ��Ȯ��(�ϰ���)�� �����ϵ��� �ϱ� ���� ���������� �ǹ���.
    ��, ����Ȯ�� �ڷᰡ DB�� ����Ǵ� ���� �����ϵ��� �ϴ� ������ ����.
    
    not null: �ΰ��� �Էµ��� ���ϰ� �ϴ� ����
    unique(������) : �ߺ��� ���� �Էµ��� ���ϰ� �ϴ� ���� (null ���� �����)
    primary key(�⺻Ű) : not null + unique(���ϼ��� �����ϴ� Ű)
    foreign key(�ܷ�Ű) : �ٸ� ���̺��� �ʵ�(�÷�)�� �����ؼ� ���Ἲ�� �˻��ϴ� ����
    check : �־��� ���� ����ϴ� ��������(���� : ��,�� ���� �ϳ��� ���)
    
    ���� ���Ἲ(integrity)�̶�?
    :�ܷ�Ű ���� ���� �����̼�(���̺�)�� �⺻Ű ���� �����ؾ� �Ѵٴ� ����
    ��, ���̺��� ������ �� ���� �ܷ�Ű ���� ���� �� ����.
    
    �ڽ����̺�(employees)�θ� ���̵�� �ܷ�Ű
    �θ����̺�(Dempartments)�� �μ����̵�� �⺻Ű(����Ű)
    
    �ܷ�Ű�� �ݵ�� ����Ű ���� �ϳ����� �Ѵ�.
    ����Ű�� ���� �ܷ�Ű�� ���� �� ����
    
    
*/

-- not null ���� ����
create table null_test (
    col_1 varchar2(20) not null,
    col_2 varchar2(20) null,
    col_3 varchar2(20)
);

desc null_test;

insert into null_test(col_1, col_2)
values ('aa', 'bb');

insert into null_test(col_2, col_3)
values ('aa', 'bb');

select * from null_test;

drop table unique_test;

create table unique_test(
    col_1 varchar2(20) unique not null,
    col_2 varchar2(20) unique,
    col_3 varchar2(20) not null,
    col_4 varchar2(20) not null,
    
    -- �ƿ����� ���
    -- constraint �������Ǹ� ��������(�÷�1, �÷�2...)
    constraint c_unique unique (col_3, col_4)
);

/*
    1. constraint c_unique unique (col_3, col_4)
    2. constraint c_unique unique (col_3)
       constraint c_unique unique (col_4)
    
    1�� 2�� ������: 2���� ���� ����ũ ���� Ȯ��������,
    1���� col_3�� col_4�� ��� ����ũ ���� Ȯ��
    ��, 2���� �� ���� �ٸ��� ���� �� ����
*/

insert into unique_test
values('aa3',null,'cc3','dd3');

insert into unique_test
values('aa1','bb1','cc1','dd');

insert into unique_test
values('aa2','bb2','cc2','dd');

insert into unique_test
values('aa4','b4','cc4','dd');

update unique_test
set col_1 = 'aa'
where col_4 = 'dd1';

select * from unique_test;

-- c_unique ���������� �����ϼ���.
alter table unique_test
drop constraint c_unique;

-- ���������� �߰�
alter table unique_test 
add constraint c4_unique unique (col_4);

delete from unique_test
where col_1 = 'aa';

/*
    �⺻Ű(primary key) ���̺� ������ �⺻Ű �����
*/

create table primary_test(
    student_id number(10) primary key, -- �ζ��� ���
    name varchar2(20)
);

insert into primary_test
values('','');

insert into primary_test
values(1212,''); -- �ߺ� ��� �ȵ�.

select * from primary_test;

-- [����] primary_test2 ���̺� �⺻Ű�� �ƿ����� �������
-- �����ϼ���. student_id, name

create table primary_test2 (
    student_id number(10),
    name varchar2(20),    
    constraint student_id_pk primary key (student_id) -- �ƿ����� ���
);

create table primary_test3 (
    student_id number(10),
    name varchar2(20)
);

-- ���� ���̺� �⺻Ű�� �߰�
alter table primary_test3 
add constraint student_id_pk primary key(student_id);

insert into primary_test3
values(111,'aa');

-- �ܷ�Ű ��������
create table fk_test (
    department_id 
    constraint dept_fk references departments(department_id)
);

select department_id from departments;

insert into fk_test(
    department_id
) values(
    100
);

insert into fk_test
values(300); -- �������� ����

create table fk_test2 (
    department_id number(4),
    constraint department_id_fk
               foreign key(department_id)
               references departments(department_id)
);

drop table fk_test3;

create table fk_test3 (
    department_id number(4),
    name varchar(20)
);


-- ���̺��� �����ϰ� ���� �ܷ�Ű�� �����ϴ� ���
alter table fk_test3
add constraint dept_fk3 foreign key (department_id)
references departments(department_id);

/* check ���� ���� */
create table check_test (
    gender varchar2(10) not null,
    constraint chk_gender check(gender in('M', 'F'))
);

drop table student;

create table student(
    stu_id number(10),
    name varchar2(10),
    age number,
    birthday date,
    regDate date default sysdate
);

-- check ���������� �̿��� ������ ��ȿ�� �˻�
alter table student
add constraint age_chk
check(round((regdate - birthday)/365) + 1 = age or round((regdate - birthday)/365) + 2 = age );

insert into student
values(
    100,
    'ss',
    28,
    '19931002',
    sysdate
);








    



