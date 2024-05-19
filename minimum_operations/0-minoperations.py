#!usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0
    
    dp = [0] * (n + 1)

   # use  maximum possible operations
    for i in range(2, n + 1):
        dp[i] = i 
        for j in range(1, i):
            if i % j == 0: # check if j is a divisor of i
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]
