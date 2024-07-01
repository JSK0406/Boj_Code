import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 강의의 수, 블루레이 개수
time_lst = list(map(int, input().split()))

lower = max(time_lst)
upper = 10_000 * 100_000

def check(time, time_lst):
    cnt = 1
    remaing_time = time
    for now_time in time_lst:
        if remaing_time - now_time >= 0:
            remaing_time -= now_time
        else:

            remaing_time = time - now_time
            cnt += 1
    return cnt

while (lower <= upper):
    mid = (lower + upper) // 2
    now_cnt = check(mid, time_lst)

    # 블루레이 용량이 더 필요
    if now_cnt > M:
        lower = mid+1
    # 블루레이 용량이 충분
    else:
        upper = mid-1

print(lower)