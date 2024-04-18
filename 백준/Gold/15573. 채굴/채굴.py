import sys
input = sys.stdin.readline
from collections import deque

# row, col, 캐야하는 광물 개수
R, C, K = map(int, input().split())
least, largest = 1, 0

map_lst = []

for _ in range(R):
    tmp_lst = list(map(int, input().split()))
    largest = max(largest, max(tmp_lst))
    map_lst.append(tmp_lst)

ans = 999_999_999
while least <= largest:
    mid = (least + largest) // 2
    cnt = 0
    q = deque()
    visited_lst = [[0 for _ in range(C)] for _ in range(R)]
    # 맨 위 추가
    for i in range(C):
        if map_lst[0][i] <= mid:
            q.append((0, i))
            visited_lst[0][i] = 1
            cnt += 1
    # 양 옆 추가
    for i in range(1, R):
        if map_lst[i][0] <= mid:
            q.append((i, 0))
            visited_lst[i][0] = 1
            cnt += 1
        if map_lst[i][C-1] <= mid:
            q.append((i, C-1))
            visited_lst[i][C-1] = 1
            cnt += 1

    if cnt == 0:
        least = mid+1
        continue
    if cnt >= K:
        ans = min(ans, mid)
        largest = mid-1
    while q:
        now_row, now_col = q.popleft()
        if cnt >= K:
            break
        for nr, nc in [(0, -1), (1, 0), (-1, 0), (0, 1)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < R and 0 <= next_col < C:
                if not visited_lst[next_row][next_col] and map_lst[next_row][next_col] <= mid:
                    visited_lst[next_row][next_col] = 1
                    cnt += 1
                    q.append((next_row, next_col))
                    if cnt >= K:
                        break

    if cnt < K:
        least = mid+1
    else:
        ans = min(ans, mid)
        largest = mid-1

print(least)