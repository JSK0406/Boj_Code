import sys
input = sys.stdin.readline
from collections import deque
import copy
N = int(input())
map_lst = [list(map(int, input().split())) for _ in range(N)]

def move_up(map_lst):
    merge_lst = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(1, N):
        for col in range(N):
            if map_lst[row][col] == 0:
                continue
            move_row = row
            while True:
                if map_lst[move_row-1][col] == 0:
                    map_lst[move_row-1][col] = map_lst[move_row][col]
                    map_lst[move_row][col] = 0
                    move_row -= 1
                    if move_row == 0:
                        break
                else:
                    break
            if not merge_lst[move_row][col] and move_row and map_lst[move_row][col] == map_lst[move_row-1][col]:
                map_lst[move_row-1][col] *= 2
                map_lst[move_row][col] = 0
                merge_lst[move_row][col] = 1
    return map_lst


def move_down(map_lst):
    merge_lst = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N-2, -1, -1):
        for col in range(N):
            if map_lst[row][col] == 0:
                continue
            move_row = row
            while True:
                if map_lst[move_row+1][col] == 0:
                    map_lst[move_row+1][col] = map_lst[move_row][col]
                    map_lst[move_row][col] = 0
                    move_row += 1
                    if move_row == N-1:
                        break
                else:
                    break
            if not merge_lst[move_row][col] and not move_row == N-1 and map_lst[move_row][col] == map_lst[move_row+1][col]:
                map_lst[move_row+1][col] *= 2
                map_lst[move_row][col] = 0
                merge_lst[move_row][col] = 1
    return map_lst
def move_left(map_lst):
    merge_lst = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(1, N):
            if map_lst[row][col] == 0:
                continue
            move_col = col
            while True:
                if map_lst[row][move_col-1] == 0:
                    map_lst[row][move_col-1] = map_lst[row][move_col]
                    map_lst[row][move_col] = 0
                    move_col -= 1
                    if move_col == 0:
                        break
                else:
                    break
            if not merge_lst[row][move_col] and move_col and map_lst[row][move_col] == map_lst[row][move_col-1]:
                map_lst[row][move_col-1] *= 2
                map_lst[row][move_col] = 0
                merge_lst[row][move_col] = 1
    return map_lst
def move_right(map_lst):
    merge_lst = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N-2, -1, -1):
            if map_lst[row][col] == 0:
                continue
            move_col = col
            while True:
                if map_lst[row][move_col+1] == 0:
                    map_lst[row][move_col+1] = map_lst[row][move_col]
                    map_lst[row][move_col] = 0
                    move_col += 1
                    if move_col == N-1:
                        break
                else:
                    break
            if not merge_lst[row][move_col] and not move_col == N-1 and map_lst[row][move_col] == map_lst[row][move_col+1]:
                map_lst[row][move_col+1] *= 2
                map_lst[row][move_col] = 0
                merge_lst[row][move_col] = 1
    return map_lst

def cal_max(map_lst):
    merge_lst = [[0 for _ in range(N)] for _ in range(N)]
    max_num = 0
    for r in range(N):
        for c in range(N):
            max_num = max(max_num, map_lst[r][c])
    return max_num

ans = 0
q = deque()
q.append((copy.deepcopy(map_lst), 0))
while q:
    now_map, cnt = q.popleft()
    # print(now_map, cnt)
    ans = max(ans, cal_max(now_map))
    if cnt == 5:
        continue
    q.append((move_up(copy.deepcopy(now_map)), cnt+1))
    q.append((move_down(copy.deepcopy(now_map)), cnt+1))
    q.append((move_left(copy.deepcopy(now_map)), cnt+1))
    q.append((move_right(copy.deepcopy(now_map)), cnt+1))

print(ans)