/* ���ڿ� �Լ� */

-- concat(str1, str2) ���ڿ� ��ħ

select concat('Hello', 'Bye') c1, concat('good','night') c2 from dual;
select concat('Hello', 'Bye') c1, 'good' || 'night' c2 from dual;

-- initcap(str) ù���ڸ� �빮�ڷ� �ٲ��ִ� �Լ�
select initcap('good mornig') from dual;

-- ������ ���� �����ڷ� �����ϰ� ù���ڸ� �빮�ڷ� ǥ����
select initcap(' good/morning hello') from dual;

-- lower(), upper() : �ҹ��ڷ�, �빮�ڷ� ��ȯ
select lower('GOOD'), upper('good') from dual;

-- LPAD(), RPAD() ����(passing) ���� ����, �����ʿ� ��
select 
    lpad('good', 6, '+'),
    lpad('good', 7, '#'),
    lpad('good', 8, 'L'),
    lpad('good', 8, '��'),
    lpad('ȫ�浿', 8, '@')
from dual;

-- lpad()
select 
    lpad('ȫ�浿', 8, '#')
from dual;

select 
    rpad('good', 6, '+'),
    rpad('good', 7, '#'),
    rpad('good', 8, 'L'),
    rpad('good', 8, '��'),
    rpad('ȫ�浿', 8, '@')
from dual;

-- ltrim(), rtrim()
-- �߰��� �ִ� ���� ����°� �Ұ�
-- go�� ���� ��� o�� �ִ� ��ŭ ����
select 
    ltrim('goodbye', 'g'),
    ltrim('goodbye', 'o'),
    ltrim('goodbye', 'go')
from dual;

select
    rtrim('goodbye','e'),
    rtrim('goodbye','odbye')
from dual;

-- substr(str, ���ۺκ�, �߶� �� ����) �߶󳻴� �Լ�
select substr('good morning john', 8, 4) from dual;
select substr('good morning john', 8) from dual;

-- �ڿ��� 4��° ���ں��� ������ ��ȯ
select substr('good morning john', -4) from dual;
select substr('good morning john', -4, 2) from dual;
select substr('good morning john', -4, 0) from dual;

-- replace() ���� ��ü
select replace('good morning tom', 'morning', 'evening') from dual;

-- trim() : ���� ����
select length('   good    ') from dual;
select length(trim('   good    ')) from dual; -- �¿� ������ ����
select length(trim(both from '   good    ')) from dual; -- �¿� ������ ����

-- �������� ���ֱ�
select length(trim(leading from '   good    ')) from dual; --

-- ���� ���� ������
select length(trim(trailing from '   good    ')) from dual; 

-- instr(����, ã�� ����, ���� �ε���, ã�� ������ ����) ���ڿ��� ��ġ���� ã�� �Լ�
select instr('good morning john', 'o', 1) from dual;
-- ����° 'o'�� ��ġ��
select instr('good morning john', 'o', 3) from dual;
-- �׹�° 'o'�� ��ġ��
select instr('good morning john', 'o', 8) from dual;

-- ù��° ���� �����ؼ� 4��° o�� ��ġ���� ã��
select instr('good morning john', 'o', 1, 4) from dual;

-- ����° 'n'�� ��ġ��
select instr('good morning john', 'n', 1, 3) from dual;















