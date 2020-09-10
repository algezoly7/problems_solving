#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/source-of-life/problem

def doc():
    a, b, c = map(float, input().split())
    if(c == 1):
        water = round(a / 30) * 1
    elif(c == 2):
        water = round(a / 30) * 1.25 
    elif(c == 3):
        water = round(a / 30) * 1.5
    elif(c == 4):
        water = round(a / 30) * 2
    if(water > b):
        return("Bad, You aren't drinking enough water!")
    else:
        return("Good, You're drinking enough water!")
t = int(input())
for _ in range(t):
    print(doc())