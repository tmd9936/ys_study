# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1

# for i in number_generator(3):
#     print(i)

def prime_generator(end):
    prime_check = [True]*(end+1)
    
    for i in range(2, end+1):
        if prime_check[i]:
            for j in range(i*2, end+1, i):
                prime_check[j] = False
            yield i
        

for p in prime_generator(50):
    print(p)
        
            

