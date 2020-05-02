#for more informations copy this link: https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    height = 1
    for i in range(n):
        if(i % 2 == 0):
            height = height * 2
        else:
            height += 1
    return(height)
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)