import sys
import bisect
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

dp = [num_lst[0]]


for i in range(1, N):
    if num_lst[i] > dp[-1]:
        dp.append(num_lst[i])
    else:
        idx = bisect.bisect_left(dp, num_lst[i])
        dp[idx] = num_lst[i]

print(len(dp))