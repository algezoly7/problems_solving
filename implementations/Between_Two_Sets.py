#for more informations copy this link: https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    array = []
    for i in range(arr[0], brr[m - 1] + 1):
        array.append(i)

    for i in range(len(array)):
        for x in range(n):
            if(array[i] % arr[x] != 0):
                array[i] = "#"
                break

    for i in range(len(array)):
        if(array[i] != "#"):
            for x in range(m):
                if(brr[x] % array[i]):
                    array[i] = "#"
                    break

    counter = 0
    for i in range(len(array)):
        if(array[i] != "#"):
            counter += 1
    return(counter)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
