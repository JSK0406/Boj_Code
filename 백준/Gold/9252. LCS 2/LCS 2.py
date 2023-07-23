import sys
input = sys.stdin.readline

col_lst = [""] + list(input().strip())
row_lst = [""] + list(input().strip())

dp = [[0 for _ in range(len(col_lst))] for _ in range(len(row_lst))]

for row in range(1, len(row_lst)):
    for col in range(1, len(col_lst)):
        if row_lst[row] == col_lst[col]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[-1][-1]) 

row = len(row_lst) - 1
col = len(col_lst) - 1

ans = []

row = len(row_lst) - 1
col = len(col_lst) - 1

while col and row:
    if dp[row][col] == dp[row - 1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col - 1]:
        col -= 1
    else:
        ans.append(col_lst[col])
        row -= 1
        col -= 1

for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end='')