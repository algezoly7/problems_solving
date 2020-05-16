import math
def median_after_addtion():
    n = int(input())
    arr_1 = list(map(int, input().split()))
    arr_2 = [arr_1[0]]
    arr_3 = []
    num = str(round(float(arr_1[0]), 1))
    arr_3.append(num)
    for i in range(1, n):
        elements = i + 1
        arr_2.append(arr_1[i])
        arr_2.sort()
        if(elements % 2 == 1):
            index = math.ceil(i/2)
            num = str(round(float(arr_2[index]), 1))
            arr_3.append(num)
        else:
            index, index_2 = int(i/2) , int((i/2) + 1)
            num = str(round(((arr_2[index] + arr_2[index_2]) / 2), 1))
            arr_3.append(num)
    print(" ".join(arr_3))
T = int(input())
for _ in range(T):
    median_after_addtion()
