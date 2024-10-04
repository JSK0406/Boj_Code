import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 총 시간, 최대 지침 지수
dis_lst = [int(input()) for _ in range(N)]

# 달리기가 끝나면 지침지수가 0이 되어야 함
# 학생들이 쉬기 시작하면 지침지수가 0이 될 때까지 쉬어야 함

# 이번에 쉰다 => 남은 지침 지수만큼 쉬어야 함
# 이번에 안 쉰다 => 이전에 남은 지침 지수 -= 1

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]  # dp[지침 지수] = 해당 지침 지수에서의 최대 시간

for i in range(N):
    for j in range(M+1):
        # 이번에 쉰다
        if i + j <= N:
            dp[i+j][0] = max(dp[i+j][0], dp[i][j], dp[i][0])
            
        # 이번에 안 쉰다
        if i+1 <= N and j+1 <= M:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + dis_lst[i])

print(dp[-1][0])