def number_generator():
    yield 0 # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1 
    yield 2

for i in number_generator():
    print(i)

# return은 반환 즉시 함수가 끝
# yield는 잠시 함수 바깥의 코드가 실행되도록 양보
# 다시말해 값을 전달하면 끝난게 아니라 대기상태로 변환
# 제너레이터 끝에 가면 StopIteration 예외 발생

def one_generator():
    yield 1
    return 'return값'

try:
    g = one_generator()
    next(g)
    next(g)
    next(g)
    next(g)
except StopIteration as e:
    print(e)


