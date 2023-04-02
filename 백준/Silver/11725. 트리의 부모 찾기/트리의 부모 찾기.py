import sys
input = sys.stdin.readline

N = int(input())

visit = [0] * (N+1)
edge_lst = [[] for _ in range(N+1)]
parents_lst = [0] * (N+1)

def dfs(v):
    stack = [v]
    while stack:
        p = stack.pop()
        visit[p] = 1
        for c in edge_lst[p]:
            if not visit[c]:
                parents_lst[c] = p
                stack.append(c)

for _ in range(N-1):
    a, b = map(int, input().split())
    edge_lst[a].append(b)
    edge_lst[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(parents_lst[i])
