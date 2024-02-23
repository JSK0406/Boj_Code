import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
if not N:
    print(0)
else:
    lst.sort()
    num = round((N*0.15)+0.0000000000001)
    print(round((sum(lst[num:N-num])/(N - 2*num))+0.0000000000001))