import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()
q.append(([N], 0))
visited = [0] * (N+1)

if N == 1:
    print(0)
    print(1)
else:
    while q:
        nums, cnt = q.popleft()
        last_num = nums[-1]
        next_num1, next_num2, next_num3 = 0, 0, 0
        if not last_num % 3:
            next_num1 = last_num // 3
            if next_num1 == 1:
                print(cnt + 1)
                print(*nums, next_num1)
                break
        if not last_num % 2:
            next_num2 = last_num // 2
            if next_num2 == 1:
                print(cnt + 1)
                print(*nums, next_num2)
                break
        next_num3 = last_num- 1
        if next_num1 == 1:
            print(cnt + 1)
            print(*nums, next_num3)
            break
        if next_num1 and not visited[next_num1]:
            q.append((nums+[next_num1], cnt + 1))
            visited[next_num1] = 1
        if next_num2 and not visited[next_num2]:
            q.append((nums+[next_num2], cnt + 1))
            visited[next_num2] = 1
        if next_num3 and not visited[next_num3]:
            q.append((nums+[next_num3], cnt + 1))
            visited[next_num3] = 1