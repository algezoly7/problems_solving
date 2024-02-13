class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        wordA = ""
        for i in word1:
            wordA += i
        
        wordB = ""
        for i in word2:
            wordB += i
            
        return(wordA == wordB)
        