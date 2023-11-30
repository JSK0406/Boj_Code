import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

N, M = map(int, input().split())
map_lst = [list(map(int, input().strip())) for _ in range(M)]
visited_lst = [[-1 for _ in range(N)] for _ in range(M)]
visited_lst[0][0] = 0
hq = [[0, 0, 0]]  # price, row, col
while visited_lst[-1][-1] == -1:
    price, row, col = heapq.heappop(hq)
    for nr, nc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_row = row + nr
        next_col = col + nc
        if 0 <= next_row < M and 0 <= next_col < N and visited_lst[next_row][next_col] == -1:
            if map_lst[next_row][next_col] == 1:
                visited_lst[next_row][next_col] = price + 1
            else:
                visited_lst[next_row][next_col] = price
            heapq.heappush(hq, [visited_lst[next_row][next_col], next_row, next_col])

print(visited_lst[-1][-1])