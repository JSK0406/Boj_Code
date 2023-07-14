import sys
input = sys.stdin.readline
import itertools
import bisect

def find_res(lst, S):
    return bisect.bisect_right(lst, S) - bisect.bisect_left(lst, S)

N, S = map(int, input().split())  # 정수 개수, 합
num_lst = list(map(int, input().split()))
sum_lst1 = []
sum_lst2 = []

num_lst1 = num_lst[len(num_lst)//2:]
num_lst2 = num_lst[:len(num_lst)//2]

for i in range(1, len(num_lst1) + 1):
    subset = itertools.combinations(num_lst1, i)
    for j in subset:
        sum_lst1.append(sum(j))

for i in range(1, len(num_lst2) + 1):
    subset = itertools.combinations(num_lst2, i)
    for j in subset:
        sum_lst2.append(sum(j))

sum_lst1.sort()
sum_lst2.sort()

cnt = 0
cnt += find_res(sum_lst1, S) + find_res(sum_lst2, S)

for num in sum_lst1:
    find = S - num
    cnt += find_res(sum_lst2, find)

print(cnt)
