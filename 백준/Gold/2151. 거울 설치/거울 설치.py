import sys
input = sys.stdin.readline
from collections import deque
INF = sys.maxsize

N = int(input())
map_lst = [list(input().strip()) for _ in range(N)]
visited_lst = [[[INF for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]  # 거울을 지나친 수

start_row, start_col = -1, -1
end_row, end_col = -1, -1

for r in range(N):
    for c in range(N):
        if map_lst[r][c] == '#':
            if start_row == -1:
                start_row, start_col = r, c
            else:
                end_row, end_col = r, c

def check(r, c):
    return 0 <= r < N and 0 <= c < N

# '#' = 문
# '.' = 아무것도 없는 공간
# '!' = 거울 설치 가능 공간
# '*' = 벽

# 위에서 내려오면 왼쪽, 오른쪽
# 아래에서 올라오면 왼쪽, 오른쪽
# 로직상 거울 2가지 경우를 고려하지 않아도 됨
# 거울을 설치하지 않아도 됨

# 최소 거울 수
# 0, 1, 2, 3 => 왼쪽, 오른쪽, 위, 아래
dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

q = deque()  # r, c, 거울 수
for i in range(4):
    nr, nc = dir[i]
    next_row, next_col = start_row + nr, start_col + nc
    if check(next_row, next_col) and map_lst[next_row][next_col] != '*':
        visited_lst[start_row][start_col][i] = 0
        q.append((start_row, start_col, 0, i))

while q:
    now_row, now_col, now_cnt, now_dir = q.popleft()
    nr, nc = dir[now_dir]
    next_row, next_col = now_row + nr, now_col + nc
    if check(next_row, next_col) and map_lst[next_row][next_col] != '*':
        if visited_lst[next_row][next_col][now_dir] > now_cnt:
            # 문일 때
            if map_lst[next_row][next_col] == '#':
                visited_lst[next_row][next_col][now_dir] = now_cnt
            # 빈 공간일 때
            if map_lst[next_row][next_col] == '.':
                visited_lst[next_row][next_col][now_dir] = now_cnt
                q.append((next_row, next_col, now_cnt, now_dir))
            # 거울 설치 가능 공간일 때
            if map_lst[next_row][next_col] == '!':
                q.append((next_row, next_col, now_cnt, now_dir))
                if now_dir == 0 or now_dir == 1:
                    for next_dir in [2, 3]:
                        if visited_lst[next_row][next_col][next_dir] > now_cnt + 1:
                            q.append((next_row, next_col, now_cnt + 1, next_dir))
                            visited_lst[next_row][next_col][next_dir] = now_cnt + 1
                if now_dir == 2 or now_dir == 3:
                    for next_dir in [0, 1]:
                        if visited_lst[next_row][next_col][next_dir] > now_cnt + 1:
                            q.append((next_row, next_col, now_cnt + 1, next_dir))
                            visited_lst[next_row][next_col][next_dir] = now_cnt + 1
print(min(visited_lst[end_row][end_col]))