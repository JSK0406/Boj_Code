import sys

N = int(input())
map_lst = [list(input()) for _ in range(N)]

loc = 0
answer = 0

for y in range(N):
    for x in range(N):
        if map_lst[y][x] == '.':
            tmp_ans = 0
            for dy, dx in [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]:
                ny, nx = y+dy, x+dx
                i = 0
                while 0 <= ny < N and 0 <= nx < N and map_lst[ny][nx] == 'W':
                    ny += dy
                    nx += dx
                    i += 1
                if nx == N or nx == -1 or ny == N or ny == -1:
                    pass
                elif map_lst[ny][nx] == 'B':
                    tmp_ans += i
            if answer < tmp_ans:
                loc = (x, y)
                answer = tmp_ans

if answer:
    print(*loc)
    print(answer)
else:
    print('PASS')