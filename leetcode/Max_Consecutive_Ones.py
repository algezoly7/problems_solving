class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        sum_1 = 0
        sum_2 = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                sum_1 += 1
            elif(nums[i] == 0):
                sum_2 = max(sum_1, sum_2)
                sum_1 = 0 
        return(sum_2)
