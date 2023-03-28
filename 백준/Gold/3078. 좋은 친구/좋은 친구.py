import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
que_lst = [deque() for _ in range(21)]

cnt = 0
for order in range(N):
    now_len = len(input().strip())
    while que_lst[now_len] and order - que_lst[now_len][0] > K:
        que_lst[now_len].popleft()
    cnt += len(que_lst[now_len])
    que_lst[now_len].append(order)

print(cnt)