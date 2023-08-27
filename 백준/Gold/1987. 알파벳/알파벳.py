import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map_lst = [list(input().strip()) for _ in range(R)]

alpha_set = set()

ans = 0
alpha_set.add(map_lst[0][0])
def dfs(row, col, cnt):
    global ans
    for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_row = row + nr
        next_col = col + nc
        if 0 <= next_row < R and 0 <= next_col < C and map_lst[next_row][next_col] not in alpha_set:
            alpha_set.add(map_lst[next_row][next_col])
            dfs(next_row, next_col, cnt+1)
            alpha_set.remove(map_lst[next_row][next_col])
    ans = max(ans, cnt)
    return

dfs(0, 0, 1)
print(ans)