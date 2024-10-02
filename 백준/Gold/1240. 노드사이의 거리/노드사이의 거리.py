import sys
from collections import deque

N, M = map(int, input().split())  # 노드 개수, 거리 알고 싶은 노드 쌍 개수
edge_lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B, D = map(int, input().split())
    edge_lst[A].append((B, D))
    edge_lst[B].append((A, D))

def bfs(a, b):
    q = deque()
    q.append(a)
    visited_lst = [0 for _ in range(N+1)]
    visited_lst[a] = 1

    while q:
        now_num = q.popleft()
        tot_dis = visited_lst[now_num]
        for next_num, next_dis in edge_lst[now_num]:
            if visited_lst[next_num] > 0:
                continue
            if next_num == b:
                return tot_dis + next_dis - 1
            visited_lst[next_num] = tot_dis + next_dis
            q.append(next_num)

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))