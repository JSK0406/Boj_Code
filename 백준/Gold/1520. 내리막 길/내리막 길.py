import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map_lst = [list(map(int, input().split())) for _ in range(R)]

visited_lst = [[-1 for _ in range(C)] for _ in range(R)]

def dfs(now_row, now_col):
    global visited_lst

    now_height = map_lst[now_row][now_col]

    if now_row == R-1 and now_col == C-1:
        return 1
    
    if visited_lst[now_row][now_col] == -1:
        visited_lst[now_row][now_col] = 0

        tmp = 0
        for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < R and 0 <= next_col < C:
                if now_height > map_lst[next_row][next_col]:
                    tmp += dfs(next_row, next_col)

        visited_lst[now_row][now_col] += tmp

    return visited_lst[now_row][now_col]


print(dfs(0, 0))