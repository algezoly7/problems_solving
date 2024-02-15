class Solution(object):
    def checkPossibility(self, nums):
        flag = False
        for i in range(len(nums)-1):
            if(nums[i] <= nums[i+1]):
                continue

            elif(flag == True):
                return(False)

            elif(i==0 or nums[i + 1] >= nums[i - 1]):
                flag = True
                nums[i] = nums[i+1]

            else:
                flag = True
                nums[i + 1] = nums[i]
        return(True)