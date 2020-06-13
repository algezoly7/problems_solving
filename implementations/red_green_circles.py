#for more informations copy this link: https://www.hackerrank.com/contests/easyhack4/challenges/red-green-circles/copy-from/1323758099
def red_green_circles():
    n, a, b = map(int, input().split())
    difference = n % (a + b)
    if(difference == 0):
        rounds = n // (a + b)
        return(rounds * a)
    else:
        rounds = n // (a + b)
        bonus = min(difference, a)
        return(rounds * a + bonus)
print(red_green_circles())