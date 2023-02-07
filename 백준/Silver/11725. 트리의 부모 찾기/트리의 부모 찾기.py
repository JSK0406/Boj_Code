import sys

N = int(sys.stdin.readline())
lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    lst[A].append(B)
    lst[B].append(A)

answer = [0 for _ in range(N+1)]

q = [1]
while q:
    tmp = q.pop(0)
    for i in lst[tmp]:
        if answer[i] == 0:
            answer[i] = tmp
            q.append(i)

for i in answer[2:]:
    print(i)