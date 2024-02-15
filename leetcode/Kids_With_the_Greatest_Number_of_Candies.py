class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_ = max(candies)
        result = []
        for i in candies:
            if(i + extraCandies >= max_):
                result.append(True)
            else:
                result.append(False)
        return(result)