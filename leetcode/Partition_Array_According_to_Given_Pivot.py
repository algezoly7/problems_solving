class Solution(object):
    def pivotArray(self, nums, pivot):
        lessThan = []
        moreThan = []
        equal = []
        for i in nums:
            if(i < pivot):
                lessThan.append(i)

            elif(i == pivot):
                equal.append(i)
                
            elif(i > pivot):
                moreThan.append(i)

        arr = []

        for i in lessThan:
            arr.append(i)

        for i in equal:
            arr.append(i)

        for i in moreThan:
            arr.append(i)

        return(arr)
        