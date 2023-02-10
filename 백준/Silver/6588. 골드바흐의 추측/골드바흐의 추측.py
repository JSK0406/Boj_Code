import sys
import math

num_lst = []
while True:
    num = int(sys.stdin.readline())
    if not num:
        break
    else:
        num_lst.append(num)


def func(n):
    tmp_lst = [True]*(n+1)
    tmp_lst[0] = False
    for i in range(2, int(math.sqrt(n))+1):
        if tmp_lst[i]:
            for j in range(2*i, n+1, i):
                tmp_lst[j] = False

    return tmp_lst

prime_lst = func(1000005)

for i in num_lst:
    for j in range(3, i):
        if prime_lst[j] and prime_lst[i-j]:
            print(f'{i} = {j} + {i-j}')
            break