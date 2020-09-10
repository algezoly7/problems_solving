#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/days-calculation-1/problem

def days():
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    result = 0
    if(y1 == y2):
        for i in range(m1, m2):
            if(i == 1):
                result += 31
            elif(i == 2):
                if (( y1%400 == 0)or (( y1%4 == 0 ) and ( y1%100 != 0))):
                    result += 29
                else:
                    result += 28
            elif(i == 3):
                result += 31
            elif(i == 4):
                result += 30
            elif(i == 5):
                result += 31
            elif(i == 6):
                result += 30
            elif(i == 7):
                result += 31
            elif(i == 8):
                result += 31
            elif(i == 9):
                result += 30
            elif(i == 10):
                result += 31
            elif(i == 11):
                result += 30
            elif(i == 12):
                result += 31
    else:
        for y in range(y1, y2 + 1):
            if(y == y1):
                for i in range(m1, 13): 
                        if(i == 1):
                            result += 31
                        elif(i == 2):
                            if(( y%400 == 0)or (( y%4 == 0 ) and ( y%100 != 0))):
                                result += 29
                            else:
                                result += 28
                        elif(i == 3):
                            result += 31
                        elif(i == 4):
                            result += 30
                        elif(i == 5):
                            result += 31
                        elif(i == 6):
                            result += 30
                        elif(i == 7):
                            result += 31
                        elif(i == 8):
                            result += 31
                        elif(i == 9):
                            result += 30
                        elif(i == 10):
                            result += 31
                        elif(i == 11):
                            result += 30
                        elif(i == 12):
                            result += 31
            elif(y == y2):
                for i in range(1, m2):
                    if(i == 1):
                            result += 31
                    elif(i == 2):
                        if(( y%400 == 0)or (( y%4 == 0 ) and ( y%100 != 0))):
                            result += 29
                        else:
                            result += 28
                    elif(i == 3):
                        result += 31
                    elif(i == 4):
                        result += 30
                    elif(i == 5):
                        result += 31
                    elif(i == 6):
                        result += 30
                    elif(i == 7):
                        result += 31
                    elif(i == 8):
                        result += 31
                    elif(i == 9):
                        result += 30
                    elif(i == 10):
                        result += 31
                    elif(i == 11):
                        result += 30
                    elif(i == 12):
                        result += 31
            else:
                for i in range(1, 13):
                    if(i == 1):
                            result += 31
                    elif(i == 2):
                        if(( y%400 == 0)or (( y%4 == 0 ) and ( y%100 != 0))):
                            result += 29
                        else:
                            result += 28
                    elif(i == 3):
                        result += 31
                    elif(i == 4):
                        result += 30
                    elif(i == 5):
                        result += 31
                    elif(i == 6):
                        result += 30
                    elif(i == 7):
                        result += 31
                    elif(i == 8):
                        result += 31
                    elif(i == 9):
                        result += 30
                    elif(i == 10):
                        result += 31
                    elif(i == 11):
                        result += 30
                    elif(i == 12):
                        result += 31
    result = result + (d2 - d1)
    return(result)
t = int(input())
for i in range(t):
    print(days())