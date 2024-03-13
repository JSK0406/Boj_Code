import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 회원 수

edge_lst = [[] for _ in range(N+1)]

while True:
    A, B = map(int, input().split())
    if A == -1 and B == -1:
        break
    edge_lst[A].append(B)
    edge_lst[B].append(A)

def bfs(start):
    visited_lst = [-1 for  _ in range(N+1)]
    visited_lst[0] = 0
    visited_lst[start] = 0
    
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        next_score = visited_lst[now] + 1
        for next in edge_lst[now]:
            if visited_lst[next] == -1:
                visited_lst[next] = next_score
                q.append(next)
    
    return max(visited_lst)

min_score = sys.maxsize
pre_lst = []

for start in range(1, N+1):
    now_score = bfs(start)
    if min_score < now_score:
        pass
    elif min_score == now_score:
        pre_lst.append(start)
    else:
        min_score = now_score
        pre_lst = [start]

print(min_score, len(pre_lst))
print(*pre_lst)