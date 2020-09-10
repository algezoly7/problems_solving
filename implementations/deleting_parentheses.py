#for more informations copy this link: https://www.hackerrank.com/contests/easyhack2/challenges/deleting-parentheses


arr = [0, 0]
word = input()
n = len(word)
counter = 0
brr = 0
for i in range(n):
    if(word[i] == '('):
        brr += 1
    else:
        if(brr > 0):
            brr -= 1
        else:
            counter += 1
print(counter + brr)