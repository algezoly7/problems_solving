# for more informations copy this link : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    i = (0 + k) % n
    energy -= 1
    if(c[i] == 1):
        energy -= 2
    while(i != 0):
        i = (i + k) % n
        energy -= 1
        if(c[i] == 1):
            energy -= 2
    return(energy)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)