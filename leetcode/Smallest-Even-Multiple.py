class Solution(object):
    def smallestEvenMultiple(self, n):
        i = n
        while(True):
            if(i % 2 == 0 and i % n == 0):
                return(i)
            i += 1
