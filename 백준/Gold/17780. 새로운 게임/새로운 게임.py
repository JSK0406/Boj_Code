import sys
input = sys.stdin.readline

# 흰색, 빨간색, 파란색
    # 흰색 : 이동 그대로 => 0
    # 빨간색 : 이동하고 이동한 말들 순서 바꾸기 => 1
    # 파란색 : 반대 방향으로 이동, 이동하지 못하면 방향만 반대로 바꿈 => 2

# 말을 옮기면 그 위에 말들도 함께 옮김

# 방향
    # 1: 오
    # 2: 왼
    # 3: 위
    # 4: 아래

# 말이 4개 이상 중복되면 끝남

dir_lst = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

N, K = map(int, input().split())  # 체스판 크기, 말의 개수
map_lst = [list(map(int, input().split())) for _ in range(N)]  # 체스판 상태
status_lst = [[[] for _ in range(N)] for _ in range(N)]  # 말 번호, 방향
cor_dict = dict()  # 현재 좌표

info_lst = []

for i in range(K):
    r, c, d = map(int, input().split())
    status_lst[r-1][c-1].append([i+1, d])
    cor_dict[i+1] = [r-1, c-1]

turn_cnt = 0
is_finish = False
while not is_finish:
    turn_cnt += 1
    if turn_cnt > 1000:
        break
    for idx in range(1, K+1):
        # 본인의 좌표를 cor_dict에서 찾음
        now_row, now_col = cor_dict[idx]
        
        # 본인의 좌표 위치에서 status_lst를 확인해 본인 위에 쌓여있는 말들을 확인
        now_lst = []  # 쌓여있는 말들, 왼쪽에서부터 밑
        
        if status_lst[now_row][now_col][0][0] == idx:
            now_lst += status_lst[now_row][now_col]
            status_lst[now_row][now_col] = []
        else:
            continue

        now_dir = now_lst[0][1]
        nr, nc = dir_lst[now_dir]
        next_row, next_col = now_row + nr, now_col + nc

        if 0 <= next_row < N and 0 <= next_col < N and map_lst[next_row][next_col] != 2:
            pass
        else:
            if now_lst[0][1] == 1:
                now_lst[0][1] = 2
            elif now_lst[0][1] == 2:
                now_lst[0][1] = 1
            elif now_lst[0][1] == 3:
                now_lst[0][1] = 4
            elif now_lst[0][1] == 4:
                now_lst[0][1] = 3
            now_dir = now_lst[0][1]
            nr, nc = dir_lst[now_dir]
            next_row, next_col = now_row + nr, now_col + nc

        if 0 <= next_row < N and 0 <= next_col < N and map_lst[next_row][next_col] == 0:  # 흰색
            status_lst[next_row][next_col] += now_lst
            for ii, di in now_lst:
                cor_dict[ii] = [next_row, next_col]
            if len(status_lst[next_row][next_col]) >= 4:
                is_finish = True

        elif 0 <= next_row < N and 0 <= next_col < N and map_lst[next_row][next_col] == 1:  # 빨간색
            status_lst[next_row][next_col] += reversed(now_lst)
            for ii, di in now_lst:
                cor_dict[ii] = [next_row, next_col]
            if len(status_lst[next_row][next_col]) >= 4:
                is_finish = True
        else:
            status_lst[now_row][now_col] += now_lst
            if len(status_lst[now_row][now_col]) >= 4:
                is_finish = True

print(-1 if turn_cnt >= 1000 else turn_cnt)