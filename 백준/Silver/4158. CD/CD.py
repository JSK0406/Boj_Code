import sys
input = sys.stdin.readline
import bisect

while True:
    N, M = map(int, input().split())

    if (N == 0 and M == 0):
        break

    A_lst = [int(input()) for _ in range(N)]
    B_lst = [int(input()) for _ in range(M)]

    cnt = 0

    for a in A_lst:
        if B_lst[bisect.bisect_left(B_lst, a)] == a:
            cnt += 1

    print(cnt)