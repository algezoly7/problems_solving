class Solution(object):
    def findTheWinner(self, n, k):
        position = 0

        arr = [x for x in range(1, n + 1)]

        while(len(arr) > 1):
            position = (position + (k-1)) % len(arr)
            arr.pop(position)
        return(arr[0])