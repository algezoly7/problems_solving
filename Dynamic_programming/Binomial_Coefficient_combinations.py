#for more copy this link: https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
#Source: GeeksForGeeks

def combinations(n, k):
    fac = [0] * (n + 1)
    fac[0] = 1
    for i in range(1, n+1):
        fac[i] = i * fac[i - 1]
    return(fac[n] / (fac[n - k] * fac[k]))
print(round(combinations(5, 2)))