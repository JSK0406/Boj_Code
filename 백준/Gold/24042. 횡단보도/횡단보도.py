import sys
input = sys.stdin.readline
import heapq

# 1번부터 N번까지 최단 시간

N, M = map(int, input().split())  # 지역 수, 횡단보도 주기

sign_lst = [[] for _ in range(N+1)]  # 다음, 주기에서의 순서

for i in range(M):
    A, B = map(int, input().split())
    sign_lst[A].append((B, i))
    sign_lst[B].append((A, i))

dist_lst = [sys.maxsize for _ in range(N+1)]

hq = []  # 지금까지의 시간, 현재 좌표, 이전 신호의 주기 순서(-1은 초기)
heapq.heappush(hq, (0, 1, -1))
dist_lst[1] = 0

while hq:
    now_time, now_node, now_order = heapq.heappop(hq)
    # 초기 세팅
    if now_order == -1:
        for next_node, next_order in sign_lst[now_node]:
            if dist_lst[next_node] > next_order + 1:
                dist_lst[next_node] = next_order + 1
                heapq.heappush(hq, (next_order+1, next_node, next_order))
        continue
    
    # 통과 조건
    if now_time > dist_lst[now_node]:
        continue

    for next_node, next_order in sign_lst[now_node]:
        # 주기 내 다음 순서
        if now_order < next_order:
            next_time = now_time + next_order - now_order
            if next_time < dist_lst[next_node]:
                dist_lst[next_node] = next_time
                heapq.heappush(hq, (next_time, next_node, next_order))
        # 다음 주기 순서
        if now_order > next_order:
            next_time = M + now_time - (now_order - next_order)
            if next_time < dist_lst[next_node]:
                dist_lst[next_node] = next_time
                heapq.heappush(hq, (next_time, next_node, next_order))

print(dist_lst[N])