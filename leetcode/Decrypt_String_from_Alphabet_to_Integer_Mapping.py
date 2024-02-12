class Solution(object):
    def freqAlphabets(self, s):
        arr = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                arr.append(s[i : i + 2])
                i += 3
            else:
                arr.append(s[i])
                i += 1
        english = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        string = []
        for i in range(len(arr)):
            index_ = int(arr[i]) - 1
            string.append(english[index_])
        return "".join(string)
