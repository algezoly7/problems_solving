#for more informations copy this link: https://www.hackerrank.com/challenges/strange-advertising/problem

import math

def viralAdvertising(n):
    recipients = 5
    likes = 0

    for _ in range(n):
        new_likes = math.floor(recipients / 2)
        likes += new_likes
        recipients = math.floor(recipients / 2) * 3
    return(likes)
    
if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

    print(result)