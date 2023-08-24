import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())  # 가로, 세로, 단수

tomato_lst = []

q = deque()

already_complete = True
for row in range(H * N):
    row_lst = list(map(int, input().split()))
    for i in range(M):
        if row_lst[i] == 1:
            q.append((row, i))  # row, col
        elif not row_lst[i]:
            already_complete = False
    tomato_lst.append(row_lst)

if already_complete:
    print(0)
else:
    while q:
        now_row, now_col = q.popleft()
        now_cost = tomato_lst[now_row][now_col]
        now_stair = (now_row // N) + 1
        for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = now_row + nr
            next_col = now_col + nc
            if (now_stair - 1) * N <= next_row < now_stair * N and 0 <= next_col < M:
                if not tomato_lst[next_row][next_col]:
                    tomato_lst[next_row][next_col] = now_cost + 1
                    q.append((next_row, next_col))
        for nr, nc in [(N, 0), (-N, 0)]:
            next_row = now_row + nr
            next_col = now_col + nc
            if 0 <= next_row < H * N and 0 <= next_col < M:
                if not tomato_lst[next_row][next_col]:
                    tomato_lst[next_row][next_col] = now_cost + 1
                    q.append((next_row, next_col))
        
    ans = -2

    not_complete = False

    for i in tomato_lst:
        ans = max(ans, max(i))
        for j in i:
            if not j:
                not_complete = True
                break
        if not_complete:
            print(-1)
            break
    else:
        print(ans - 1)

