class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        flag = False
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                flag = True
        return(flag)