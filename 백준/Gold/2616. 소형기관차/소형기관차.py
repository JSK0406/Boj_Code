import sys
input = sys.stdin.readline

# 소형 기관차 3대 => 최대로 끌 수 있는 객차 수 같다
# 최대한 많은 손님
# 번호가 연속적으로 이어진 객차

N = int(input())  # 객차 수
num_lst = list(map(int, input().split()))
T = int(input())  # 소형 기관차가 끌 수 있는 수

sum_lst = []  # 객차 첫번째 기준

now_sum = sum(num_lst[:T])
sum_lst.append(now_sum)

for i in range(T, N):
    now_sum += num_lst[i]
    now_sum -= num_lst[i-T]
    sum_lst.append(now_sum)

# sum_lst에서 T라는 간격을 두고 3개 고르기

dp = [[0, 0, 0] for _ in range(N-T+1)]  # 지금까지 1개 고름, 지금까지 2개 고름, 지금까지 3개 고름

for i in range(N-T+1):
    left_idx = i-T
    if left_idx < 0:
        dp[i][0] = sum_lst[i]
        continue
    dp[i][0] = max(dp[i-1][0], sum_lst[i])
    dp[i][1] = max(dp[i-1][1], dp[left_idx][0] + sum_lst[i])
    dp[i][2] = max(dp[i-1][2], dp[left_idx][1] + sum_lst[i])


print(dp[-1][-1])