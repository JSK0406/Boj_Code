import sys
import heapq

input = sys.stdin.readline
INF = 1e9
cnt = 1

while True:
    N = int(input())
    if N == 0:
        break
    cost_lst = [0]
    for _ in range(N):
        cost_lst.append([0] + list(map(int, input().split())))
    lowest = [[INF for _ in range(N+1)] for _ in range(N+1)]
    lowest[1][1] = cost_lst[1][1]
    hq = [(cost_lst[1][1], 1, 1)]
    while True:
        cost, row, col = heapq.heappop(hq)
        if row + 1 <= N:
            tmp = cost + cost_lst[row+1][col]
            if lowest[row+1][col] > tmp:
                lowest[row+1][col] = tmp
                heapq.heappush(hq, (tmp, row+1,col))
        if row - 1 >= 1:
            tmp = cost + cost_lst[row-1][col]
            if lowest[row-1][col] > tmp:
                lowest[row-1][col] = tmp
                heapq.heappush(hq, (tmp, row-1,col))
        if col + 1 <= N:
            tmp = cost + cost_lst[row][col+1]
            if lowest[row][col+1] > tmp:
                lowest[row][col+1] = tmp
                heapq.heappush(hq, (tmp, row, col+1))
        if col - 1 >= 1:
            tmp = cost + cost_lst[row][col-1]
            if lowest[row][col-1] > tmp:
                lowest[row][col-1] = tmp
                heapq.heappush(hq, (tmp, row, col-1))
        if lowest[N][N] != INF:
            print(f"Problem {cnt}: {lowest[N][N]}")
            cnt += 1
            break


            
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     cost_lst = [0]
#     for _ in range(N):
#         cost_lst.append([0] + list(map(int, input().split())))
#     lowest = [[INF for _ in range(N+1)] for _ in range(N+1)]
#     lowest[1][1] = cost_lst[1][1]
#     hq = [(cost_lst[1][1], 1, 1)]
#     moveX = [1, -1, 0, 0]
#     moveY = [0, 0, 1, -1]
#     while hq:
#         cost, row, col = heapq.heappop(hq)
#         for i in range(4):
#             next_Y = row+moveY[i]
#             next_X = col+moveX[i]
#             if (1 <= next_Y <= N) and (1 <= next_X <= N):
#                 tmp = cost + cost_lst[next_Y][next_X]
#                 if lowest[next_Y][next_X] > tmp:
#                     lowest[next_Y][next_X] = tmp
#                     heapq.heappush(hq, (tmp, next_Y, next_X))
#         if lowest[N][N] != INF:
#             print(f"Problem {cnt}: {lowest[N][N]}")
#             cnt += 1
#             break
