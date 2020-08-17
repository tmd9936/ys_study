select sysdate from dual;

select to_char(sysdate, 'yyyy-mm-dd') from dual;

/* to_date() */
select to_date('20200814', 'yyyy-mm-dd') from dual; -- 안바뀜
select to_date('2020/08/14', 'yyyy-mm-dd') from dual; -- 안바뀜

-- oracle의 환경변수 조회
select * from v$nls_parameters;

-- 날짜 형식 변경
alter session set nls_date_format = 'YYYY-MM-DD';

-- 날짜 형식 확인
select * from employees;

select to_date('20201111', 'yyyy/mm/dd') from dual;

select to_char(sysdate, 'hh24:MI:SS') from dual;

