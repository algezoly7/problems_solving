from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):

        dictionary = defaultdict(list)

        for i in range(len(nums)):
            dictionary[nums[i]].append(i)
                
        nums.sort()

        i = 0
        j = len(nums) - 1
        while(True):
            if(nums[i] + nums[j] == target):
                if(nums[i] == nums[j]):
                    return([ dictionary[nums[i]][0], dictionary[nums[j]][1] ])
                    break
                else:
                    return([ dictionary[nums[i]][0], dictionary[nums[j]][0] ])
                    break
            elif(nums[i] + nums[j] > target):
                j -= 1
            elif(nums[i] + nums[j] < target):
                i += 1