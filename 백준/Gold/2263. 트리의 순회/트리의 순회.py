import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
from collections import deque

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_idx = [0 for _ in range(N+1)]

for i in range(N):
    in_idx[in_order[i]] = i

def pre_order(in_left, in_right, post_left, post_right):
    if (in_left > in_right) or (post_left > post_right):
        return
    
    now_root = post_order[post_right]
    print(now_root, end=' ')

    left_len = in_idx[now_root]-in_left
    right_len = in_right-in_idx[now_root]

    pre_order(in_left, in_left+left_len-1, post_left, post_left+left_len-1)
    pre_order(in_right-right_len+1, in_right, post_right-right_len, post_right-1)


pre_order(0, N-1, 0, N-1)