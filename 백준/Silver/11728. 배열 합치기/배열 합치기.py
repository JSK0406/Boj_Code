import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
A_que = deque()
B_que = deque()
A_lst = list(map(int, input().split()))
A_que += A_lst
B_lst = list(map(int, input().split()))
B_que += B_lst

ans_lst = []

while (A_que and B_que):
    if A_que[0] < B_que[0]:
        ans_lst.append(A_que.popleft())
    else:
        ans_lst.append(B_que.popleft())

ans_lst += A_que + B_que

print(*ans_lst)