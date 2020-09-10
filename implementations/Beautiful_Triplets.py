#for more informations copy this link: https://www.hackerrank.com/challenges/beautiful-triplets/problem

def beautifulTriplets(d, arr):
    counter = 0
    for i in range(0, n-2):
        if(arr[i] + d in arr and arr[i] + d * 2 in arr):
            counter += 1
    return(counter)

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)
