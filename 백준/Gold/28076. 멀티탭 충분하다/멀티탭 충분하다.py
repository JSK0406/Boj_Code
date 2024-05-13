import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
if N == 1:
    print(lst[0])
elif N == 2:
    print(lst[0]+lst[1]-1)
else:
    if N % 3 == 0:
        print(lst[0]+lst[N//3]+lst[2*(N//3)]-3)
    elif N % 3 == 1:
        print(lst[0]+lst[N//3+1]+lst[2*(N//3)+1]-3)
    elif N % 3 == 2:
        print(lst[0]+lst[N//3+1]+lst[2*(N//3)+2]-3)