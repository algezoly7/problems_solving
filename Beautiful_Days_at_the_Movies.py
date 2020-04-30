#for more informations copy this link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):
    counter = 0
    for num in range(i , j + 1):
        reversed_num = str(num)[::-1]
        difference = int(reversed_num) - num
        if(difference % k == 0):
            counter += 1
    return(counter)

if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
