import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

lst.sort()
left = 0
right = len(lst)-1
cnt = 0

while left < right:
    tmp = lst[left] + lst[right]
    if tmp < target:
        left += 1
    elif tmp > target:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)