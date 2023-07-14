import sys
import bisect
from collections import deque
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

dp = [num_lst[0]]
length_lst = [1]  # 해당 인덱스의 dp에서의 idx

max_length = 1
for i in range(1, N):
    if dp[-1] < num_lst[i]:
        dp.append(num_lst[i])
        max_length += 1
        length_lst.append(max_length)
    else:
        idx = bisect.bisect_left(dp, num_lst[i])
        dp[idx] = num_lst[i]
        length_lst.append(idx + 1)

q = deque()

for i in range(len(length_lst) - 1, -1, -1):
    if length_lst[i] == max_length:
        q.appendleft(num_lst[i])
        max_length -= 1
    if max_length == 0:
        break

print(len(dp))
print(*list(q))