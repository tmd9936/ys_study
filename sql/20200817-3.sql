/*
    무결성 제약조건(constraints)
    : DB에 들어 있는  데이터의 정확성(일관성)을 보장하도록 하기 위한 제약조건을 의미함.
    즉, 부정확한 자료가 DB에 저장되는 것을 방지하도록 하는 조건을 말함.
    
    not null: 널값이 입력되지 못하게 하는 조건
    unique(유일한) : 중복된 값이 입력되지 못하게 하는 조건 (null 값을 허용함)
    primary key(기본키) : not null + unique(유일성을 보장하는 키)
    foreign key(외래키) : 다른 테이블의 필드(컬럼)를 참조해서 무결성을 검사하는 조건
    check : 주어진 값만 허용하는 제약조건(성별 : 남,여 중의 하나만 허용)
    
    참조 무결성(integrity)이란?
    :외래키 값은 참조 릴레이션(테이블)의 기본키 값과 동의해야 한다는 규정
    죽, 테이블은 참조할 수 없는 외래키 값을 가지 수 없다.
    
    자식테이블(employees)부모 아이디는 외래키
    부모테이블(Dempartments)의 부서아이디는 기본키(참조키)
    
    외래키는 반드시 참조키 중의 하나여야 한다.
    참조키에 없는 외래키는 있을 수 없다
    
    
*/

-- not null 제약 조건
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
    
    -- 아웃라인 방식
    -- constraint 제약조건명 제약조건(컬럼1, 컬럼2...)
    constraint c_unique unique (col_3, col_4)
);

/*
    1. constraint c_unique unique (col_3, col_4)
    2. constraint c_unique unique (col_3)
       constraint c_unique unique (col_4)
    
    1과 2의 차이점: 2번은 따로 유니크 인지 확인하지만,
    1번은 col_3과 col_4를 묶어서 유니크 인지 확인
    즉, 2번은 한 개만 다르면 넣을 수 있음
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

-- c_unique 제약조건을 삭제하세요.
alter table unique_test
drop constraint c_unique;

-- 제약조건을 추가
alter table unique_test 
add constraint c4_unique unique (col_4);

delete from unique_test
where col_1 = 'aa';

/*
    기본키(primary key) 테이블 생성시 기본키 만들기
*/

create table primary_test(
    student_id number(10) primary key, -- 인라인 방식
    name varchar2(20)
);

insert into primary_test
values('','');

insert into primary_test
values(1212,''); -- 중복 허용 안됨.

select * from primary_test;

-- [문제] primary_test2 테이블에 기본키를 아웃라인 방식으로
-- 설정하세요. student_id, name

create table primary_test2 (
    student_id number(10),
    name varchar2(20),    
    constraint student_id_pk primary key (student_id) -- 아웃라인 방식
);

create table primary_test3 (
    student_id number(10),
    name varchar2(20)
);

-- 위의 테이블에 기본키를 추가
alter table primary_test3 
add constraint student_id_pk primary key(student_id);

insert into primary_test3
values(111,'aa');

-- 외래키 제약조건
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
values(300); -- 제약조건 위배

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


-- 테이블을 생성하고 나서 외래키를 지정하는 방법
alter table fk_test3
add constraint dept_fk3 foreign key (department_id)
references departments(department_id);

/* check 제약 조건 */
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

-- check 제약조건을 이용한 나이의 유효성 검사
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








    



