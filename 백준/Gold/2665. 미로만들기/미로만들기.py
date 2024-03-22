import sys
input = sys.stdin.readline
import heapq

N = int(input())

# 0: 검은 방, 1: 흰 방
map_lst = [list(map(int, list(input().strip()))) for _ in range(N)]

visited_lst = [[sys.maxsize for _ in range(N)] for _ in range(N)]

hq = []  # 색 변경 횟수, row, col
heapq.heappush(hq, (0, 0, 0))

def check_map(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False

isFinish = False
visited_lst[0][0] = 0

while hq and not isFinish:
    now_cnt, now_row, now_col = heapq.heappop(hq)
    for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        next_row, next_col = now_row + dr, now_col + dc
        if check_map(next_row, next_col):
            if map_lst[next_row][next_col] == 0:  # 검은 방
                if visited_lst[next_row][next_col] > now_cnt + 1:
                    visited_lst[next_row][next_col] = now_cnt + 1
                    if next_row == N-1 and next_col == N-1:
                        isFinish = True
                        break
                    heapq.heappush(hq, (now_cnt+1, next_row, next_col))
            elif map_lst[next_row][next_col] == 1:  # 흰 방
                if visited_lst[next_row][next_col] > now_cnt:
                    visited_lst[next_row][next_col] = now_cnt
                    if next_row == N-1 and next_col == N-1:
                        isFinish = True
                        break
                    heapq.heappush(hq, (now_cnt, next_row, next_col))

print(visited_lst[-1][-1])