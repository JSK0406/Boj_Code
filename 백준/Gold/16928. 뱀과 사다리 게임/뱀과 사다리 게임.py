import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
sqaure_lst = [i for i in range(101)]
visited_lst = [0 for _ in range(101)]

for _ in range(N+M):
    A, B = map(int, input().split())
    sqaure_lst[A] = B

q = deque()
q.append(1)

while not visited_lst[100]:
    now = q.popleft()
    for i in range(1, 7):
        next_idx = now + i
        now_cnt = visited_lst[now]
        if 1 <= next_idx < 101:
            next = sqaure_lst[next_idx]
            if not visited_lst[next]:
                visited_lst[next] = now_cnt + 1
                q.append(next)

print(visited_lst[100])