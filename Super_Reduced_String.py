#for more informations copy this link: https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    arr = []
    for k in s:
        if(not arr):
            arr.append(k)
        else:
            if(arr[-1] == k):
                arr.pop()
            else:
                arr.append(k)
    if(not arr):
        return('Empty String')
    else:
        return(''.join(arr))
    
if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result)