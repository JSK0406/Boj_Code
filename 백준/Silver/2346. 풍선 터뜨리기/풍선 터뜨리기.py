import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
num_lst = list(map(int, input().split()))

q = deque([[num_lst[i], i+1] for i in range(N)])

ans_lst = []

while q:
    now_num, now_idx = q.popleft()
    ans_lst.append(now_idx)
    if not q:
        break
    if now_num < 0:  # popleft후 append
        now_num = -now_num
        for _ in range(now_num):
            q.appendleft(q.pop())
    elif now_num > 0:  # pop한 후 appendleft
        for _ in range(now_num-1):
            q.append(q.popleft())

print(*ans_lst)