import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 배터리 개수, 장착 최대 개수
battery_lst = list(map(int, input().split()))  # 각 배터리 전력량

dp = [sys.maxsize for _ in range(50001)]
dp[0] = 0
for battery in battery_lst:
    for left in range(50000-battery, -1, -1):
        right = left+battery
        dp[right] = min(dp[right], dp[left]+1)

ans = []
for i in range(len(dp)):
    if 1 <= dp[i] <= K:
        ans.append(i)
print(len(ans))
print(*ans)