#for more informations copy this link: https://www.geeksforgeeks.org/window-sliding-technique/
#Source: GeeksForGeeks

def max_sum(arr, n, k): 
    window_sum = sum(arr[:k])
    max_ = window_sum 
 
    for i in range(n-k): 
        window_sum = window_sum - arr[i] + arr[i + k] 
        max_ = max(window_sum, max_) 
  
    return max_

arr = list(map(int, input().split()))
n = int(input())
k = int(input())
print(max_sum(arr, n, k))
