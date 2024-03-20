import sys
input = sys.stdin.readline

N = int(input())

num_lst = list(map(int, input().split()))

sum_lst = []

dp = [[0 for _ in range(N)] for _ in range(2)]

dp[0][0] = num_lst[0]
dp[1][0] = num_lst[0]

for i in range(1, N):
    dp[0][i] = max(num_lst[i], dp[0][i-1] + num_lst[i])

for i in range(1, N):
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + num_lst[i])

ans = max(max(dp[0]), max(dp[1]))
print(ans)