#for more informations copy this link: https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    maximum = 0
    for k in arr:
        freq = arr.count(k)
        maximum = max(maximum, freq)
    number_of_dels = n - maximum
    return(number_of_dels)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
