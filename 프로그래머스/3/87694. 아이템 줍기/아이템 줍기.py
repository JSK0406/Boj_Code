# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
    
#     # 해당 위치에서 dir, 해당 칸으로 이동 가능한지
#     map_lst = [[[0, -1] for _ in range(51)] for _ in range(51)]
    
#     # x1, y1, x2, y2 =>
#     # x1,y1부터 x2,y1까지, x1,y2부터 x2,y2까지  1번
#     # x1,y1부터 x1,y2까지, x2,y1부터 x2,y2까지  0번
#     # 꼭짓점 왼위 : 2, 오위: 3, 왼아 : 4, 오아 : 5
#     # 겹치는 건 6
#     # 재배치 가능하면 0, 배치가 아예 안된 건 -1, 도형 안쪽은 -2
    
#     for x1,y1,x2,y2 in rectangle:
#         for x in range(x1, x2+1):  # 양 옆
#             if map_lst[x][y1][1] == -1:
#                 map_lst[x][y1][0] = 1
#                 map_lst[x][y1][1] = 0
#             elif map_lst[x][y1][1] != -2:
#                 map_lst[x][y1][0] = 6
#                 map_lst[x][y1][1] = 0
#             if map_lst[x][y2][1] == -1:
#                 map_lst[x][y2][0] = 1
#                 map_lst[x][y2][1] = 0
#             elif map_lst[x][y2][1] != -2:
#                 map_lst[x][y2][0] = 6
#                 map_lst[x][y2][1] = 0
#         for y in range(y1, y2+1):  # 위 아래
#             if map_lst[x1][y][1] == -1:
#                 map_lst[x1][y][0] = 0
#                 map_lst[x1][y][1] = 0
#             elif map_lst[x1][y][1] != -2:
#                 map_lst[x1][y][0] = 6
#                 map_lst[x1][y][1] = 0
#             if map_lst[x2][y][1] == -1:
#                 map_lst[x2][y][0] = 0
#                 map_lst[x2][y][1] = 0
#             elif map_lst[x2][y][1] != -2:
#                 map_lst[x2][y][0] = 6
#                 map_lst[x2][y][1] = 0
#         map_lst[x1][y1][0] = 4
#         map_lst[x2][y2][0] = 3
#         map_lst[x1][y2][0] = 2
#         map_lst[x2][y1][0] = 5
#         for x in range(x1+1, x2):
#             for y in range(y1+1, y2):
#                 map_lst[x][y][1] = -2
            
#     visited_lst = [[0 for _ in range(51)] for _ in range(51)]
    
#     q = deque()
#     q.append((characterX, characterY, 0))  # x좌표, y좌표, count
#     visited_lst[characterX][characterY] = 1
#     is_finish = False
#     while q and not is_finish:
#         now_x, now_y, now_cnt = q.popleft()
#         print(now_x, now_y, now_cnt)
#         dir = map_lst[now_x][now_y][0]  # 0이면 위아래 1이면 양옆
#         print(dir)
#         # 꼭짓점 왼위 : 2, 오위: 3, 왼아 : 4, 오아 : 5
#         if dir == 0:  # 위 아래
#             dir_lst = [(0, 1), (0, -1)]
#         elif dir == 1:  # 양 옆
#             dir_lst = [(1, 0), (-1, 0)]
#         elif dir == 2:
#             dir_lst = [(1, 0), (0, -1)]
#         elif dir == 3:
#             dir_lst = [(-1, 0), (0, -1)]
#         elif dir == 4:
#             dir_lst = [(1, 0), (0, 1)]
#         elif dir == 5:
#             dir_lst = [(-1, 0), (0, 1)]
#         elif dir == 6:
#             dir_lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         for nx, ny in dir_lst:
#             next_x, next_y = now_x + nx, now_y + ny
#             if map_lst[next_x][next_y][1] in [-1, -2]:
#                 continue
#             if next_x == itemX and next_y == itemY:
#                 answer = now_cnt+1
#                 is_finish = True
#                 break
#             if map_lst[next_x][next_y][1] == 0 and not visited_lst[next_x][next_y]:
#                 q.append((next_x, next_y, now_cnt+1))
#                 visited_lst[next_x][next_y] = 1
                
#     return answer






from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # answer = 0
    answer = []
    
    # 해당 위치에서 dir, 해당 칸으로 이동 가능한지(0이면 빈칸 / 1이면 채워짐 / 2이면 못감)
    map_lst = [[[0, 0] for _ in range(102)] for _ in range(102)]
    
    # x1, y1, x2, y2 =>
    # 좌우 0번
    # 상하 1번
    # 상하좌우 2번
    
    for x1,y1,x2,y2 in rectangle:
        for x in range(2*x1, 2*x2+1):  # 양 옆
            if map_lst[x][2*y1][1] == 0:
                map_lst[x][2*y1][0] = 0
                map_lst[x][2*y1][1] = 1
            elif map_lst[x][2*y1][1] == 1:
                map_lst[x][2*y1][0] = 2
            if map_lst[x][2*y2][1] == 0:
                map_lst[x][2*y2][0] = 0
                map_lst[x][2*y2][1] = 1
            elif map_lst[x][2*y2][1] == 1:
                map_lst[x][2*y2][0] = 2
        for y in range(2*y1, 2*y2+1):  # 위 아래
            if map_lst[2*x1][y][1] == 0:
                map_lst[2*x1][y][0] = 1
                map_lst[2*x1][y][1] = 1
            elif map_lst[2*x1][y][1] == 1:
                map_lst[2*x1][y][0] = 2
            if map_lst[2*x2][y][1] == 0:
                map_lst[2*x2][y][0] = 1
                map_lst[2*x2][y][1] = 1
            elif map_lst[2*x2][y][1] == 1:
                map_lst[2*x2][y][0] = 2
                
        map_lst[2*x1][2*y1][0] = 2
        map_lst[2*x1][2*y1][1] = 1
        map_lst[2*x2][2*y2][0] = 2
        map_lst[2*x2][2*y2][1] = 1
        map_lst[2*x1][2*y2][0] = 2
        map_lst[2*x1][2*y2][1] = 1
        map_lst[2*x2][2*y1][0] = 2
        map_lst[2*x2][2*y1][1] = 1
        
        # 도형 안 처리
        for x in range(2*x1+1, 2*x2):
            for y in range(2*y1+1, 2*y2):
                map_lst[x][y][1] = 2
            
    visited_lst = [[0 for _ in range(102)] for _ in range(102)]
    
    q = deque()
    q.append((2*characterX, 2*characterY, 0))  # x좌표, y좌표, count
    visited_lst[2*characterX][2*characterY] = 1
    is_finish = False
    while q and not is_finish:
        now_x, now_y, now_cnt = q.popleft()
        dir = map_lst[now_x][now_y][0]  # 0이면 위아래 1이면 양옆
        # 꼭짓점 왼위 : 2, 오위: 3, 왼아 : 4, 오아 : 5
        if dir == 1:  # 위 아래
            dir_lst = [(0, 1), (0, -1)]
        elif dir == 0:  # 양 옆
            dir_lst = [(1, 0), (-1, 0)]
        elif dir == 2:
            dir_lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
        for nx, ny in dir_lst:
            next_x, next_y = now_x + nx, now_y + ny

            # 0이면 비어있음, 2이면 못감
            if map_lst[next_x][next_y][1] in [0, 2]:
                continue
            if next_x == itemX*2 and next_y == itemY*2:
                # answer = now_cnt+1
                # is_finish = True
                answer.append(now_cnt+1)
                break
            if map_lst[next_x][next_y][1] == 1 and not visited_lst[next_x][next_y]:
                q.append((next_x, next_y, now_cnt+1))
                visited_lst[next_x][next_y] = 1
                
    # return answer//2
    return min(answer) // 2

