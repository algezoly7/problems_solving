#determine the minimum stops a car will make for fuel before reaching it's destination
def minimumrefiles(arr, n, l, end):
    numfills = 0
    current_refill = 0
    while(arr[current_refill] < end):
        last_refill = current_refill
        while(current_refill + 1 <= n - 1 and arr[current_refill + 1] - arr[last_refill] <= l):
            current_refill += 1
        numfills += 1
        if(current_refill == last_refill and current_refill != n - 1):
            return('Impossible')
    return(numfills - 1)
arr = list(map(int, input().split()))
l = int(input())
end = int(input())
arr.insert(0,0)
arr.append(end)
n = len(arr)
print(minimumrefiles(arr, n, l, end))