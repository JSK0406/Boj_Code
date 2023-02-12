import sys

N, K = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))
sum_lst = [0]
tmp = 0
for i in range(N):
    tmp += temperature[i]
    sum_lst.append(tmp)

answer = None
for i in range(N-K+1):
    if not answer:
        answer = sum_lst[i+K] - sum_lst[i]
    else:
        answer = max(sum_lst[i+K] - sum_lst[i], answer)
print(answer)