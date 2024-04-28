import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

num = num_lst[0]

if len(num_lst) > 1:
    for n in num_lst[1:]:
        num ^= n
    if num == 0:
        print('cubelover')
    else:
        print('koosaga')
else:
    print('koosaga')