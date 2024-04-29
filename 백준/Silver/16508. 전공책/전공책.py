import sys
input = sys.stdin.readline
from collections import Counter
import copy

target = input().strip()
target_counter = Counter(target)

N = int(input())  # 전공책 수

info_lst = []  # 가격, 글자 counter

for _ in range(N):
    A, B = input().strip().split()
    A = int(A)
    info_lst.append((A, Counter(B)))

tot_cnt = 2**N - 1

ans = sys.maxsize
for i in range(1, tot_cnt+1):
    price = 0
    alphas = Counter()
    for j in range(N):
        if (i & 1 << j):
            price += info_lst[j][0]
            alphas += info_lst[j][1]
    
    is_possible = True
    for k in target_counter:
        if k in alphas and target_counter[k] <= alphas[k]:
            pass
        else:
            is_possible = False
            break
    if is_possible:
        ans = min(ans, price)
print(-1 if ans == sys.maxsize else ans)