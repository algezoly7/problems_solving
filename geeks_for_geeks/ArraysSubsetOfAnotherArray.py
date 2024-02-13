#User function Template for python3

def isSubset( a1, a2, n, m):
    for i in a2:
        if(i not in a1):
            return("No")
        a1.remove(i)
    return("Yes")