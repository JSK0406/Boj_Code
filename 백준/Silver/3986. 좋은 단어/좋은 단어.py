import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    for letter in input().strip():
        stack.append(letter)
        try:
            while stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        except:
            pass

    if not stack:
        cnt += 1

print(cnt)