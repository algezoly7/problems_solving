#for more informations copy this link: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
#Source: HackerRank
def transmitters():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    counter = 0
    i = 0
    while(i < n):
        counter += 1
        next_point = arr[i] + k
        while(i < n and arr[i] <= next_point):
            i += 1
        next_point = arr[i - 1] + k
        while(i < n and arr[i] <= next_point):
            i += 1
    return(counter)
print(transmitters())
