import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())

for _ in range(T):
    now_str = list(input().strip())
    K = int(input())

    str_cnt = [0 for _ in range(122-97)]

    str_dict = defaultdict(list)

    for idx in range(len(now_str)):
        s = now_str[idx]
        str_dict[s].append(idx)

    short_ans, long_ans = 999_999_999, 0

    for alpha, idx_lst in str_dict.items():
        if len(idx_lst) < K:
            continue
        for i in range(len(idx_lst)-K+1):
            short_ans = min(short_ans, idx_lst[i+K-1]-idx_lst[i]+1)
            long_ans = max(long_ans, idx_lst[i+K-1]-idx_lst[i]+1)

    if short_ans == 999_999_999 and long_ans == 0:
        print(-1)
    else:
        print(short_ans, long_ans)

