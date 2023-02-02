import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.insert(0,0)
d = [0]*(N+1)

for i in range(1,N+1):
    for j in range(i):
        if lst[i]>lst[j]:
            d[i]=max(d[j]+1,d[i])

max = max(d)
print(max)
answer = []
for i in range(N,0,-1):
    if d[i]==max:
        answer.append(lst[i])
        max-=1
    if max==0:
        break

print(*answer[::-1])