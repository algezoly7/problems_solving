#for more informations copy this link: https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    if(p<=n):
        return min(p//2, n//2 - p//2)

if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
