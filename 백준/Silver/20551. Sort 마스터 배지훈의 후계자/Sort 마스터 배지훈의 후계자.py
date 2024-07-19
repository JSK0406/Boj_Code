import sys
input = sys.stdin.readline
import bisect

N, M = map(int, input().split())

num_lst = [int(input()) for _ in range(N)]
num_lst.sort()

ans_lst = []

for _ in range(M):
    num = int(input())
    idx = bisect.bisect_left(num_lst, num)
    if 0 <= idx < N and num_lst[idx] == num:
        ans_lst.append(idx)
    else:
        ans_lst.append(-1)


for ans in ans_lst:
    print(ans)