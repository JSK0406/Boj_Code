import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
left_house = lst[N//2-1]
left_sum = 0
right_house = lst[N//2]
right_sum = 0

for i in lst:
    left_sum += abs(left_house-i)

for i in lst:
    right_sum += abs(right_house-i)

print(left_house if left_sum <= right_sum else right_house)