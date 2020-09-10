#for more informations copy this link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    counter = 0

    for i in range(n):

        for j in range(i + 1, n):

            if((ar[i] + ar[j]) % k == 0):
                counter += 1

    return(counter)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
