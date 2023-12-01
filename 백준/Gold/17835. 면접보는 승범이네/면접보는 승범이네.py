import sys
input = sys.stdin.readline
INF = int(1e12)
import heapq

V, E, K = map(int, input().split())
edge_lst = [[] for _ in range(V+1)]
dist_lst = [INF for _ in range(V+1)]

for _ in range(E):
    s, e, p = map(int, input().split())
    edge_lst[e].append([s, p])
    
arrival_lst = list(map(int, input().split()))

def dijkstra():
    hq = []
    for i in arrival_lst:
        hq.append([0, i])
        dist_lst[i] = 0
    while hq:
        price, now = heapq.heappop(hq)
        if dist_lst[now] < price:
            continue
        for next, next_price in edge_lst[now]:
            if dist_lst[next] > price + next_price:
                dist_lst[next] = price + next_price
                heapq.heappush(hq, [dist_lst[next], next])

ans = -1
max_dist = -1

dijkstra()

for i in range(1, V+1):
    if max_dist < dist_lst[i]:
        ans = i
        max_dist = dist_lst[i]

print(ans)
print(max_dist)