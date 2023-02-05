import sys

N, K = map(int, sys.stdin.readline().split())

lst = [i for i in range(1,N+1)]
order = K-1
answer = []

for i in range(N):
    answer.append(str(lst.pop(order)))
    for i in range(K-1):
        if len(lst)<=order:
            order = 0
        order +=1
        if len(lst)<=order:
            order = 0

print('<'+', '.join(answer)+'>')