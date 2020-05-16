#for more informations copy this link: https://www.hackerrank.com/contests/easyhack4-warmup/challenges/warrag-loves-fibonacci
def nth_fibonacci_number():
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
        print(b)
T = int(input())
for _ in range(T):
    nth_fibonacci_number()