import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, end):
    dist_lst[start] = 0
    visited_lst[start] = True
    hq = [[0, start]]
    while hq:
        p, now = heapq.heappop(hq)
        dist_now = dist_lst[now]
        visited_lst[now] = True
        for next in range(1, V+1):
            if edge_lst[now][next] >= 0 and not visited_lst[next] and dist_lst[next] > dist_now + edge_lst[now][next]:
                dist_lst[next] = dist_now + edge_lst[now][next]
                visited_city_lst[next] = visited_city_lst[now] + [now]
                heapq.heappush(hq, [dist_lst[next], next])

V = int(input())
E = int(input())
edge_lst = [[-1 for _ in range(V+1)] for _ in range(V+1)]
visited_lst = [False for _ in range(V+1)]
visited_city_lst = [[] for _ in range(V+1)]
dist_lst = [INF for _ in range(V+1)]

for _ in range(E):
    s, e, price = map(int, input().split())
    if edge_lst[s][e] == -1 or edge_lst[s][e] > price:
        edge_lst[s][e] = price

start, end = map(int, input().split())
dijkstra(start, end)

print(dist_lst[end])
final_city_lst = visited_city_lst[end] + [end]
print(len(final_city_lst))
print(*final_city_lst)