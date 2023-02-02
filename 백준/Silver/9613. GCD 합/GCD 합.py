import sys

N = int(sys.stdin.readline().rstrip('\n'))

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b:
        tmp = b
        b = a%b
        a = tmp

    return a
for i in range(N):
    answer = 0
    lst = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(lst)):
        for k in range(j+1,len(lst)):
            answer += gcd(lst[j],lst[k])
    print(answer)