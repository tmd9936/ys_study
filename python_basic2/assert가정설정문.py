# a = 3
# assert a==2

lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]

def test(t):
    assert type(t) is int, '정수가 아닌데'

for t in lists:
    test(t)