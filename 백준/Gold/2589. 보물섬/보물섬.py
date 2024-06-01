import sys
input = sys.stdin.readline
from collections import deque
import itertools
import heapq

# L : 육지, W: 바다

R, C = map(int, input().split())

map_lst = [list(input().strip()) for _ in range(R)]

def bfs(r, c):
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    tmp_ans = 0
    while q:
        now_row, now_col = q.popleft()
        now_cnt = visited[now_row][now_col]
        for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < R and 0 <= next_col < C:
                if visited[next_row][next_col] == -1 and map_lst[next_row][next_col] == 'L':
                    visited[next_row][next_col] = now_cnt + 1
                    q.append((next_row, next_col))
                    tmp_ans = max(tmp_ans, now_cnt+1)
    return tmp_ans

ans = 0

for r in range(R):
    for c in range(C):
        if map_lst[r][c] == 'L':
            ans = max(ans, bfs(r, c))

print(ans)