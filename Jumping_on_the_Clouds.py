#for more informations copy this link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    end = n - 1
    current_cloud = 0
    jumps = 0
    while(current_cloud < end):
        if((current_cloud + 2 <= end) and (c[current_cloud + 2] == 0)):
            current_cloud += 2
            jumps += 1
        elif(c[current_cloud + 1] == 0):
            current_cloud += 1
            jumps += 1
    return(jumps)

if __name__ == '__main__':
 
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)