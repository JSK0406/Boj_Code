import sys
input = sys.stdin.readline

N = int(input())  # 한 변의 길이

paper_lst = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0

def inner_func(mode, next_N, now_lst):
    global white_cnt
    global blue_cnt
    inner_lst = []
    cnt = 0
    if mode == "upper_left":
        A, B, C, D = 0, next_N, 0, next_N
    elif mode == "upper_right":
        A, B, C, D = 0, next_N, next_N, next_N * 2
    elif mode == "lower_left":
        A, B, C, D = next_N, next_N * 2, 0, next_N
    elif mode == "lower_right":
        A, B, C, D = next_N, next_N * 2, next_N, next_N * 2
    for r in range(A, B):
        tmp_lst = []
        for c in range(C, D):
            now = now_lst[r][c]
            cnt += now
            tmp_lst.append(now)
        inner_lst.append(tmp_lst)
    if cnt == 0:
        white_cnt += 1
        return
    elif cnt == next_N * next_N:
        blue_cnt += 1
        return
    else:
        recur(next_N, inner_lst)

def recur(N, now_lst):
    global blue_cnt
    global white_cnt
    next_N = N // 2
    tmp_sum = 0
    for i in now_lst:
        tmp_sum += sum(i)
    if tmp_sum == N * N:
        blue_cnt += 1
        return
    elif tmp_sum == 0:
        white_cnt += 1
        return
    inner_func("upper_left", next_N, now_lst)
    inner_func("upper_right", next_N, now_lst)
    inner_func("lower_left", next_N, now_lst)
    inner_func("lower_right", next_N, now_lst)


recur(N, paper_lst)

print(white_cnt)
print(blue_cnt)