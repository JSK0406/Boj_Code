import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
lst = [int(input()) for _ in range(N)]
if not N:
    print(0)
else:
    lst.sort()
    num = my_round(N*0.15)
    print(my_round(sum(lst[num:N-num])/(N - 2*num)))