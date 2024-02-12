class Solution(object):
    def longestCommonPrefix(self, strs):
        min_ = 1000000
        for i in strs:
            min_ = min(len(i), min_)
        if min_ == 0:
            return ""
        sample = []
        for i in range(min_):
            character = strs[0][i]
            flag = True
            for j in range(len(strs)):
                if character != strs[j][i]:
                    flag = False
                    break
            if flag == True:
                sample.append(character)
            else:
                break
        return "".join(sample)
