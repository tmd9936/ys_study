/*
    DML(Data Mnipulation Language) : ������ ���۾�
    select��, delete��, insert��, update��
    
    -- ����
    -- select ��
    select �÷�, �÷�2,....
    from ���̺�1, ���̺�2
    where ����
    group by �÷�, �÷�2,...
    having by ����
    order by �÷�;
    
    
    -- insert ��
    // ���̺��� ���ڵ�(row)�� �Է��ϴ� ��ɾ�
    -- �÷� ������ ���� ������ ����
    -- ���� ���� ���� �� �÷� Ÿ�԰� ��ġ�ؾ� �Ѵ�.
    insert into ���̺��(�÷�1, �÷�2, �÷�3,...) 
    values (��1, ��2, ��3);
    
    -- update ��
    update ���̺�� set Į��1 = ��, Į��2 = ��,...
    where ����..;
    
    -- delete ��
    delete from ���̺��
    where ����;
    
*/

-- ���� sample ���̺��� �˷� �÷� ������ ���弼��.
-- �μ���ȣ, �μ���, �μ���ġ, �μ��Ŵ���

create table sample (
    depNo NUMBER(20),
    depName varchar(20),
    depAddress varchar(100),
    depManager varchar(20)
    
);

insert into sample (
    depNo,
    depName,
    depAddress,
    depManager
) values (
    20,
    '�λ��',
    '���� ���α� �ＺŸ�� 2F 201ȣ',
    'ȫ�浿'
);

desc sample;

select * from sample;

update sample
set
    depManager = '��ö��'
where
    depNo = 20;

update sample
set
    depaddress = '���ֽ� ����Ÿ��'
where
    depNo = 20;

delete from sample
where
    depno = 20;

/*    
    ����Ŭ ������ Ÿ��(DataType)
    : Į���� ����Ǵ� �������� ����(����)
    ���� : ������, ������, ��¥ (�ð�), LOB(Large Object)
    
    -- ������ ������
    // �������� : ó�� char(20)���� ���� �� �� 'abc'�� �־ ������ 20byte�� �����
    // ���� : ó�� char(20)���� �����ؼ� 'abc'�� ������ 3byte�� �����
    char(n) : �������� ����(max: 2000byte, default: 1byte) 
    varchar2(n) : �������� ����(max: 4000byte, default: 1byte)
    nchar(n) : ��������(�����ڵ�)(max: 2000byte, default: 1byte) 
    nvarchar(n) : �������� ����(max: 2000byte, default: 1byte)
    long : �������� ����(max: 2GB, default: 1byte) 
    
    -- ������ ������ (��κκ� number�� ���� ����.)
    number(p, s) : p(��ü �ڸ���), s(�Ҽ��� �����ڸ�)(max: 22byte) 
                   ���� ���� (p, s�� �Է����� ������ �ڵ����� ����)
    float(p) : number�� ����Ÿ��(max: 22byte)
    binary_float : 32��Ʈ �ε� �Ҽ��� (max: 4byte)
    binary_double : 64��Ʈ �ε� �Ҽ��� (max: 8byte)
    
    -- ��¥ ������
    date : ��¥�� �ð�(��/��/��/��/��/��)
    timestamp : ��/��/��/��/��/��/�и���
    
    -- LOB Ÿ�� (��뷮 ���� Ÿ��)
    clob : ���� ���� ��ü�� ������ ��
    nclob : ���� �����ڵ� ������ ����
    blob :  ���� ���� ��ü�� ������ ��(�̹���, ������, ����)
    bfile: ���� ���������� ��ġ, �̸��� ������ ��
*/

-- ���� book ���̺��� �����Ͽ� ���ڵ带 �Է��ϼ���.
-- �÷� ���� : å�ڵ�, å����, å����, �Ⱓ��

drop table book;

create table book (
    book_id number(10), 
    title varchar2(40),
    author varchar2(20),
    pdate date
    
);

-- ��� Į������ ���������� Į���� ���� ����
insert into book 
values(199, '���̽��� ���� Ȱ��', 'ȫ�浿', '2020/03/03');

select * from book;

-- null  �� �ֱ�
insert into book
values (300,'c���', '��浿', '2019/11/11');

-- ���� 300�� �ڵ��� å������ '������ �м�'���� �����ϼ���.

update book 
set title = '������ �м�'
where
    book_id = 300;
    
delete from book
where title = 'java';

delete book;
select * from book;

truncate table book;

select * from sample;

insert into samples
values (200, '������', '��õ', '����');

insert into sample
values (300, 'IT���ߺ�', '����', '�ڿ���');

commit;

-- ���� [IT �μ��� ��ġ�� ���ַ� �ٲٱ�] �׸���
-- rollback ����� ������ , sample ���̺��� Ȯ��

update sample
set
    depaddress = '����'
where
    depno = 300;

SELECT * FROM sample;

-- ������ Ŀ���� �κ����� �ٽ� �ǵ��ư� 
rollback;
commit;

-- Ʈ����� (�۾� ����)
/*
    a-1, a-2, a-3�� �� ���� �Ǿ� �ϴ� �۾��̶��
    ���� a-2���� ������ �߻��ϸ� ��� �۾��� �ѹ��ϰ�
    �ٽ� ó������ ���۵Ǿ� ��
    ���� ��ü ������ ���������� ������ �� �� commit
*/

drop table itBook;

create table itBook(
    bCode number(4),
    title varchar2(20),
    author varchar2(10),
    publisher varchar2(20),
    pubDate date default sysdate
);

desc book;

insert into book(
    book_id,
    title,
    AUTHOR,
    pDate
) values (
    201,
    'C#',
    '��C',
    sysdate
);

insert into itBook(bCode, title, author, publisher)
values (101, 'python ����', 'jh', 'jh����');

select * from itBook;

-- ���� �Ʒ��� ������ member ���̺��� ����� ȸ�������� �߰��ϼ���.
-- �̸�, ���̵�, ��й�ȣ, ����, ��������

drop table member;

create table member(
    mname varchar2(20),
    mid varchar(20),
    password varchar(20),
    age number(2),
    regDate date default sysdate
);

insert into member(mname, mid, password, age)
values ('ȫ�浿', 'test123', '123456', 20);

select * from member;