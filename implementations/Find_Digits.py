#for more informations copy this link: https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    str_number = str(n)
    length = len(str_number)
    counter = 0
    for i in range(length):
        digit = int(str_number[i])
        if(digit != 0):
            digit_result = n % digit
            if(digit_result == 0):
                counter += 1
    return(counter)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(result)
