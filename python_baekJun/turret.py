def swap(x,y):
    if x >= y:
        return (x,y)
    else:
        return (y,x)


for _ in range(int(input())):
    out = input().split(' ')
    x1,y1,r1,x2,y2,r2 = int(out[0]), int(out[1]), int(out[2]), int(out[3]), int(out[4]), int(out[5])
    dx = x1 - x2
    dy = y1 - y2

    r1, r2 = swap(r1,r2)
    r_sub = (r1 - r2)**2
    r_sum = (r1 + r2)**2
    d = dx**2 + dy**2

    if (d < r_sum and d > r_sub):
        print(2)
    elif (d == r_sum or ((d == r_sub) and (d != 0))):
        print(1)
    elif (d < r_sub or d > r_sum):
        print(0)
    elif (d == 0):
        if (r1 == r2):
            print(-1)
        else:
            print(0)


