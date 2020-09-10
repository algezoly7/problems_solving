#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/bit-5/problem

n = int(input())
x = 0
for _ in range(n):
    opr = input()
    if(opr == '+'):
        x = x + 1
    else:
        x = x - 1
print(x)