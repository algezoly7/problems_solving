import math
def digits_of_the_n_factorial():
        n = int(input())
        if (n < 0): 
            return(0) 
        if (n <= 1): 
            return 1
        else:
            digits = 0
            for i in range(1, n+1):
                digits += math.log10(i)
            return(math.floor(digits) + 1)
T = int(input())
for _ in range(T):
    print(digits_of_the_n_factorial())