def coins_change(money, coins):
    length = len(coins)
    least_coins = [float('inf')] * (money + 1)
    least_coins[0] = 0
    for i in range(1, money + 1):
        for j in range(0, length):
            if(i >= coins[j]):
                num_coins = least_coins[i - coins[j]] + 1
                if(num_coins < least_coins[i]):
                    least_coins[i] = num_coins
    return(least_coins[money])
money = int(input())
coins = list(map(int, input().split()))
print(coins_change(money, coins))