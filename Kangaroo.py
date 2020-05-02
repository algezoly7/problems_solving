#for more informations visit https://www.hackerrank.com/challenges/kangaroo/problem.

def kangaroo(x1, v1, x2, v2):
    if(v2 > v1):
        the_result = "NO"

        return(the_result)

    else:
        the_result = "NO"
        
        for _ in range(10000):
            x2 = x2 + v2

            x1 = x1 + v1

            if(x1 == x2):
                the_result = "YES"

        return(the_result)

if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)