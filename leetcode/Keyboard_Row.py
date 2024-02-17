class Solution(object):
    def findWords(self, words):

        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        arr = []
        for i in words:

            row = 0
            flag = True

            for j in range(len(i)):
                if(j == 0):
                    if(i[j].lower() in row1):
                        row = 1
                    elif(i[j].lower() in row2):
                        row = 2
                    elif(i[j].lower() in row3):
                        row = 3

                elif(row == 1 and i[j].lower() not in row1):
                    flag = False
                    break
                elif(row == 2 and i[j].lower() not in row2):
                    flag = False
                    break
                elif(row == 3 and i[j].lower() not in row3):
                    flag = False
                    break
            if(flag == True):
                arr.append(i)
        return(arr)