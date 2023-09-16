# import sys
# input = sys.stdin.readline

# row, col = map(int, input().split())

# red_row, red_col, blue_row, blue_col = 0, 0, 0, 0
# map_lst = []

# for r in range(row):
#     row_lst = list(map(int, input().split()))
#     for c in range(col):
#         if row_lst[c] == 'R':
#             red_row, red_col = r, c
#         elif row_lst[c] == 'B':
#             blue_row, blue_col = r, c

# def move_up(now_row, now_col, map_lst, color):
#     next_row, next_col = now_row, now_col
#     while True:
#         if map_lst[next_row - 1][next_col] == '.':
#             next_row -= 1
#         else:
#             break
#     if color == 'R':
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'R'
#     else:
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'B'

#     if map_lst[next_row - 1][next_col] == 'O':
#         return (next_row, next_col, map_lst, 'F')
#     elif now_row == next_row and now_col == next_col:
#         return (next_row, next_col, map_lst, 'X')
#     else:
#         return (next_row, next_col, map_lst, 'O')
    
# def move_down(now_row, now_col, map_lst, color):
#     next_row, next_col = now_row, now_col
#     while True:
#         if map_lst[next_row + 1][next_col] == '.':
#             next_row += 1
#         else:
#             break
#     if color == 'R':
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'R'
#     else:
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'B'

#     if map_lst[next_row + 1][next_col] == 'O':
#         return (next_row, next_col, map_lst, 'F')
#     elif now_row == next_row and now_col == next_col:
#         return (next_row, next_col, map_lst, 'X')
#     else:
#         return (next_row, next_col, map_lst, 'O')

# def move_left(now_row, now_col, map_lst, color):
#     next_row, next_col = now_row, now_col
#     while True:
#         if map_lst[next_row][next_col - 1] == '.':
#             next_col -= 1
#         else:
#             break
#     if color == 'R':
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'R'
#     else:
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'B'

#     if map_lst[next_row][next_col - 1] == 'O':
#         return (next_row, next_col, map_lst, 'F')
#     elif now_row == next_row and now_col == next_col:
#         return (next_row, next_col, map_lst, 'X')
#     else:
#         return (next_row, next_col, map_lst, 'O')
    
# def move_right(now_row, now_col, map_lst, color):
#     next_row, next_col = now_row, now_col
#     while True:
#         if map_lst[next_row][next_col + 1] == '.':
#             next_col += 1
#         else:
#             break
#     if color == 'R':
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'R'
#     else:
#         map_lst[now_row][now_col] = '.'
#         map_lst[next_row][next_col] = 'B'

#     if map_lst[next_row][next_col + 1] == 'O':
#         return (next_row, next_col, map_lst, 'F')
#     elif now_row == next_row and now_col == next_col:
#         return (next_row, next_col, map_lst, 'X')
#     else:
#         return (next_row, next_col, map_lst, 'O')

# # result => F: 구멍에 빠짐, X: 안 움직임, O: 움직임 

# def move_blue_first(red_row, red_col, blue_row, blue_col, map_lst, cnt):
#     global ans
#     next_blue_row, next_blue_col, next_map_lst, blue_result = move_up(blue_row, blue_col, next_map_lst)
#     next_red_row, next_red_col, next_map_lst, red_result = move_up(red_row, red_col, map_lst)
#     if red_result == 'F':
#         ans = min(ans, cnt+1)
#         return 'Finish'
#     elif blue_result == 'F':
#         return 'Finish'
#     elif red_result == 'X' and blue_result == 'X':
#         return 'Finish'
#     else:
#         return (next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst)

# def move_red_first(red_row, red_col, blue_row, blue_col, map_lst, cnt):
#     next_red_row, next_red_col, next_map_lst, red_result = move_up(red_row, red_col, map_lst)
#     next_blue_row, next_blue_col, next_map_lst, blue_result = move_up(blue_row, blue_col, next_map_lst)
#     if red_result == 'F':
#         ans = min(ans, cnt+1)
#         return 'Finish'
#     elif blue_result == 'F':
#         return 'Finish'
#     elif red_result == 'X' and blue_result == 'X':
#         return 'Finish'
#     else:
#         return (next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst)

# ans = 999_999_999
# def dfs(red_row, red_col, blue_row, blue_col, map_lst, cnt):
#     global ans
    
#     # up
#     if red_col == blue_col:
#         if red_row > blue_row:
#             res = move_red_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#         else:
#             res = move_blue_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#     else:
#         res = move_red_first
#         if res == 'Finish':
#             return
#         else:
#             next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#             dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)

#     # down
#     if red_col == blue_col:
#         if red_row < blue_row:
#             res = move_red_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#         else:
#             res = move_blue_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#     else:
#         res = move_red_first
#         if res == 'Finish':
#             return
#         else:
#             next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#             dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)

#     # left

#     if red_row == blue_row:
#         if red_col < blue_col:
#             res = move_red_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#         else:
#             res = move_blue_first
#             if res == 'Finish':
#                 return
#             else:
#                 next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#                 dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#     else:
#         res = move_red_first
#         if res == 'Finish':
#             return
#         else:
#             next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst = res
#             dfs(next_red_row, next_red_col, next_blue_row, next_blue_col, next_map_lst, cnt+1)
#     # right




import sys
input = sys.stdin.readline

row, col, square_row, square_col, K = map(int, input().split())  # 세로, 가로, 주사위 x, 주사위 y, 명령의 개수
now_row, now_col = square_row, square_col
map_lst = [list(map(int, input().split())) for _ in range(row)]
order_lst = list(map(int, input().split()))
ans_lst = []
near, further, up, down, left, right = 0, 0, 0, 0, 0, 0
for i in range(K):
    order = order_lst[i]
    if order == 4:  # 남
        if 0 <= now_row + 1 < row:
            now_row += 1
            near, further, up, down, left, right = up, down, further, near, left, right
        else:
            continue
    elif order == 2:  # 서
        if 0 <= now_col - 1 < col:
            now_col -= 1
            near, further, up, down, left, right = near, further, right, left, up, down
        else:
            continue
    elif order == 3:  # 북
        if 0 <= now_row - 1 < row:
            now_row -= 1
            near, further, up, down, left, right = down, up, near, further, left, right
        else:
            continue
    else:  # 동
        if 0 <= now_col + 1 < col:
            now_col += 1
            near, further, up, down, left, right = near, further, left, right, down, up
        else:
            continue
    if map_lst[now_row][now_col] == 0:
        map_lst[now_row][now_col] = down
    else:
        down = map_lst[now_row][now_col]
        map_lst[now_row][now_col] = 0
    ans_lst.append(up)

for i in ans_lst:
    print(i)