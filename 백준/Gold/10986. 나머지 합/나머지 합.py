import sys
from collections import Counter
import math

N, M = map(int, sys.stdin.readline().split())

num_lst = list(map(int, sys.stdin.readline().split()))
sum_lst = [0]
tmp = 0
for i in range(N):
    tmp += num_lst[i]
    sum_lst.append(tmp)

div_lst = [i%M for i in sum_lst]

div_lst = div_lst[1:]

my_dict = dict(Counter(div_lst))

key_lst = list(my_dict.keys())
answer = 0
for i in key_lst:
    if i == 0:
        answer += my_dict[i]
        answer += math.comb(my_dict[i], 2)
    else:
        answer += math.comb(my_dict[i], 2)
print(answer)