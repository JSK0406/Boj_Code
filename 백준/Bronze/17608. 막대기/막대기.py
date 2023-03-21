import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    stack.append(int(input()))

answer = 0
largest = 0
for i in range(len(stack)-1, -1, -1):
    if largest < stack[i]:
        answer+=1
        largest = stack[i]
    else:
        pass

print(answer)
