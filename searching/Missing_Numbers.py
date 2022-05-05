#for more informations copy this link: https://www.hackerrank.com/challenges/missing-numbers/problem
def missing_number():
    n = int(input())
    #not needed in this solution
    arr = list(map(int, input().split()))
    m = int(input())
    #not needed in this solution
    brr = list(map(int, input().split()))
    m = max(brr) + 1
    #the (+ 1) is for the index
    list_ = [0] * m
    for i in brr:
        list_[i] += 1
    for i in arr:
        list_[i] -= 1
    result = sorted([item for item in range(len(list_)) if list_[item] != 0])
    print(" ".join(map(str, result)))
missing_number()