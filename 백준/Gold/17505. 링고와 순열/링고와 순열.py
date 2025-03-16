import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())

result_lst = [0 for _ in range(N)]

# (N-1)!보다 크면 안됨

last = N-1
i = 0
for i in range(1, N+1):
    if M - last >= 0:
        result_lst[last] = i
        M -= last
        last -= 1
    else:
        result_lst[M] = i
        M = 0

    if M == 0:
        break

i += 1

for j in range(N):
    if result_lst[j] == 0:
        result_lst[j] = i
        i += 1

if M != 0:
    print(-1)
else:
    print(*result_lst)
