#for more informations copy this link: geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

def smaller_to_left(arr, n):
    s = []
    for i in range(n):
        while(len(s) > 0 and s[-1] >= arr[i]):
            s.pop()

        if(len(s) == 0):
            print('_', end = ', ')
        else:
            print(s[-1], end = ', ')
        s.append(arr[i])
    

arr = list(map(int, input().split()))
n = len(arr)
smaller_to_left(arr, n)