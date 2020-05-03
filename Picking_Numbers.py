#for more informations copy this link: https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    maximum = 0
    for k in a:
        n1 = a.count(k)
        n2 = a.count(k - 1)
        maximum = max(maximum, n1 + n2)
    return(maximum)
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
