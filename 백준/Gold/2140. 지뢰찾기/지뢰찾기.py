import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
map_lst = [list(input().strip()) for _ in range(N)]

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

def check(a, b):
    return 0 <= a < N and 0 <= b < N

for now_row in range(1, N-1):
    for now_col in range(1, N-1):
        for i in range(8):
            next_row, next_col = now_row + dr[i], now_col + dc[i]
            if check(next_row, next_col):
                if not map_lst[next_row][next_col] in ["X", "#"]:
                    if map_lst[next_row][next_col] == "0":
                        map_lst[now_row][now_col] = "X"
                        break
        else:
            for i in range(8):
                next_row, next_col = now_row + dr[i], now_col + dc[i]
                if check(next_row, next_col):
                    if not map_lst[next_row][next_col] in ["X", "#"]:
                        map_lst[next_row][next_col] = str(int(map_lst[next_row][next_col]) - 1)

ans = 0

for lst in map_lst:
    ans += lst.count("#")

print(ans)