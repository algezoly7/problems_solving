class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i == j):
                    continue
                else:
                    if(nums[i] == nums[j] and i < j):
                        counter += 1
        return(counter)
