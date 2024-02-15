from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        dictionary = defaultdict(int)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i] == list2[j]):
                    dictionary[list1[i]] = i + j
        dictionary_items = dictionary.items()
        min_ = 1000000000000

        for i in dictionary_items:
            min_ = min(min_, i[1])
        
        arr = []
        for i in dictionary_items:
            if(i[1] == min_):
                arr.append(i[0])
        return(arr)
