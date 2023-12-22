import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N, M = map(int, input().split())
edge_lst = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge_lst[B].append((A, C))
    edge_lst[A].append((B, C))
    
def dijkstra(start):
    dist_lst = [INF for _ in range(N+1)]
    linked_lst = [0 for _ in range(N+1)]

    hq = [(0, start)]
    dist_lst[start] = 0

    while hq:
        now_dist, now = heapq.heappop(hq)
        for next, price in edge_lst[now]:
            if dist_lst[next] > now_dist + price:
                dist_lst[next] = now_dist + price
                heapq.heappush(hq, (dist_lst[next], next))
                linked_lst[next] = now
    return linked_lst

ans_lst = dijkstra(1)

print(N-1)
for idx in range(2, N+1):
    print(idx, ans_lst[idx])
