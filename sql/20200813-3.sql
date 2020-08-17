/* 문자열 함수 */

-- concat(str1, str2) 문자열 합침

select concat('Hello', 'Bye') c1, concat('good','night') c2 from dual;
select concat('Hello', 'Bye') c1, 'good' || 'night' c2 from dual;

-- initcap(str) 첫글자를 대문자로 바꿔주는 함수
select initcap('good mornig') from dual;

-- 공백이 들어가면 구분자로 생각하고 첫글자를 대문자로 표현함
select initcap(' good/morning hello') from dual;

-- lower(), upper() : 소문자로, 대문자로 변환
select lower('GOOD'), upper('good') from dual;

-- LPAD(), RPAD() 공백(passing) 값을 왼쪽, 오른쪽에 줌
select 
    lpad('good', 6, '+'),
    lpad('good', 7, '#'),
    lpad('good', 8, 'L'),
    lpad('good', 8, '고'),
    lpad('홍길동', 8, '@')
from dual;

-- lpad()
select 
    lpad('홍길동', 8, '#')
from dual;

select 
    rpad('good', 6, '+'),
    rpad('good', 7, '#'),
    rpad('good', 8, 'L'),
    rpad('good', 8, '고'),
    rpad('홍길동', 8, '@')
from dual;

-- ltrim(), rtrim()
-- 중간에 있는 경우는 지우는게 불가
-- go를 지울 경우 o가 있는 만큼 지움
select 
    ltrim('goodbye', 'g'),
    ltrim('goodbye', 'o'),
    ltrim('goodbye', 'go')
from dual;

select
    rtrim('goodbye','e'),
    rtrim('goodbye','odbye')
from dual;

-- substr(str, 시작부분, 잘라 낼 갯수) 잘라내는 함수
select substr('good morning john', 8, 4) from dual;
select substr('good morning john', 8) from dual;

-- 뒤에서 4번째 글자부터 끝까지 반환
select substr('good morning john', -4) from dual;
select substr('good morning john', -4, 2) from dual;
select substr('good morning john', -4, 0) from dual;

-- replace() 문자 교체
select replace('good morning tom', 'morning', 'evening') from dual;

-- trim() : 공백 제거
select length('   good    ') from dual;
select length(trim('   good    ')) from dual; -- 좌우 공백이 삭제
select length(trim(both from '   good    ')) from dual; -- 좌우 공백이 삭제

-- 죄측공백 없애기
select length(trim(leading from '   good    ')) from dual; --

-- 우측 공백 없에기
select length(trim(trailing from '   good    ')) from dual; 

-- instr(문장, 찾을 문장, 시작 인덱스, 찾을 문장의 순서) 문자열의 위치값을 찾는 함수
select instr('good morning john', 'o', 1) from dual;
-- 세번째 'o'의 위치값
select instr('good morning john', 'o', 3) from dual;
-- 네번째 'o'의 위치값
select instr('good morning john', 'o', 8) from dual;

-- 첫번째 부터 시작해서 4번째 o의 위치값을 찾음
select instr('good morning john', 'o', 1, 4) from dual;

-- 세번째 'n'의 위치값
select instr('good morning john', 'n', 1, 3) from dual;















