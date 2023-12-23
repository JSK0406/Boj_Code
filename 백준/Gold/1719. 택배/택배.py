import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N, M = map(int, input().split())
edge_lst = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge_lst[A].append((B, C))
    edge_lst[B].append((A, C))

parent_lst = [[0 for _ in range(N+1)] for _ in range(N+1)]

def dijkstra(start):
    global parent_lst
    dist_lst = [INF for _ in range(N+1)]

    hq = [(0, start)]
    parent_lst[start][start] = '-'
    dist_lst[start] = 0

    while hq:
        now_dist, now = heapq.heappop(hq)
        for next, next_price in edge_lst[now]:
            if dist_lst[next] > now_dist + next_price:
                dist_lst[next] = now_dist + next_price
                if start == now:
                    parent_lst[start][next] = next
                else:
                    parent_lst[start][next] = parent_lst[start][now]
                heapq.heappush(hq, (dist_lst[next], next))

for i in range(1, N+1):
    dijkstra(i)

for i in range(1, N+1):
    for j in range(1, N+1):
        print(parent_lst[i][j], end=' ')
    print('')