import sys
input = sys.stdin.readline
import math

# 1 : 0 1 : 1
# 2 : 1 0 : 1
# 3 : 1 1 : 2
# 4 : 1 0 0 : 1
# 5 : 1 0 1 : 2
# 6 : 1 1 0 : 2
# 7 : 1 1 1 : 3
# 8 : 1 0 0 0 : 1
# 9 : 1 0 0 1 : 2
# 10 : 1 0 1 0 : 2
# 11 : 1 0 1 1 : 3
# 12 : 1 1 0 0 : 2
# 13 : 1 1 0 1 : 3
# 14 : 1 1 1 0 : 3
# 15 : 1 1 1 1 : 4
# 16 : 1 0 0 0 0 : 1

# 1 : 0
# 2 ~ 3 : (3-2+1) + 1 * 1C1
# 4 ~ 7 : (7-4+1) + 2 * 2C2 + 1 * 2C1 : 4
# 8 ~ 15 : (15-8+1) + 3 * 3C3 + 2 * 3C2 + 1 * 3C1 => 3 + 6 + 3 : 12 = 3 * 4 => 3승에서 4승전까지
# 16 ~ 31 : (31-16+1) + 4 * 4C4 + 3 * 4C3 + 2 * 4C2 + 1 * 4C1 => 4 + 12 + 12 + 4 : 32 = 4 * 8
# 32 ~ 63 : (63-32+1) + 5 * 5C5 + 4 * 5C4 + 3 * 5C3 + 2 * 5C2 + 1 * 5C1 => 5 + 20 + 30 + 20 + 5 : 80 = 5 * 16
# 64 ~ 127 : 6 * 6C6 + 5 * 6C5 + 4 * 6C4 + 3 * 6C3 + 2 * 6C2 + 1 * 6C1 => 6 + 30 + 60 + 60 + 30 + 6 : 192 = 6 * 32

lst = [0 for _ in range(55)]
for i in range(1, 55):
    lst[i] = lst[i-1] + i*2**(i-1)

A, B = map(int, input().split())
A -= 1
B_cnt = 0

while True:
    if B == 1:
        B_cnt += 1
        break
    if B == 0:
        break
    B_cnt += lst[B.bit_length()-2] + B
    B = B - (2 ** (B.bit_length()-1))

A_cnt = 0

while True:
    if A == 1:
        A_cnt += 1
        break
    if A == 0:
        break
    A_cnt += lst[A.bit_length()-2] + A
    A = A - (2 ** (A.bit_length()-1))
print(B_cnt-A_cnt)