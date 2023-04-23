import sys

N, M = map(int,sys.stdin.readline().split())

lst = []

def solution():
    if len(lst)==M:
        print(*lst)
        return
    for i in range(1,N+1):
        if i not in lst:
            lst.append(i)
            solution()
            lst.pop()

solution()