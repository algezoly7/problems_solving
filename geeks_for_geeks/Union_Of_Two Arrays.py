#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        arr = a + b
        the_set = set(arr)
        return(len(the_set))