print('Hello, world!'.__iter__())
{'a':1, 'b':2}.__iter__()

it = range(3).__iter__()
print(it.__next__())


def star_diamond(num):
    space = num // 2
    star = 1
    
    for i in range(0, num):
        # 공백
        for x in range(space):
            print(' ', end='')
        # 별
        for x in range(star):
            print('*', end='')
        
        if i < num // 2:
            space -= 1
            star += 2
        else:
            space += 1
            star -= 2
        print()

star_diamond(15)