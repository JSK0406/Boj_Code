import sys
input = sys.stdin.readline

# 현재 칸에서 할 수 있는 것
# 1. 바로 이전 칸 + 1
# 2. 지름길로 올 수 있었던 이전 칸 + 비용

N, D = map(int, input().split())  # 지름길 개수, 전체 길이

dp = [0 for _ in range(D+1)]

# 도착하는 칸의 인덱스에 시작 칸의 인덱스와 비용 추가
shortcut_lst = [[] for _ in range(D+1)]

for _ in range(N):
    start, end, price = map(int, input().split())
    if start > D or end > D:
        continue
    shortcut_lst[end].append((start, price))

for end in range(1, D+1):
    dp[end] = dp[end-1] + 1  # 일단 전 칸 고려해서 설정
    if shortcut_lst[end]:
        for start, price in shortcut_lst[end]:
            dp[end] = min(dp[end], dp[start] + price)

print(dp[-1])