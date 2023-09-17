import sys
input = sys.stdin.readline
from collections import deque

# 파란 구슬 빠지면 제외
# 10회 넘어가면 끝
# 이동 없으면 안 넣음

row, col = map(int, input().split())

map_lst = []

R_row, R_col, B_row, B_col = -1, -1, -1, -1
for ri in range(row):
    row_lst = list(input().strip())
    map_lst.append(row_lst)
    for ci in range(col):
        if row_lst[ci] == 'R':
            R_row, R_col = ri, ci
        elif row_lst[ci] == 'B':
            B_row, B_col = ri, ci
        
q = deque()
q.append((R_row, R_col, B_row, B_col, 0))
isFinish = False
ans = -1
visited_lst = [(R_row, R_col, B_row, B_col, 0)]
while q:
    R_row, R_col, B_row, B_col, now_cnt = q.popleft()
    if now_cnt >= 10:
        break
    for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        isAppend = True
        next_R_row, next_R_col = R_row, R_col
        while map_lst[next_R_row+nr][next_R_col+nc] not in ['#', 'O']:
            next_R_row, next_R_col = next_R_row + nr, next_R_col + nc

        if map_lst[next_R_row+nr][next_R_col+nc] == '#':
            pass
        elif map_lst[next_R_row+nr][next_R_col+nc] == 'O':
            isFinish = True

        next_B_row, next_B_col = B_row, B_col
        while map_lst[next_B_row+nr][next_B_col+nc] not in ['#', 'O']:
            next_B_row, next_B_col = next_B_row + nr, next_B_col + nc

        if map_lst[next_B_row+nr][next_B_col+nc] == '#':
            pass
        elif map_lst[next_B_row+nr][next_B_col+nc] == 'O':
            isFinish = False
            continue
        if isFinish:
            break
        if next_R_row == next_B_row and next_B_col == next_R_col:
            if abs(R_row - next_R_row) + abs(R_col - next_R_col) < abs(B_row - next_B_row) + abs(B_col - next_B_col):
                next_B_row -= nr
                next_B_col -= nc
            else:
                next_R_row -= nr
                next_R_col -= nc
        if (next_B_row, next_B_col) == (B_row, B_col) and (next_R_row, next_R_col) == (R_row, R_col):
            isAppend = False
        if isAppend and (next_R_row, next_R_col, next_B_row, next_B_col, now_cnt + 1) not in visited_lst:
            q.append((next_R_row, next_R_col, next_B_row, next_B_col, now_cnt + 1))
    if isFinish:
        ans = now_cnt + 1
        break

print(ans)