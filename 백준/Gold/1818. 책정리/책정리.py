import sys
input = sys.stdin.readline
import bisect

# 1 5 2 3 4
# X X O O O

# 2 3 4 1 5

# 1 5 4 3 2 => 3번
# X X X X X

# 1 2 3 4 5

# 2 1 4 5 3
# 1 2 3 4 5

# 5 4 3 2 1
# 1 2 3 4 5

N = int(input())
num_lst = list(map(int, input().split()))

dp = [num_lst[0]]
for i in range(1, N):
    now_num = num_lst[i]
    found_idx = bisect.bisect_left(dp, now_num)
    if found_idx == len(dp):
        dp.append(now_num)
    else:
        dp[found_idx] = now_num
print(N-len(dp))