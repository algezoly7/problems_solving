#for more informations copy this link: https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/
#Source: Geeks For Geeks
def get_number_of_ways():
    n = int(input())
    coins = list(map(int, input().split()))
    length_coins = len(coins)
    ways = [0] * (n + 1)
    length_ways = len(ways)
    ways[0] = 1
    for i in range(length_coins):
        for j in range(1, length_ways):
            if(coins[i] <= j):
                ways[j] = ways[j] + ways[j - coins[i]]
    return(ways[n])
print(get_number_of_ways())