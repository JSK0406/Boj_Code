import sys
input = sys.stdin.readline

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접에 가장 많은 자리
# 2. 1을 만족하는 경우가 여러 개라면, 인접 칸 중에 비어있는 칸이 가장 많은 칸으로
# 3. 2를 만족하는 경우가 여러 개라면, 행의 번호 가장 작은 칸, 열의 번호 가장 작은 칸

N = int(input())  # 한 변의 길이

favorite_dict = dict()
map_lst = [[0 for _ in range(N)] for _ in range(N)]
order_lst = []

for _ in range(N**2):
    A, B, C, D, E = map(int, input().split())
    favorite_dict[A] = [B, C, D, E]
    order_lst.append(A)

def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

def check_seat(stu):  # stu는 학생 번호
    max_cnt = 0
    empty_cnt = 0
    seat_row, seat_col = 999_999_999, 999_999_999

    for r in range(N):
        for c in range(N):
            if map_lst[r][c] != 0:
                continue
            now_row, now_col = r, c
            fav_cnt = 0
            blank_cnt = 0
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                next_row, next_col = now_row + dr, now_col + dc
                if in_range(next_row, next_col):
                    if map_lst[next_row][next_col] in favorite_dict[stu]:
                        fav_cnt += 1
                    elif map_lst[next_row][next_col] == 0:
                        blank_cnt += 1
            # 좋아하는 학생 가장 많게
            if max_cnt < fav_cnt:
                max_cnt = fav_cnt
                empty_cnt = blank_cnt
                seat_row, seat_col = r, c
            elif max_cnt == fav_cnt:
                # 비어있는 칸이 가장 많은 걸로
                if empty_cnt < blank_cnt:
                    seat_row, seat_col = r, c
                    empty_cnt = blank_cnt
                # 행의 번호 열의 번호는 가장 앞으로 자동으로 설정
                elif empty_cnt == blank_cnt:
                    if seat_row > r:
                        seat_row, seat_col = r, c
                    elif seat_row == r:
                        if seat_col > c:
                            seat_row, seat_col = r, c

    
    return (seat_row, seat_col)

def check_happy():
    cnt = 0
    for r in range(N):
        for c in range(N):
            stu = map_lst[r][c]
            now_row, now_col = r, c
            fav_cnt = 0
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                next_row, next_col = now_row + dr, now_col + dc
                if in_range(next_row, next_col):
                    if map_lst[next_row][next_col] in favorite_dict[stu]:
                        fav_cnt += 1
            if fav_cnt == 1:
                cnt += 1
            elif fav_cnt == 2:
                cnt += 10
            elif fav_cnt == 3:
                cnt += 100
            elif fav_cnt == 4:
                cnt += 1000
    return cnt

for stu in order_lst:
    seat_r, seat_c = check_seat(stu)
    map_lst[seat_r][seat_c] = stu

print(check_happy())