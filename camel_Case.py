#for more informations copy this link: https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    counter = 1
    for i in range(0,len(s)):
        if(s[i] in "QWERTYUIOPASDFGHJKLZXCVBNM"):
            counter += 1
            
    return(counter)

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(result)
