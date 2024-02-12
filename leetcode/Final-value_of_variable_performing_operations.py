class Solution(object):
    def finalValueAfterOperations(self, operations):
        value = 0
        for i in operations:
            if i == "++X" or i == "X++":
                value += 1
            else:
                value -= 1
        return value
