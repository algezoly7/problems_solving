#you are given a list of children with different ages ,your task is to group
#them considering the max difference between the ages of any two children in
#the list.
#source: coursera
def num_of_groubs(arr, max_difference):
    arr.sort()
    i = 0
    last = len(arr) - 1
    ans = []
    while(i <= last):
        sub_ans = []
        j = i
        i += 1
        sub_ans.append(arr[j])
        while(i <= last and arr[i] - arr[j] <= max_difference):
            sub_ans.append(arr[i])
            i = i+1
        ans.append(sub_ans)
    return(ans)
arr = list(map(int, input("ages: ").split()))
max_difference = int(input("max_difference: "))
print(num_of_groubs(arr, max_difference))
