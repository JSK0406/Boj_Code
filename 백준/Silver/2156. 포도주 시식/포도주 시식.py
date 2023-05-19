import sys

N = int(sys.stdin.readline())

grapes = [0]*10001
for i in range(N):
    grapes[i+1] = int(sys.stdin.readline())

d = [0]*10001
d[1]=grapes[1]
d[2]=grapes[1]+grapes[2]

if N>=3:
    for i in range(3,N+1):
        d[i]=max(d[i-2]+grapes[i],d[i-3]+grapes[i-1]+grapes[i],d[i-4]+grapes[i-1]+grapes[i])

print(max(d))