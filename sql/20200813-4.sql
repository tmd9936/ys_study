-- 날짜 관련 함수

-- sysdate : 현재 시스템의 날짜
select sysdate from dual;

-- months_between() 날짜사이의 기간
select months_between(sysdate, '2020/01/01') from dual;

-- last_day : 지정한 날짜의 해당 월의 마지막날짜를 구함
select last_day(sysdate) from dual;

-- 50번 부서의 사원들의 근무 개월 수를 파악
select 
    first_name, 
    months_between(sysdate, hire_date)
from
    employees
where  
    department_id = 50;
    
-- add_months() : 현재 달로 부터 지정한 달의 날짜를 수함
select add_months(sysdate, 7) from dual;

-- next_day() :
select next_day(sysdate, '일요일') "다음 일요일" from dual; -- 다음 일요일
select next_day(sysdate, '월요일') "다음 월요일" from dual;    
 
select next_day(sysdate - 8, '일요일') "이전 일요일" from dual; -- 이전 일요일    
select next_day(sysdate, '월요일') "이전 월요일" from dual;    

-- to_char() : 스트링 값으로 변경
select first_name, to_char(e.hire_date) from employees e;

-- nvl() : 널 값을 다른 값으로 변경
select first_name, nvl(e.commission_pct, 0) from employees e;

-- case() : elseif문과 같은 역활 함수
select first_name, department_id,
    case when department_id = 20 then '마케팅부'
    when department_id = 60 then '전산실'
    when department_id = 90 then '전략기획실'
    else ''
    end "부서명"
from employees;