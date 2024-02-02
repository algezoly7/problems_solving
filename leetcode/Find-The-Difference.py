class Solution(object):
    def findTheDifference(self, s, t):
        for i in range(len(t)):
            if(t[i] not in s or t.count(t[i]) != s.count(t[i])):
                return(t[i])
                break
