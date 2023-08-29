import sys
input = sys.stdin.readline

N = int(input())
lst = [[0 for _ in range(501)] for _ in range(501)]

for _ in range(N):
    A, B = map(int, input().split())
    lst[A][B] = 1

dp = [[0 for _ in range(501)] for _ in range(501)]

for i in range(1, 501):
    for j in range(1, 501):
        if lst[i][j]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(N - dp[-1][-1])