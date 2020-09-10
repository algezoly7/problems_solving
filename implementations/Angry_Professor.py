#for more informations copy this link: https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    counter = 0
    for i in range(n):
        if(a[i] <= 0):
            counter += 1
    if(counter >= k):
        return("NO")
    else:
        return("YES")

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
