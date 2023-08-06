import sys

N = int(input())
M = int(input())
S = list(input().strip())

ans = 0
cnt = 0
idx = 1
while idx < M - 1:
    if S[idx] == 'O' and S[idx-1] == 'I' and S[idx + 1] == 'I':
        cnt += 1
        idx += 2
        if cnt >= N:
            ans += 1
    else:
        idx += 1
        cnt = 0

print(ans)