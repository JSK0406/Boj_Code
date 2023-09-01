import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())  # 칸의 개수, 하한선, 상한선
map_lst = [list(map(int, input().split())) for _ in range(N)]

def bfs(row, col):
    global visited_lst
    global map_lst

    q = deque()
    q.append((row, col))
    isChange = False
    tot_sum = map_lst[row][col]
    now_visited_lst = [(row, col)]
    visited_lst[row][col] = 1
    while q:
        now_row, now_col = q.popleft()
        for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < N and 0 <= next_col < N:
                if not visited_lst[next_row][next_col] and L <= abs(map_lst[now_row][now_col] - map_lst[next_row][next_col]) <= R:
                    isChange = True
                    visited_lst[next_row][next_col] = 1
                    tot_sum += map_lst[next_row][next_col]
                    now_visited_lst.append((next_row, next_col))
                    q.append((next_row, next_col))
    change_num = tot_sum // len(now_visited_lst)
    if isChange:
        for rr, cc in now_visited_lst:
            map_lst[rr][cc] = change_num
        return 1
    else:
        return 0

ans = 0
while True:
    visited_lst = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if not visited_lst[row][col]:
                cnt += bfs(row, col)
    if not cnt:
        break
    else:
        ans += 1

print(ans)