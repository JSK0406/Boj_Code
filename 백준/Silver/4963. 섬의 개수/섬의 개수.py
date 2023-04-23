import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]  # col
dy = [-1, 0, 1, -1, 1, -1, 0, 1]  # row

def check(row, col):
    global cnt
    global graph

    q = deque()
    q.append((row, col))
    graph[row][col] = 0
    while q:
        row, col = q.popleft()
        for i in range(8):
            next_row, next_col = row + dy[i], col + dx[i]
            if 0 <= next_row and next_row < h and 0 <= next_col and next_col < w:
                if graph[next_row][next_col]:
                    graph[next_row][next_col] = 0
                    q.append((next_row, next_col))
    cnt += 1
            
while True:
    w, h = map(int, input().split())  # col, row
    if not w and not h:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for row in range(h):
        for col in range(w):
            if graph[row][col]:
                check(row, col)
    print(cnt)