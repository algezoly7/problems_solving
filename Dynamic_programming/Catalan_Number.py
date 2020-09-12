#for more informations copy this link: https://www.geeksforgeeks.org/program-nth-catalan-number/
# A dynamic programming based function to find nth 
# Catalan number
#Source: GeeksForGeeks

def catalan(n): 
    if (n == 0 or n == 1): 
        return 1
  
    # Table to store results of subproblems 
    catalan = [0 for i in range(n + 1)] 
  
    # Initialize first two values in table 
    catalan[0] = 1
    catalan[1] = 1
  
    # Fill entries in catalan[] using recursive formula 
    for i in range(2, n + 1): 
        for j in range(i + 1): 
            catalan[i] = catalan[i] + catalan[j - 1] * catalan[i-j] 
  
    # Return last entry 
    return catalan[n] 
  
n = int(input())
print (catalan(n)) 