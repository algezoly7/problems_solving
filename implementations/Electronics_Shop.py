# for more informations copy this link : https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    items_required = False
    items_coast = 0
    for i in range(0, n):
        for num in range(0, m):
            new_items_coast = keyboards[i] + drives[num]
            if(new_items_coast > items_coast and new_items_coast <= b):
                items_coast = new_items_coast
                items_required = True
    if(items_required == True):
        return(items_coast)
    else:
        return(-1)

if __name__ == '__main__':
    
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
