import sys
input = sys.stdin.readline
from collections import deque
import itertools

# 더러운 칸 => 깨끗한 칸
# 가구 놓여진 칸 이동 x
# 같은 칸 여러번 가능

while True:

    C, R = map(int, input().split())

    # 종료조건
    if R == 0 and C == 0:
        break

    robot_row, robot_col = -1, -1
    dust_lst = []
    map_lst= [list(input().strip()) for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if map_lst[r][c] == 'o':
                robot_row, robot_col = r, c
            if map_lst[r][c] == '*':
                dust_lst.append([r, c])

    tot_lst = [[robot_row, robot_col]] + dust_lst  # 로봇청소기와 먼지 좌표 동시
    dist_matrix = [[-1 for _ in range(len(tot_lst))] for _ in range(len(tot_lst))]
    # 0번 인덱스는 로봇

    # 각 지점마다 서로의 거리를 찾는 과정
    for now_idx in range(len(tot_lst)):
        dist_matrix[now_idx][now_idx] = 0
        start_row, start_col = tot_lst[now_idx]

        visited_lst = [[-1 for _ in range(C)] for _ in range(R)]
        target_cnt = len(tot_lst) - 1
        q = deque()
        q.append((start_row, start_col))
        visited_lst[start_row][start_col] = 0
        while q and target_cnt > 0:
            now_row, now_col = q.popleft()
            now_cnt = visited_lst[now_row][now_col]
            for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                next_row, next_col = now_row + nr, now_col + nc
                if 0 <= next_row < R and 0 <= next_col < C:
                    if map_lst[next_row][next_col] != 'x':
                        if visited_lst[next_row][next_col] == -1:
                            visited_lst[next_row][next_col] = now_cnt + 1
                            q.append((next_row, next_col))
                            if [next_row, next_col] in tot_lst:
                                found_idx = tot_lst.index([next_row, next_col])
                                dist_matrix[now_idx][found_idx] = visited_lst[next_row][next_col]
                                target_cnt -= 1

    ans = sys.maxsize
    for i in itertools.permutations([i for i in range(1, len(tot_lst))], len(tot_lst)-1):
        order_lst = [0] + list(i)
        tmp_ans = 0
        is_impossible = False
        for now_idx in range(len(order_lst)-1):
            now, next = order_lst[now_idx], order_lst[now_idx+1]
            if dist_matrix[now][next] == -1:
                is_impossible = True
                break
            tmp_ans += dist_matrix[now][next]
        if not is_impossible:
            ans = min(ans, tmp_ans)

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)
