import sys
input = sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]

answer = 0
largest = 0
for i in range(len(stack)-1, -1, -1):
    if largest < stack[i]:
        answer+=1
        largest = stack[i]
    else:
        pass

print(answer)
