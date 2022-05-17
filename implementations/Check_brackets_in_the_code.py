#Source: coursera
#a code for checking brackets
#if it's isn't balanced it will return the index of the issue
#otherwise it will return Success
def Check_brackets_in_the_code():
    string = input()
    n = len(string)
    opening = ['(', '{', '[']
    ending  = [')', '}', ']']
    arr = []
    brr = []
    #for problems like this [[(()
    for i in range(n):
        if string[i] in opening:
            arr.append(string[i])
            brr.append(i)
        elif string[i] in ending:
            index = ending.index(string[i])
            if len(arr) > 0 and opening[index] == arr[-1]:
                arr.pop()
                brr.pop()
            else:
                return(i + 1)
    if len(arr) != 0:
        return(brr[-1] + 1)
        #for problems like this [[(()
    else:
        return('Success')
print(Check_brackets_in_the_code())