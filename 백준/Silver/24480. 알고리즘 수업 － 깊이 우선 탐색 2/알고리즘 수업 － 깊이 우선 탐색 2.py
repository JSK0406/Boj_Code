import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]
graph.insert(0, [])
visit = [0]*(N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort(reverse=True)

answer = [0] * (N+1)
check = 1
def dfs(v):
    global check
    visit[v] = 1
    answer[v] = check
    check += 1
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
    return
dfs(R)

for i in answer[1:]:
    print(i)