/*  DDL(Data definition Language)
    : Create문, Alter문, Drop문, Truncate문

*/

desc employees;

create table employees2(
    employee_id number(10),
    name varchar(20),
    salary number(7,2) -- 소수점 두자리를 포함
);

desc employees2;

-- 기존 테이블과 똑같은 구조로 생성
create table employees3
as
select * from employees2;

-- 칼럼 추가
alter table employees3 add(
    manager_id varchar2(20)
);

desc employees3;

-- 칼럼 수정
alter table employees3 modify(
    manager_id varchar2(10)
);

-- 칼럼 삭제
alter table employees3 drop column manager_id;

-- 테이블 구조를 완전히 삭제
drop table employees3;

desc employees2;

-- 구조는 있지만 레코드가 지워짐.
truncate table employees2;

select * from employees2;

