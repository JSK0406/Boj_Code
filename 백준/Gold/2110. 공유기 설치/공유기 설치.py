import sys
input = sys.stdin.readline

# 1 2 4 8 9

# 집 개수, 공유기 개수
N, C = map(int, input().split())
C -= 1
lst = [int(input()) for _ in range(N)]
lst.sort()

lower = 1
upper = 1_000_000_000

while (lower <= upper):
    mid = (lower + upper) // 2
    now_cnt = 0
    now_loc = lst[0]
    for i in lst:
        if i-now_loc >= mid:
            now_cnt += 1
            now_loc = i
    if now_cnt < C:
        upper = mid-1
    else:
        lower = mid+1

print(upper)
