lett = ['a','b','c','d','e','f','g']
print(lett)
print(len(lett))
lett[0:2] = ['A','B']
print(lett)
lett[0:2] = []
print(lett)
lett[:] = []
print(lett)

a,b = 0,1
while a < 10:
    print(a, end=' ')
    a,b = b, a+b