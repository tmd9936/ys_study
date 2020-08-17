input('더미')

# def gold_bah(arg):
#     max_num = math.ceil(math.sqrt(arg))
#     is_prime = [False,False] + [True]*(arg-1)
#     prime_dict = dict()

#     for i in range(2, max_num):
#         if is_prime[i]:
#             for j in range(i*2, arg+1, i):
#                 is_prime[j] = False

#     for i, check in enumerate(is_prime):
#         if check:
#             prime_dict[i] = True

#     gold_bah_list = []
#     for k1,v1 in prime_dict.items():
#         if v1:
#             for k2,v2 in prime_dict.items():
#                 if k1 + k2 == arg:
#                     prime_dict[k1] = False
#                     prime_dict[k2] = False
#                     gold_bah_list.append([k1,k2])

#     result = [gold_bah_list[0][0],gold_bah_list[0][1]]
#     for cop in gold_bah_list:
#         if abs(result[0]-result[1]) > abs(cop[0]-cop[1]):
#             result = [cop[0], cop[1]]
    

#     print(result[0], result[1])

def prime_list(arg):
    max_num = int(arg ** 0.5)
    is_prime = [True]*(arg)

    for i in range(2, max_num + 1):
        if is_prime[i]:
            for j in range(i*2, arg, i):
                is_prime[j] = False

    return [i for i in range(2,len(is_prime)) if is_prime[i]]

def gold_bah(arg):
    primes = prime_list(arg)

    for i in primes[int(len(primes)/2):]:
        for j in primes[int(len(primes)/2)-1::-1]:
            if i+j == arg:
                print(j,i)
                return
    
for _ in range(int(input())):
    n=int(input())
    gold_bah(n)