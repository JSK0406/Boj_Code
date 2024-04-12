import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

left, right = 0, min(times) * M

while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for time in times:
        cnt += mid // time
    
    if cnt < M:
        left = mid + 1
    else:
        right = mid - 1

print(left)