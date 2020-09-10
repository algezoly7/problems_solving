#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/io-1000-assembly-simulator

def reconvert(num_):
    first = (num_ // 16)
    second = num_ % 16
    if(first == 10):
        third = 'A'
    elif(first == 11):
        third = 'B'
    elif(first == 12):
        third = 'C'
    elif(first == 13):
        third = 'D'
    elif(first == 14):
        third = 'E'
    elif(first == 15):
        third = 'F'
    else:
        third = str(first)
    
    if(second == 10):
        fourth = 'A'
    elif(second == 11):
        fourth = 'B'
    elif(second == 12):
        fourth = 'C'
    elif(second == 13):
        fourth = 'D'
    elif(second == 14):
        fourth = 'E'
    elif(second == 15):
        fourth = 'F'
    else:
        fourth = str(second)
    word = third + fourth
    return(word)

def reconvert2(num_):
    first = (num_ // 16)
    second = num_ % 16
    if(first == 10):
        third = 'A'
    elif(first == 11):
        third = 'B'
    elif(first == 12):
        third = 'C'
    elif(first == 13):
        third = 'D'
    elif(first == 14):
        third = 'E'
    elif(first == 15):
        third = 'F'
    else:
        third = str(first)
    
    if(second == 10):
        fourth = 'A'
    elif(second == 11):
        fourth = 'B'
    elif(second == 12):
        fourth = 'C'
    elif(second == 13):
        fourth = 'D'
    elif(second == 14):
        fourth = 'E'
    elif(second == 15):
        fourth = 'F'
    else:
        fourth = str(second)
    word = third + fourth
    if(word[0] == '0'):
        return(fourth)
    else:
        return(word)

num = input()
arr = ['0'] * (int(num, 16)+ 1)

while(True):
    order = list(input().split())
    if(order[0] == 'MOVE'):
        if(order[1][0] == '#'):
            N = int(order[1][1:], 16)
            B = int(order[2], 16)
            arr[B] = str(N)
        else:
            A = int(order[1], 16)
            B = int(order[2], 16)
            arr[B] = str(A)

    elif(order[0] == 'ADD'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        arr[B] = str(int(arr[B]) + int(arr[A]))
    elif(order[0] == 'SUB'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        arr[B] = str(int(arr[A]) - int(arr[B]))
    elif(order[0] == 'AND'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        arr[B] = str(int(arr[A]) & int(arr[B]))

    elif(order[0] == 'OR'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        arr[B] = str(int(arr[A]) | int(arr[B]))

    elif(order[0] == 'XOR'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        arr[B] = str(int(arr[A]) ^ int(arr[B]))

    elif(order[0] == 'PRINT'):
        A = int(order[1], 16)
        print(reconvert2(int(arr[A])))
    elif(order[0] == 'PRINTLN'):
        A = int(order[1], 16)
        B = int(order[2], 16)
        brr = list(map(int, arr[A: B + 1]))
        brr = list(map(reconvert2, brr))
        print(' '.join(brr))
    elif(order[0] == 'END'):
        break
