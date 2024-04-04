import sys
input = sys.stdin.readline
from collections import deque
import itertools


N = int(input())
edge_lst = [list(map(int, input().split())) for _ in range(N)]

two_lst = [set() for _ in range(N)]

for n1 in range(N):
    for n2 in range(N):
        for n3 in range(N):
            if edge_lst[n1][n2] == 1 and edge_lst[n2][n3] == 1:
                two_lst[n1].add(n3)

ans = 0

for n1 in range(N):
    for n2 in two_lst[n1]:
        if n1 == n2:
            continue
        union_set1 = set()
        union_set2 = set()
        for i in range(N):
            if i == n1 or i == n2:
                continue
            if edge_lst[n1][i] == 1:
                union_set1.add(i)
            if edge_lst[n2][i] == 1:
                union_set2.add(i)
        union_set = union_set1.intersection(union_set2)

        ans += len(union_set) * (len(union_set) - 1)

print(ans)