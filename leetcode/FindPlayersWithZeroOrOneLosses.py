class Solution(object):
    def findWinners(self, matches):
        losses = {}

        for i in range(len(matches)):
            losses[matches[i][0]] = 0
            losses[matches[i][1]] = 0

        for i in range(len(matches)):
            losses[matches[i][1]] += 1

        answers = [[], []]
        for i in losses.items():
            if(i[1] == 0):
                answers[0].append(i[0])
            elif(i[1] == 1):
                answers[1].append(i[0])
        answers[0].sort()
        answers[1].sort()
        return(answers)
                