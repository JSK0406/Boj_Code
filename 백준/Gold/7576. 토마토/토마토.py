# from collections import deque

# M, N = map(int, input().split())
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input().split())))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# #first

# q_plus1 = deque()
# q_minus1 = deque()

# for x in range(N):
#     for y in range(M):
#         if graph[x][y]==1:
#             q_plus1.append((x,y))
#         elif graph[x][y]==-1:
#             q_minus1.append((x,y))

# while q_plus1:
#     x,y = q_plus1.popleft()
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
#             q_plus1.append((nx,ny))
#             graph[nx][ny]=graph[x][y]+1

# answer = graph[x][y]

# for test in q_minus1:
#     x,y = test
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
#             if graph[nx][ny]==0:
#                 answer=0
#     if answer==0:
#         break

# print(answer-1)

import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0

q = deque()

for i in range(n):
    for j in range(m):
        if map_lst[i][j] == 1:
            q.append((i, j))

def bfs(col, row):
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not map_lst[nx][ny]:
                map_lst[nx][ny] = map_lst[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if map_lst[i][j] == 1:
            bfs(i, j)

Flag = True

for row in map_lst:
    for node in row:
        if node == 0:
            answer = 0
            Flag = False
            break
    if not Flag:
        break
    else:
        answer = max(answer, max(row))
print(answer-1)