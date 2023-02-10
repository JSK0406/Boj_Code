import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    lst[A].append(B)
    lst[B].append(A)

for i in lst:
    i.sort(reverse=True)

q = deque()
q.append(R)
cnt = 1
while q:
    cur = q.popleft()
    if visit[cur]:
        continue
    for i in lst[cur]:
        q.append(i)
    visit[cur] = cnt
    cnt+=1
            
for i in visit[1:]:
    print(i)