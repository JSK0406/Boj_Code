import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())  # 정점 개수, 간선 개수
edge_lst = [[] for _ in range(N+1)]  # 다음 정점, 비용

for _ in range(M):
    a, b, c = map(int, input().split())
    edge_lst[a].append((b, c))
    edge_lst[b].append((a, c))

S, E = map(int, input().split())

dist_lst = [sys.maxsize for _ in range(N+1)]

hq = []
dist_lst[S] = 0
heapq.heappush(hq, (S, dist_lst[S]))
while hq:
    now_node, until_price = heapq.heappop(hq)
    if dist_lst[now_node] < until_price:
        continue
    for next_node, next_price in edge_lst[now_node]:
        if until_price + next_price < dist_lst[next_node]:
            dist_lst[next_node] = until_price + next_price
            heapq.heappush(hq, (next_node, dist_lst[next_node]))

print(dist_lst[E])