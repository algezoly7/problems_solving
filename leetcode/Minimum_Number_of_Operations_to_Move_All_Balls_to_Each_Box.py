class Solution(object):
    def minOperations(self, boxes):
        arr = []

        for i in range(len(boxes)):
            if(boxes[i] == "1"):
                arr.append(i)
            elif(boxes[i] == "0"):
                arr.append("NO")

        solution = [0]*len(boxes)

        for i in range(len(boxes)):
            for j in range(len(arr)):
                if(arr[j] != "NO" and i != j):
                    solution[i] += abs(arr[j] - i)

                
        return(solution)
        