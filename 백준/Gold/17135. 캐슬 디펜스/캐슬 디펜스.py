import sys
input = sys.stdin.readline
from collections import deque
import itertools
import copy

# N * M 격자판
# 각 칸에 최대 한 명의 적
# N+1 행에는 모든 칸에 성이 있음
# 성에 궁수 3명, 한 칸에 한 명의 궁수
# 거리가 D이하인 적 => 가장 왼쪽에 있는 적 공격
# 같은 적이 여러 궁수에게 공격 당할 수도

# 대각선은 그냥 row, col 차이 +

R, C, D = map(int, input().split())
init_map = deque([list(map(int, input().split())) for _ in range(R)])

def move_enemy(map_lst):
    map_lst.pop()
    map_lst.appendleft([0 for _ in range(C)])
    return map_lst

def attack_enemy(map_lst, a_col):  # 궁수 col 좌표 (0 ~ C-1)
    if map_lst[R-1][a_col] == 1:
        return (R-1, a_col)

    q = deque()
    q.append((R-1, a_col, 1))

    visited_lst = [[0 for _ in range(C)] for _ in range(R)]
    visited_lst[R-1][a_col] = 1
    while q:
        now_row, now_col, now_d = q.popleft()
        for nr, nc in [(0, -1), (-1, 0), (0, 1)]:
            next_row, next_col = now_row + nr, now_col + nc
            if 0 <= next_row < R and 0 <= next_col < C:
                if not visited_lst[next_row][next_col]:
                    if now_d + 1 <= D:
                        if map_lst[next_row][next_col] == 1:
                            return (next_row, next_col)
                        q.append((next_row, next_col, now_d+1))
    return (-1, -1)
def check_finish(map_lst):
    check_sum = 0
    for lst in map_lst:
        check_sum += sum(lst)
    if check_sum == 0:
        return True
    else:
        return False

ans = 0
for iter_cols in itertools.combinations(range(C), 3):
    now_catched = 0
    now_map = copy.deepcopy(init_map)
    while True:
        catched_enemy = set()
        for iter_col in iter_cols:
            catched_row, catched_col = attack_enemy(now_map, iter_col)
            if catched_row != -1 and catched_col != -1:
                catched_enemy.add((catched_row, catched_col))
        now_catched += len(catched_enemy)
        for r, c in list(catched_enemy):
            now_map[r][c] = 0
        now_map = move_enemy(now_map)
        if check_finish(now_map) == True:
            break
    ans = max(ans, now_catched)

print(ans)