import sys
import heapq

def func(start, end, edge):
    shortest = [9999999]*(N+1)
    visit = [0] * (N+1)
    cur = start
    shortest[start] = 0
    hq = []
    while sum(visit) < N and cur != end:
        visit[cur] = 1
        for next in range(1, N+1):
            if edge[cur][next]!=0:
                tmp = shortest[cur] + edge[cur][next]
                if shortest[next] < tmp:
                    continue
                else:
                    shortest[next] = shortest[cur] + edge[cur][next]
                    if visit[next] == 0:
                        heapq.heappush(hq, (shortest[next], next))
        cur = heapq.heappop(hq)[1]
    return shortest[end]

N, M, X = map(int, sys.stdin.readline().split())
edge = [[0 for _ in range(N+1)] for _ in range(N)]
edge.insert(0, 0)
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    edge[start][end] = cost

result = 0
for i in range(1, N+1):
    if i==X:
        continue
    result = max(result, func(i, X, edge) + func(X, i, edge))
print(result)