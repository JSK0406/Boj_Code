import sys

sum_lst = []

N, M = map(int, sys.stdin.readline().split())
tmp = 0
num_lst = list(map(int, sys.stdin.readline().split()))
for i in num_lst:
    tmp += i
    sum_lst.append(tmp)
sum_lst.insert(0,0)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    answer = sum_lst[B] - sum_lst[A-1]
    print(answer)