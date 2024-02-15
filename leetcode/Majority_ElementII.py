from collections import defaultdict
nums = [1, 2]
num_times = len(nums)//3
dictionary = defaultdict(int)

for i in range(len(nums)):
    dictionary[nums[i]] += 1

arr = []
for i in dictionary.items():
    if(i[1] > num_times):
        arr.append(i[0])
print(arr)