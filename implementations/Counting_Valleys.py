#for more informations copy this link: https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(n, s):
    Gary_level = 0
    counter = 0
    for i in range(n):
        if(s[i] == "U"):
            Gary_level += 1
            if(Gary_level == 0):
                counter += 1
        else:
            Gary_level -= 1
    return(counter)

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
