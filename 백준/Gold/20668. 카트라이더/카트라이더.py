import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())  # 정점 개수, 간선 개수
edge_lst = [[] for _ in range(N+1)]  # 도착지, 길이, 속도 제한

ten_fac = 3_628_800

for _ in range(M):
    A, B, L, K = map(int, input().split())
    edge_lst[A].append((B, L*ten_fac, K))
    edge_lst[B].append((A, L*ten_fac, K))

hq = []  # 지금까지의 시간, 지금 정점, 지금 속도, 이전 노드
heapq.heappush(hq, (0, 1, 1))

delete_set = set()

# 속도 별 최단 시간
time_lst = [[sys.maxsize for _ in range(N+1)] for _ in range(11)]
time_lst[1][1] = 0

# 속도가 더 느린 경우에 더 짧은 게 있다면 추가 안함

while hq:
    now_time, now_node, now_speed = heapq.heappop(hq)
    if time_lst[now_speed][now_node] < now_time:
        continue
    for next_node, length, speed_limit in edge_lst[now_node]:
        # 속도 +1
        if 1 <= now_speed+1 <= speed_limit:
            if time_lst[now_speed+1][next_node] > now_time + length // (now_speed + 1):
                time_lst[now_speed+1][next_node] = now_time + length // (now_speed + 1)
                heapq.heappush(hq, (time_lst[now_speed+1][next_node], next_node, now_speed + 1))
        # 속도 일정
        if 1 <= now_speed <= speed_limit:
            if time_lst[now_speed][next_node] > now_time + length // (now_speed):
                time_lst[now_speed][next_node] = now_time + length // (now_speed)
                heapq.heappush(hq, (time_lst[now_speed][next_node], next_node, now_speed))
        # 속도 -1
        if 1 <= now_speed-1 <= speed_limit:
            if time_lst[now_speed-1][next_node] > now_time + length // (now_speed - 1):
                time_lst[now_speed-1][next_node] = now_time + length // (now_speed - 1)
                heapq.heappush(hq, (time_lst[now_speed-1][next_node], next_node, now_speed - 1))

ans = sys.maxsize
for i in range(1, 11):
    ans = min(ans, time_lst[i][N])

x = ans
print(x // 3628800, end='')
x %= 3628800
y = x / 3628800
print(f"{y:.9f}"[1:])