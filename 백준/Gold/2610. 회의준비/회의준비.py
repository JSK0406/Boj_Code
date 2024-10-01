import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 회의에 참여하는 사람

parent_lst = [i for i in range(N+1)]
edge_lst = [[] for _ in range(N+1)]

def find(n):
    if parent_lst[n] == n:
        return n
    parent_lst[n] = find(parent_lst[n])
    return parent_lst[n]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent_lst[b] = a
    else:
        parent_lst[a] = b

for _ in range(int(input())):
    A, B = map(int, input().split())
    edge_lst[A].append(B)
    edge_lst[B].append(A)
    union(A, B)

for i in range(1, N+1):
    find(i)

info_dict = dict()

for i in range(1, N+1):
    parent = parent_lst[i]
    if parent in info_dict:
        info_dict[parent].append(i)
    else:
        info_dict[parent] = [i]

ans_lst = []

for lst in info_dict.values():
    min_value = sys.maxsize
    min_num = -1
    for start in lst:
        visited_lst = [0 for _ in range(N+1)]
        q = deque([start])
        visited_lst[start] = 1
        while q:
            now_num = q.popleft()
            now_cnt = visited_lst[now_num]
            for next_num in edge_lst[now_num]:
                if not visited_lst[next_num]:
                    visited_lst[next_num] = now_cnt + 1
                    q.append(next_num)
        if min_value > max(visited_lst):
            min_value = max(visited_lst)
            min_num = start
    ans_lst.append(min_num)

print(len(ans_lst))
ans_lst.sort()
for ans in ans_lst: print(ans)