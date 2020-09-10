#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/open-the-chest

n = int(input())
arr = list(map(str, input().split()))
tracker = False
j = 1
for i in range(n):
    if(j == 1):
        if(arr[i] == 'white'):
            j = 2
        elif(arr[i] == 'black'):
            j = 5
        else:
            j = 1
    elif(j == 2):
        if(arr[i] == 'purple'):
            j = 3
        elif(arr[i] == 'green'):
            j = 4
        else:
            j = 1
    elif(j == 3):       
        if(arr[i] == 'red' or arr[i] == 'orange'):
            break
        elif(arr[i] == 'white'):
            j = 2
        elif(arr[i] == 'black'):
            j = 5
        elif(arr[i] == 'purble'):
            j = 3
        elif(arr[i] == 'green'):
            j = 4
    elif(j == 4):
        if(arr[i] == 'black'):
            j = 5
        elif(arr[i] == 'purple'):
            j = 3
        elif(arr[i] == 'orange'):
            break
        else:
            j = 1
    elif(j == 5):
        if(arr[i] == 'orange'):
            j = 6
        elif(arr[i] == 'white'):
            j = 1
        else:
            j = 1
    elif(j == 6):
        if(arr[i] == 'red'):
            j = 7
        elif(arr[i] == 'purple'):
            j = 3
        elif(arr[i] == 'black'):
            j = 5
        else:
            j = 1
    elif(j == 7): 
        tracker = True
        break
if(tracker == True or j == 7):
    print('GOLD')
else:
    print('LOCKED')