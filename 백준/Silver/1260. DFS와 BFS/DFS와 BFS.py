import sys
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visit1 = [0 for _ in range(N+1)]
visit2 = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

def bfs(v):
    q = deque()
    q.append(v)
    visit1[v]=1
    while q:
        p = q.popleft()
        print(p,end=' ')
        for i in graph[p]:
            if not visit1[i]:
                q.append(i)
                visit1[i]=1

def dfs(v):
    visit2[v]=1
    print(v, end=' ')
    for i in graph[v]:
        if visit2[i]==0:
            dfs(i)

dfs(V)
print()
bfs(V)