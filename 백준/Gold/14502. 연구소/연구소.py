import sys
import copy
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())  # row, col
answer = 0
graph = [list(map(int, input().split())) for _ in range(N)]
wall_lst = []
for Ni in range(N):
    for Mi in range(M):
        if not graph[Ni][Mi]:
            wall_lst.append((Ni, Mi))

virus = []  # row, col
for row in range(N):
    for col in range(M):
        if graph[row][col] == 2:
            virus.append((row, col))
dx = [-1, 1, 0, 0]  # col
dy = [0, 0, -1, 1]  # row

def bfs(graph):
    tmp_graph = copy.deepcopy(graph)
    for order in order_lst:
        r, c = wall_lst[order]
        tmp_graph[r][c] = 1        
    q = deque(virus)

    while q:
        row, col = q.popleft()
        for i in range(4):
            next_row, next_col = row + dy[i], col + dx[i]
            if 0 <= next_row and next_row < N and 0 <= next_col and next_col < M:
                if not tmp_graph[next_row][next_col]:
                    q.append((next_row, next_col))
                    tmp_graph[next_row][next_col] = 2
    zero_cnt = 0
    for tmp_lst in tmp_graph:
        zero_cnt += tmp_lst.count(0)

    return zero_cnt

order_lst = []
def make_wall(start):
    global answer
    if len(order_lst) == 3:
        answer = max(bfs(graph), answer)
        return
    for i in range(start, len(wall_lst)):
        if i not in order_lst:
            order_lst.append(i)
            make_wall(i+1)
            order_lst.pop()

make_wall(0)
print(answer)
