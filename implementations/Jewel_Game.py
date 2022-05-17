#for more informations copy this link: https://www.hackerrank.com/contests/hack-the-interview-v-asia-pacific/challenges/candy-crush-4/copy-from/1324509784
#Source: HackerRank/Hack the interview V(Asia Pacific)
def Jewel_Game():
    word = input()
    n = len(word)
    arr = []
    for i in range(n):
        arr.append(word[i])
    i = 1
    counter = 0
    while(i < n):
        if(arr[i] == arr[i - 1]):
            counter += 1
            arr.pop(i)
            arr.pop(i - 1)
            i -= 1
            #it's for test cases like this abba
            n = len(arr)
            #because the length of arr changes
        else:
            i += 1
    return(counter)
T = int(input())
for _ in range(T):
    print(Jewel_Game())