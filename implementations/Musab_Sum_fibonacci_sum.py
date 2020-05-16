#for more informations copy this link: https://www.hackerrank.com/contests/easyhack4-warmup/challenges/musabsum

def fibnacci_sum_till_n():
    sum_ = 1
    n = int(input())
    a = 0
    b = 1
    if(n == 0):
        print(a)
    elif(n == 1):
        print(b)
    else:
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
            sum_ = sum_ + b
        print(sum_)
T = int(input())
for _ in range(T):
    fibnacci_sum_till_n()