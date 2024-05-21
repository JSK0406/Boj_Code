import sys
input = sys.stdin.readline
from collections import deque
import itertools

N = int(input())

teachers = []

map_lst = []

for r in range(N):
    tmp = list(input().strip().split())
    for c in range(N):
        if tmp[c] == 'T':
            teachers.append((r, c, 0, 1))
            teachers.append((r, c, 0, -1))
            teachers.append((r, c, 1, 0))
            teachers.append((r, c, -1, 0))
    map_lst.append(tmp)

def check(map_lst):
    q = deque(teachers)
    is_possible = True
    
    while q and is_possible:
        now_row, now_col, nr, nc = q.popleft()
        next_row, next_col = now_row + nr, now_col + nc
        if 0 <= next_row < N and 0 <= next_col < N:
            if map_lst[next_row][next_col] == 'X':
                q.append((next_row, next_col, nr, nc))
            elif map_lst[next_row][next_col] == 'S':
                is_possible = False
                break
    return is_possible

cords = []

for i in range(N):
    for j in range(N):
        cords.append((i, j))

ans = False
for i in itertools.combinations(cords, 3):
    all_x = True
    for x, y in i:
        if map_lst[x][y] != 'X':
            all_x = False
    if not all_x:
        continue

    for x, y in i:
        map_lst[x][y] = 0
    if check(map_lst):
        ans = True
    for x, y in i:
        map_lst[x][y] = 'X'
    if ans:
        break
    
print('YES' if ans == True else 'NO')