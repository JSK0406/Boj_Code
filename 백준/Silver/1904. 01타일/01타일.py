import sys
input = sys.stdin.readline

N = int(input())

# N = 1 => 1
# N = 2 => 11, 00
# N = 3 => 100 / 111, 001
# N = 4 => 1100,0000 / 1001, 1111, 0011

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2

if N <= 2:
    print(dp[N] % 15746)
else:
    for i in range(3, N+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
    print(dp[N])