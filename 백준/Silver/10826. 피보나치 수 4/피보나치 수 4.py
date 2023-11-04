import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)];

for i in range(1, N+1):
    if (i == 1):
        dp[i] = 1;
        continue;
    dp[i] = dp[i-2] + dp[i-1];

print(dp[N])