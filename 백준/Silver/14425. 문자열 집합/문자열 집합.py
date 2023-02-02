import sys

N, M = map(int,sys.stdin.readline().split())
S = {}
for _ in range(N):
    S[sys.stdin.readline()] = 1

i = 0
for _ in range(M):
    try:
        S[sys.stdin.readline()]
        i+=1
    except:
        pass

print(i)