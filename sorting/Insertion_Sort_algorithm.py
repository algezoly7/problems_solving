#for more informations copy this link: https://www.hackerrank.com/challenges/insertionsort2/problem

n = int(input())
arr = list(map(int, input().rstrip().split()))
def insertionSort2():
    for i in range(1, n):
        the_num = arr[i]
        previous_index = i - 1
        while(previous_index >= 0 and arr[previous_index] > the_num):
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1
        arr[previous_index + 1] = the_num
        print(" ".join(str(j) for j in arr))
insertionSort2()
