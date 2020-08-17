# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int,a))
# print(a)

# out = map(int, input('입력 : ').split())
# print(list(out))

# x = input().split()
# m = map(int, x)

# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

# print([x + ' n' for x in a if len(x) == 5])

out = input().split()

out_m = list(map(int, out))

p_list = [2**x for x in range(out_m[0], out_m[1]+1)]
del p_list[1]
del p_list[-2]
print(p_list)