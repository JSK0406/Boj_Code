import sys
input = sys.stdin.readline
import math

N = int(input())
num_lst = [1] * (N + 1)
prime_lst = []

for i in range(2, math.ceil(math.sqrt(N)) + 1):
    for j in range(i * 2, N + 1, i):
        num_lst[j] = 0

for i in range(2, N+1):
    if num_lst[i] == 1:
        prime_lst.append(i)

sum_lst = [0]

tmp = 0
for i in prime_lst:
    tmp += i
    sum_lst.append(tmp)

left = 0
right = 0
cnt = 0
# while right < len(sum_lst):
#     if left == right:
#         if sum_lst[left] == N:
#             cnt += 1
#         right += 1
#         continue
#     if sum_lst[right] - sum_lst[left] == N:
#         cnt += 1
#         right += 1
#     else:
#         if sum_lst[right] - num_lst[left] < N:
#             right += 1
#         else:
#             left += 1

while right < len(sum_lst):
    if sum_lst[right] - sum_lst[left] == N:
        cnt += 1
        right += 1
    elif sum_lst[right] - sum_lst[left] < N:
        right += 1
    else:
        left += 1

# print(prime_lst)
# print(sum_lst)
print(cnt)