import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())  # 밑, 지수, 나누는 수

def func(mit, jisu):
    if jisu == 1:
        return mit % C
    else:
        next = func(mit, jisu//2)
        if jisu % 2 == 0:
            return next * next % C
        else:
            return next * next * mit % C

print(func(A, B))