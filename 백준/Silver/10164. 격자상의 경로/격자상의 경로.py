import sys
input = sys.stdin.readline

# 행, 열, 지나야 하는 번호
row, col, K = map(int, input().split())

dp = [[1 for _ in range(col+1)] for _ in range(row+1)]
for r in range(row+1):
    dp[r][0] = 0

for c in range(col+1):
    dp[0][c] = 0
k_row, k_col = (K-1)//col + 1, (K-1)%col + 1

for r in range(1, row+1):
    for c in range(1, col+1):
        dp[r][c] = max(dp[r-1][c] + dp[r][c-1], 1)

if K == 0:
    print(dp[row][col])
else:
    print(dp[k_row][k_col] * dp[row-k_row+1][col-k_col+1])