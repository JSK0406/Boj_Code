import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 물품 수, 최대 무게

weight_value_lst = [list(map(int, input().split())) for _ in range(N)]
weight_value_lst.insert(0, [0, 0])
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for cnt in range(1, N+1):
    now_weight, now_value = weight_value_lst[cnt][0], weight_value_lst[cnt][1]
    if 1 >= now_weight:
        dp[cnt][1] = max(now_value, dp[cnt-1][1])
    else:
        dp[cnt][1] = dp[cnt-1][1]
    for weight in range(2, K+1):
        if weight >= now_weight:
            dp[cnt][weight] = max(dp[cnt-1][weight], now_value + dp[cnt-1][weight-now_weight])
        else:
            dp[cnt][weight] = max(dp[cnt-1][weight], dp[cnt][weight-1])

print(dp[-1][-1])