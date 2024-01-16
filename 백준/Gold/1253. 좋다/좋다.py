import sys
input = sys.stdin.readline
import bisect

N = int(input())

lst = list(map(int, input().split()))
lst.sort()
is_good = [0 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        left_idx = bisect.bisect_left(lst, lst[i]+lst[j])
        right_idx = bisect.bisect_right(lst, lst[i]+lst[j])
        if not 0 <= left_idx < N or is_good[left_idx] == 1 :
            continue
        if lst[i]+lst[j] == lst[left_idx]:
            for k in range(left_idx, right_idx):
                if k == i or k == j:
                    continue
                is_good[k] = 1

print(sum(is_good))