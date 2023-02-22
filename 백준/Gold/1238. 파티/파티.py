import sys
import heapq

def dijkstra(start, end):
    shortest = [999_999_999] * (N+1)
    shortest[start] = 0
    hq = [(shortest[start], start)]
    while hq:
        cur = heapq.heappop(hq)[1]
        if cur == end:
            break
        for i in edge[cur]:
            tmp = shortest[cur] + i[0]
            if shortest[i[1]] > tmp:
                shortest[i[1]] = tmp
                heapq.heappush(hq, (shortest[i[1]], i[1]))
    return shortest[end]

N, M, X = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    edge[start].append((cost, end))

result = 0
for i in range(1, N+1):
    if i==X:
        continue
    result = max(result, dijkstra(i, X) + dijkstra(X, i))
print(result)