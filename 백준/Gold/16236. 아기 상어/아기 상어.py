import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

map_lst = [list(map(int, input().split())) for _ in range(N)]
start_row, start_col = 0, 0
dn = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 위 왼 오 아래

for i in range(N):
    for j in range(N):
        if map_lst[i][j] == 9:
            start_row, start_col = i, j
map_lst[start_row][start_col] = 0

def bfs(row, col, lev):
    global map_lst
    visited_lst = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((row, col, 0))
    visited_lst[row][col] = 1
    visiting_lst = []
    while q:
        now_row, now_col, cnt = q.popleft()
        for nr, nc in dn:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < N and 0 <= next_col < N and not visited_lst[next_row][next_col]:
                if 0 < map_lst[next_row][next_col] < lev:
                    visiting_lst.append((next_row, next_col, cnt + 1))
                    visited_lst[next_row][next_col] = 1
                elif map_lst[next_row][next_col] == 0 or map_lst[next_row][next_col] == lev:
                    q.append((next_row, next_col, cnt + 1))
                    visited_lst[next_row][next_col] = 1
                else:
                    visited_lst[next_row][next_col] = 1
    return visiting_lst

running_Flag = True
lev = 2
cnt = 0
ans = 0

while running_Flag:
    tmp_lst = bfs(start_row, start_col, lev)
    if not tmp_lst:
        running_Flag = False
        print(ans)
    else:
        tmp_lst.sort(key = lambda x : (x[2], x[0], x[1]))
        next_row, next_col = tmp_lst[0][0], tmp_lst[0][1]
        map_lst[next_row][next_col] = 0
        ans += tmp_lst[0][2]
        start_row, start_col = next_row, next_col
        cnt += 1
    if cnt == lev:
        lev += 1
        cnt = 0