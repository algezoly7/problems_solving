#for more informations copy this link: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
#Soucre: coursera & GeeksForGeeks
def knapsack_without_repetation():
    values = list(map(int, input().split()))
    n = len(values)
    weights = list(map(int, input().split()))
    max_weight = 10
    max_value = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]
    print(max_value)
    for i in range(1, n + 1):
        for w in range(1, max_weight +1):
            if(weights[i - 1] <= w):
                max_value[i][w] = max(max_value[i - 1][w - weights[i-1]] + values[i-1], max_value[i-1][w])
            else:
                max_value[i][w] = max_value[i - 1][w]
    print(max_value)
    return(max_value[n][max_weight])
print(knapsack_without_repetation())