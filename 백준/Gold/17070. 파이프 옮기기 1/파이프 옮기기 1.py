import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
map_lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# 가로, 세로, 대각선
dp[0][1][0] = 1
for r in range(N):
    for c in range(N):
        if 0 <= c+1 < N and not map_lst[r][c+1]:
            dp[r][c+1][0] += dp[r][c][0] + dp[r][c][2]
        if 0 <= r+1 < N and not map_lst[r+1][c]:
            dp[r+1][c][1] += dp[r][c][1] + dp[r][c][2]
        if 0 <= r+1 < N and 0 <= c+1 < N:
            if not map_lst[r+1][c] and not map_lst[r][c+1] and not map_lst[r+1][c+1]:
                dp[r+1][c+1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]

print(sum(dp[-1][-1]))