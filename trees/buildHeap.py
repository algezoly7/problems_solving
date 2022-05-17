# python3
n= int(input())
arr = list(map(int, input().split()))
answer = []
def sift_down(i):
    min_index = i
    l = 2*i + 1
    r = 2*i + 2
    if(l < n and arr[l] < arr[min_index]):
        min_index = l
    if(r < n and arr[r] < arr[min_index]):
        min_index = r
    if(min_index != i):
        arr[min_index],  arr[i] = arr[i], arr[min_index]
        brr = [str(i), str(min_index)]
        answer.append(' '.join(brr))
        sift_down(min_index)
def heapify():
    for i in reversed(range(0, n // 2 + 1)):
        sift_down(i)
heapify()
print(len(answer))
for i in answer:
    print(i)
