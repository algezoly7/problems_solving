#for more informations copy this link: https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a):
    minimum = 1001
    for i in range(n - 1):
        for num in range(i+1, n):
            if(a[i] == a[num]):
                distance = abs(i - num)
                minimum = min(minimum, distance)
    if(minimum == 1001):
        minimum = -1
    return(minimum)

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)