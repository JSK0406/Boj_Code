import sys
input = sys.stdin.readline
import bisect

N = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

ans = sys.maxsize
for idx in range(N):
    num = num_lst[idx]
    found_idx = bisect.bisect_left(num_lst, -num)
    if found_idx - 1 >= 0 and found_idx-1 != idx:
        if abs(ans) > abs(num+num_lst[found_idx-1]):
            ans = num+num_lst[found_idx-1]
    if found_idx + 1 < N and found_idx+1 != idx:
        if abs(ans) > abs(num+num_lst[found_idx+1]):
            ans = num+num_lst[found_idx+1]
    if found_idx < N and found_idx != idx:
        if abs(ans) > abs(num+num_lst[found_idx]):
            ans = num+num_lst[found_idx]

print(ans)