import sys

N = int(sys.stdin.readline().strip())

answer=[-1 for i in range(N)]
lst = list(map(int,sys.stdin.readline().split()))
stack = [0]

for i in range(1,N):
    while stack and lst[stack[-1]]<lst[i]:
        answer[stack.pop()] = lst[i]
    stack.append(i)

print(*answer)

