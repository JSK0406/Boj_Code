import sys
input = sys.stdin.readline
from collections import deque
import copy

row, col = map(int, input().split())
tot_cheese = 0
cnt = 0
map_lst = []

for r in range(row):
    lst = list(map(int, input().split()))
    for c in range(col):
        if lst[c] == 1:
            tot_cheese += 1
    map_lst.append(lst)

def bfs(now_map_lst):
    next_map_lst = copy.deepcopy(now_map_lst)
    visited_lst = [[0 for _ in range(col)] for _ in range(row)]

    q = deque()
    q.append((0, 0))
    delete_cheese = 0
    visited_lst[0][0] = 1

    while q:
        now_row, now_col = q.popleft()
        for nr, nc in [(0, 1), (0, -1), (1, 0), (-1 ,0)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < row and 0 <= next_col < col:
                if not visited_lst[next_row][next_col]:
                    if now_map_lst[next_row][next_col] == 1:
                        next_map_lst[next_row][next_col] = 0
                        visited_lst[next_row][next_col] = 1
                        delete_cheese += 1
                    else:
                        visited_lst[next_row][next_col] = 1
                        q.append((next_row, next_col))

    return (next_map_lst, delete_cheese)

while True:
    map_lst, delete_cheese = bfs(map_lst)
    cnt += 1
    if delete_cheese == tot_cheese:
        break
    else:
        tot_cheese -= delete_cheese


print(cnt)
print(tot_cheese)