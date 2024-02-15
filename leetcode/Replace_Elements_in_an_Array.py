class Solution(object):
    def arrayChange(self, nums, operations):
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i

        for i in range(len(operations)):
            dictionary[operations[i][1]] = dictionary[operations[i][0]]
            dictionary.pop(operations[i][0])
        dictionary = sorted(dictionary.items(), key=lambda item: item[1])
        arr = []
        for i in dictionary:
            arr.append(i[0])
        return(arr)