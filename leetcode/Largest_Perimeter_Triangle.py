class Solution(object):
    def largestPerimeter(self, nums):
        n = len(nums)
        nums.sort(reverse = True)
        maxi = 0

        for i in range(0, n - 2):
            if nums[i] < (nums[i + 1] + nums[i + 2]):
                maxi = max(maxi, nums[i] + nums[i + 1] + nums[i + 2])
                break
        
        return(maxi)
        