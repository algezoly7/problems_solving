#for more informations copy this link : https://www.hackerrank.com/challenges/sherlock-and-array/problem
def Sherlock_and_array():
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = n - 1
    left_sum = arr[i]
    right_sum = arr[j]
    while(i != j):
        if(right_sum < left_sum):
            j = j - 1
            right_sum += arr[j]
        else:
            i = i + 1
            left_sum += arr[i]
    return(right_sum == left_sum)
T = int(input())
for _ in range(T):
    if(Sherlock_and_array()):
        print('YES')
    else:
        print('NO')