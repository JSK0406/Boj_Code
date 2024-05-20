import sys
input = sys.stdin.readline

# 왼쪽 위부터 시작하는데 오른쪽 위, 오른쪽, 오른쪽 아래 우선순위로 진행

R, C = map(int, input().split())
map_lst = [list(input().strip()) for _ in range(R)]
visited_lst = [[0 for _ in range(C)] for _ in range(R)]

def dfs(now_row, now_col):
    is_done = False
    for nr, nc in [(-1, 1), (0, 1), (1, 1)]:
        next_row, next_col = now_row + nr, now_col + nc
        if 0 <= next_row < R and 0 <= next_col < C:
            if map_lst[next_row][next_col] == '.':
                if not visited_lst[next_row][next_col] and not is_done:
                    visited_lst[next_row][next_col] = 1
                    if (next_col == C-1):
                        return True
                    is_done = dfs(next_row, next_col)
                    # if not is_done:
                    #     visited_lst[next_row][next_col] = 0
    return is_done

ans = 0

for start_row in range(R):
    if dfs(start_row, 0):
        ans += 1

print(ans)