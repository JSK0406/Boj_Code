import sys
input = sys.stdin.readline

N = int(input())

left = 0
right = 2 ** 33

while left <= right:
    mid = (left + right) // 2
    mid_pow = mid ** 2
    if mid_pow < N:
        left = mid+1
    else:
        right = mid-1

print(left)