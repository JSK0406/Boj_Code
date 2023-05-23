# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000000)

# N, M = map(int, input().split())  # row, col
# init_row, init_col, direction = map(int, input().split())

# # 0 : 북 1: 동 2:남 3:서
# dc = [0, 1, 0, -1]
# dr = [-1, 0, 1, 0]

# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))

# cnt = 0
# def dfs(row, col, graph, direction):
#     global cnt
#     if not 0 <= row < N or not 0 <= col < M:
#         exit
#     if not graph[row][col]:
#         graph[row][col] = 1
#         cnt += 1
#     for _ in range(4):
#         direction -= 1
#         if direction == -1:
#             direction = 3
#         next_col = col + dc[direction]
#         next_row = row + dr[direction]
#         if 0 <= next_row < N and 0 <= next_col < M and not graph[next_row][next_col]:
#             dfs(next_row, next_col, graph, direction)
#     else:
#         dfs(row - dr[direction], col - dc[direction], graph, direction)
#     return

# dfs(init_row, init_col, graph, direction)
# print(cnt)
# print(graph)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # row, col
row, col, direction = map(int, input().split())

# 0 : 북 1: 동 2:남 3:서
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cnt = 0

while True:
    if graph[row][col] == 1:
        break
    if not graph[row][col]:
        graph[row][col] = 2
        cnt += 1
    for _ in range(4):
        direction -= 1
        if direction == -1:
            direction = 3
        next_col = col + dc[direction]
        next_row = row + dr[direction]
        if 0 <= next_row < N and 0 <= next_col < M and not graph[next_row][next_col]:
            col = next_col
            row = next_row
            break
    else:
        row -= dr[direction]
        col -= dc[direction]

print(cnt)