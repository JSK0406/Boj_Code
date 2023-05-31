import sys
input = sys.stdin.readline
from collections import deque
dn = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N, M, fuel = map(int, input().split())  # 맵 크기, 배달지 수, 연료
map_lst = [list(map(int, input().split())) for _ in range(N)]
start_row, start_col = map(int, input().split())
start_row -= 1
start_col -= 1
delivery_dict = dict()
for _ in range(M):
    A, B, C, D = map(int, input().split())
    A-=1
    B-=1
    C-=1
    D-=1
    map_lst[A][B] = 2  # 2는 dept
    delivery_dict[(A, B)] = (C, D)
# dept_row, dept_col, arrive_row, arrive_col

def bfs1(start_row, start_col):
    q = deque()
    visited_lst = [[0 for _ in range(N)] for _ in range(N)]
    visiting_lst = []
    q.append((start_row, start_col, 0))
    visited_lst[start_row][start_col] = 1
    if map_lst[start_row][start_col] == 2:
        return [(start_row, start_col, 0)]
    while q:
        now_row, now_col, cnt = q.popleft()
        for dr, dc in dn:
            next_row = now_row + dr
            next_col = now_col + dc
            if 0 <= next_row < N and 0 <= next_col < N and not visited_lst[next_row][next_col]:
                if map_lst[next_row][next_col] != 1:
                    if map_lst[next_row][next_col] == 0:
                        visited_lst[next_row][next_col] = 1
                        q.append((next_row, next_col, cnt + 1))
                    elif map_lst[next_row][next_col] == 2:
                        visiting_lst.append((next_row, next_col, cnt + 1))
    return visiting_lst

def bfs2(dept_row, dept_col, arrive_row, arrive_col):
    q = deque()
    visited_lst = [[0 for _ in range(N)] for _ in range(N)]
    q.append((dept_row, dept_col, 0))
    while q:
        now_row, now_col, cnt = q.popleft()
        for dr, dc in dn:
            next_row, next_col = now_row + dr, now_col + dc
            if 0 <= next_row < N and 0 <= next_col < N and not visited_lst[next_row][next_col]:
                if next_row == arrive_row and next_col == arrive_col:
                    return cnt + 1
                elif map_lst[next_row][next_col] != 1:
                    q.append((next_row, next_col, cnt+1))
                    visited_lst[next_row][next_col] = 1
                    

Flag = True
while delivery_dict:
    tmp_lst = bfs1(start_row, start_col)
    tmp_lst.sort(key = lambda x : (x[2], x[0], x[1]))
    if tmp_lst:
        tmp1 = tmp_lst[0]
        dept_row, dept_col, price1 = tmp1
        map_lst[dept_row][dept_col] = 0
        arrive_row, arrive_col = delivery_dict[(dept_row, dept_col)]
        del delivery_dict[(dept_row, dept_col)]
        price2 = bfs2(dept_row, dept_col, arrive_row, arrive_col)
        if price2:
            if fuel >= price1 + price2:
                fuel = fuel - price1 + price2
                start_row, start_col = arrive_row, arrive_col
            else:
                Flag = False
                break
        else:
            Flag = False
            break
    else:
        Flag = False
        break
if Flag:
    print(fuel)
else:
    print(-1)