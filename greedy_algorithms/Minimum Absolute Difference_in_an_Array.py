#for more informations copy this link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
#Source: HackerRank
def minimum_absolute_difference():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    minimum_difference = 10000000000
    for i in range(n - 1):
        difference = abs(arr[i] - arr[i+1])
        if(difference < minimum_difference):
            minimum_difference = difference
    return(minimum_difference)
print(minimum_absolute_difference())