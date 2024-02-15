class Solution(object):
    def rearrangeArray(self, nums):
        positives = []
        negatives = []

        for i in nums:
            if(i >= 0):
                positives.append(i)
            elif(i < 0):
                negatives.append(i)

        arr = []
        for i in range(len(positives)):
            arr.append(positives[i])
            arr.append(negatives[i])
        return(arr)