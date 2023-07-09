import sys
input = sys.stdin.readline

N = int(input())  # 3 * N

dp = [0] * 31

dp[1] = 0
dp[2] = 3
dp[3] = 0

# N = 4 => d[2] * 3 + 2
# N = 6 => d[4] * 3 + d[2] * 2 + 2
# N = 8 => d[6] * 3 + d[4] * 2 + d[2] * 2 + 2


if N >= 4:
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
print(dp[N])
