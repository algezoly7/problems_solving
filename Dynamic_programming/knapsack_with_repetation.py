#for more informations copy this link: https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
#Source: coursera & GeeksForGeeks

def knapsack_with_repetation():
    n = int(input())
    #the array of values
    values = list(map(int, input().split()))
    #the array of weights
    weights = list(map(int, input().split()))
    W = int(input())
    max_value = [0] * (W + 1)
    max_value[0] = 0
    for x in range(1, W + 1):
        for i in range(n):
            if(weights[i] <= x):
                #cut and paste tech technick
                val = max_value[x - weights[i]] + values[i]
                max_value[x] = max(val, max_value[x])
    return(max_value[W])
print(knapsack_with_repetation())