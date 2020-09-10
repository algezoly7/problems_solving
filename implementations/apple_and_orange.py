#for more informations visit https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appels_in_the_house = 0

    for i in range(len(apples)):

        appel_location = apples[i] + a

        if appel_location in range(s, t+1):

            appels_in_the_house  = appels_in_the_house + 1

    print(appels_in_the_house)

    oranges_in_the_house = 0

    for i in range(len(oranges)):

        oranges_location = oranges[i] + b

        if oranges_location in range(s, t+1):

            oranges_in_the_house  = oranges_in_the_house + 1

    print(oranges_in_the_house)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
