import sys
input = sys.stdin.readline

N, M = map(int, input().split())

str_dict = dict()
for _ in range(N):
    now_str = input().strip()
    if len(now_str) >= M:
        if now_str in str_dict:
            str_dict[now_str] += 1
        else:
            str_dict[now_str] = 1

str_lst = list(str_dict.items())

str_lst.sort(key=lambda x:(-x[1], -len(x[0]), x))

for now_str, cnt in str_lst:
    print(now_str)