import sys
input = sys.stdin.readline
from collections import deque

A_lst = list(map(int, input().strip()))
B_lst = list(map(int, input().strip()))
C_lst = list(map(int, input().strip()))
D_lst = list(map(int, input().strip()))

rotate_cnt = int(input())

A_left, A_right = 6, 2
B_left, B_right = 6, 2
C_left, C_right = 6, 2
D_left, D_right = 6, 2

for _ in range(rotate_cnt):
    num, dir = map(int, input().split())
    A_dir, B_dir, C_dir, D_dir = 0, 0, 0, 0
    if (num == 1):
        A_dir = dir
        if (A_lst[A_right] != B_lst[B_left]):
            B_dir = -A_dir
        if (B_dir and B_lst[B_right] != C_lst[C_left]):
            C_dir = -B_dir
        if (C_dir and C_lst[C_right] != D_lst[D_left]):
            D_dir = -C_dir
    if (num == 2):
        B_dir = dir
        if (B_lst[B_left] != A_lst[A_right]):
            A_dir = -B_dir
        if (C_lst[C_left] != B_lst[B_right]):
            C_dir = -B_dir
        if (C_dir and C_lst[C_right] != D_lst[D_left]):
            D_dir = -C_dir
    if (num == 3):
        C_dir = dir
        if (C_lst[C_left] != B_lst[B_right]):
            B_dir = -C_dir
        if (D_lst[D_left] != C_lst[C_right]):
            D_dir = -C_dir
        if (B_dir and A_lst[A_right] != B_lst[B_left]):
            A_dir = -B_dir
    if (num == 4):
        D_dir = dir
        if (C_lst[C_right] != D_lst[D_left]):
            C_dir = -D_dir
        if (C_dir and B_lst[B_right] != C_lst[C_left]):
            B_dir = -C_dir
        if (B_dir and A_lst[A_right] != B_lst[B_left]):
            A_dir = -B_dir
    A_left -= A_dir
    A_right -= A_dir
    B_left -= B_dir
    B_right -= B_dir
    C_left -= C_dir
    C_right -= C_dir
    D_left -= D_dir
    D_right -= D_dir
    if A_left == 8:
        A_left = 0
    if A_left == -1:
        A_left = 7
    if B_left == 8:
        B_left = 0
    if B_left == -1:
        B_left = 7
    if C_left == 8:
        C_left = 0
    if C_left == -1:
        C_left = 7
    if D_left == 8:
        D_left = 0
    if D_left == -1:
        D_left = 7
    if A_right == 8:
        A_right = 0
    if A_right == -1:
        A_right = 7
    if B_right == 8:
        B_right = 0
    if B_right == -1:
        B_right = 7
    if C_right == 8:
        C_right = 0
    if C_right == -1:
        C_right = 7
    if D_right == 8:
        D_right = 0
    if D_right == -1:
        D_right = 7

A_up = A_right + 6 if A_right - 2 < 0 else A_right - 2
B_up = B_right + 6 if B_right - 2 < 0 else B_right - 2
C_up = C_right + 6 if C_right - 2 < 0 else C_right - 2
D_up = D_right + 6 if D_right - 2 < 0 else D_right - 2
# print(A_lst[A_up])
# print(B_lst[B_up])
# print(C_lst[C_up])
# print(D_lst[D_up])

print(A_lst[A_up] * 1 + B_lst[B_up] * 2 + C_lst[C_up] * 4 + D_lst[D_up] * 8)