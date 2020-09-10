#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/a-smart-lightbulb

arr = [0] * 25
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] -= 1
tracker = 0
time = 0
for i in range(25):
    if(arr[i] > 0):
        tracker += 1
    elif(arr[i] < 0):
        tracker -= 1
    if(tracker > 0):
        time += 1
print(time)