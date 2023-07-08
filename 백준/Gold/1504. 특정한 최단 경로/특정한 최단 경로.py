import sys
import heapq
input = sys.stdin.readline
INF = 999_999_999

N, E = map(int, input().split())  # 정점 개수, 간선 개수

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())  # 출발, 도착, 거리
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (start, 0))
    shortest = [INF] * (N + 1)
    shortest[start] = 0

    while hq:
        now, now_dist = heapq.heappop(hq)
        if shortest[now] < now_dist:
            continue
        for next, next_dist in graph[now]:
            cost = now_dist + next_dist
            if cost < shortest[next]:
                shortest[next] = cost
                heapq.heappush(hq, (next, cost))
    return shortest

v1, v2 = map(int, input().split())  # 들러야 하는 2개의 노드
v1_v2 = dijkstra(v1)[v2]

ans1 = dijkstra(1)[v1] + v1_v2 + dijkstra(v2)[N]
ans2 = dijkstra(1)[v2] + v1_v2 + dijkstra(v1)[N]
ans = min(ans1, ans2)

if ans < INF:
    print(ans)
else:
    print(-1)