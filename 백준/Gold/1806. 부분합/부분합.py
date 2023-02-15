import sys

N, S = map(int, sys.stdin.readline().split())

num_lst = list(map(int, sys.stdin.readline().split()))
sum_lst = [0]

sum_tmp = 0
for i in num_lst:
    sum_tmp += i
    sum_lst.append(sum_tmp)

left = 0
right = 0
minimum = 999999999

while right <= N:
    if sum_lst[right] - sum_lst[left] >= S:
        minimum = min(right-left, minimum) 
        left += 1
    else:
        right += 1
if minimum == 999999999:
    print(0)
else:
    print(minimum)

