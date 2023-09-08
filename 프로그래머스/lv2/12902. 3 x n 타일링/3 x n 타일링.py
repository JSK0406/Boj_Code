def solution(n):
    
    dp = [0]*(5001)
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11
    if n >= 5:
        for i in range(5, n+1):
            if i % 2 == 1:
                dp[i] = 0
            else:
                dp[i] = (dp[i-2] * 3 + sum(dp[1:i-3]) * 2 + 2) % 1_000_000_007 
     
    answer = dp[n]
    
    return answer