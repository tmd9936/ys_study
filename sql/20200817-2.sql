/*
    DML(Data Mnipulation Language) : 데이터 조작어
    select문, delete문, insert문, update문
    
    -- 형식
    -- select 문
    select 컬럼, 컬럼2,....
    from 테이블1, 테이블2
    where 조건
    group by 컬럼, 컬럼2,...
    having by 조건
    order by 컬럼;
    
    
    -- insert 문
    // 테이블의 레코드(row)를 입력하는 명령어
    -- 컬럼 갯수와 값의 객수가 동일
    -- 값을 넣을 때는 각 컬럼 타입과 일치해야 한다.
    insert into 테이블명(컬럼1, 컬럼2, 컬럼3,...) 
    values (값1, 값2, 값3);
    
    -- update 문
    update 테이블명 set 칼럼1 = 값, 칼럼2 = 값,...
    where 조건..;
    
    -- delete 문
    delete from 테이블명
    where 조건;
    
*/

-- 문제 sample 테이블을 알래 컬럼 구조로 만드세요.
-- 부서번호, 부서명, 부서위치, 부서매니저

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
    '인사부',
    '서울 종로구 삼성타워 2F 201호',
    '홍길동'
);

desc sample;

select * from sample;

update sample
set
    depManager = '김철수'
where
    depNo = 20;

update sample
set
    depaddress = '제주시 제주타워'
where
    depNo = 20;

delete from sample
where
    depno = 20;

/*    
    오라클 데이터 타입(DataType)
    : 칼럼에 저장되는 데이터의 형식(유형)
    종류 : 문자형, 숫자형, 날짜 (시간), LOB(Large Object)
    
    -- 문자형 데이터
    // 고정길이 : 처음 char(20)으로 설정 한 후 'abc'만 넣어도 무조건 20byte가 저장됨
    // 가변 : 처음 char(20)으로 설정해서 'abc'를 넣으면 3byte가 저장됨
    char(n) : 고정길이 문자(max: 2000byte, default: 1byte) 
    varchar2(n) : 가변길이 문자(max: 4000byte, default: 1byte)
    nchar(n) : 고정길이(유니코드)(max: 2000byte, default: 1byte) 
    nvarchar(n) : 가변길이 문자(max: 2000byte, default: 1byte)
    long : 가변길이 문자(max: 2GB, default: 1byte) 
    
    -- 숫자형 데이터 (대부부분 number를 많이 쓴다.)
    number(p, s) : p(전체 자리수), s(소수점 이하자리)(max: 22byte) 
                   가변 숫자 (p, s를 입력하지 않으면 자동으로 조절)
    float(p) : number의 서브타입(max: 22byte)
    binary_float : 32비트 부동 소수점 (max: 4byte)
    binary_double : 64비트 부동 소수점 (max: 8byte)
    
    -- 날짜 데이터
    date : 날짜와 시간(년/월/일/시/분/초)
    timestamp : 년/월/일/시/분/초/밀리초
    
    -- LOB 타입 (대용량 저장 타입)
    clob : 문자 대용령 객체를 저장항 때
    nclob : 대용령 유니코드 문자형 저장
    blob :  이진 대용령 객체를 저장할 때(이미지, 동영상, 사운드)
    bfile: 대용령 이진파일의 위치, 이름을 저장할 때
*/

-- 문제 book 테이블을 생성하여 레코드를 입력하세요.
-- 컬럼 구조 : 책코드, 책제목, 책저자, 출간일

drop table book;

create table book (
    book_id number(10), 
    title varchar2(40),
    author varchar2(20),
    pdate date
    
);

-- 모든 칼럼값을 넣을때에는 칼럼명 생략 가능
insert into book 
values(199, '파이썬을 쉽게 활용', '홍길동', '2020/03/03');

select * from book;

-- null  값 넣기
insert into book
values (300,'c언어', '김길동', '2019/11/11');

-- 문제 300번 코드의 책제목을 '데이터 분석'으로 변경하세요.

update book 
set title = '데이터 분석'
where
    book_id = 300;
    
delete from book
where title = 'java';

delete book;
select * from book;

truncate table book;

select * from sample;

insert into samples
values (200, '영업부', '인천', '김상사');

insert into sample
values (300, 'IT개발부', '대전', '박영희');

commit;

-- 문제 [IT 부서의 위치를 광주로 바꾸기] 그리고
-- rollback 명령을 내리고 , sample 테이블을 확인

update sample
set
    depaddress = '광주'
where
    depno = 300;

SELECT * FROM sample;

-- 마지막 커밋한 부분으로 다시 되돌아감 
rollback;
commit;

-- 트랜잭션 (작업 단위)
/*
    a-1, a-2, a-3가 한 번에 되야 하는 작업이라면
    만약 a-2에서 에러가 발생하면 모든 작업을 롤백하고
    다시 처음부터 시작되야 함
    만약 전체 과정이 정상적으로 끝나면 그 때 commit
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
    '김C',
    sysdate
);

insert into itBook(bCode, title, author, publisher)
values (101, 'python 기초', 'jh', 'jh출판');

select * from itBook;

-- 문제 아래의 구조로 member 테이블을 만들고 회원정보를 추가하세요.
-- 이름, 아이디, 비밀번호, 나이, 가입일자

drop table member;

create table member(
    mname varchar2(20),
    mid varchar(20),
    password varchar(20),
    age number(2),
    regDate date default sysdate
);

insert into member(mname, mid, password, age)
values ('홍길동', 'test123', '123456', 20);

select * from member;