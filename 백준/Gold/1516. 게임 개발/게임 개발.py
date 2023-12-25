import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

time_lst = [0 for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
edge_lst = [[] for _ in range(N+1)]


for i in range(1, N+1):
    tmp_lst = list(map(int, input().split()))
    time_lst[i] = tmp_lst[0]
    for j in tmp_lst[1:]:
        if j == -1:
            break
        in_degree[i] += 1
        edge_lst[j].append(i)

q = deque()

ans_lst = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)
        ans_lst[i] = time_lst[i]

while q:
    now = q.popleft()

    for next in edge_lst[now]:
        in_degree[next] -= 1
        ans_lst[next] = max(ans_lst[next], ans_lst[now] + time_lst[next])
        if in_degree[next] == 0:
            q.append(next)

for i in ans_lst[1:]:
    print(i)