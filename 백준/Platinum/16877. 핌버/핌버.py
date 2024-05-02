import sys
input = sys.stdin.readline

N = int(input())
stone_lst = list(map(int, input().split()))

# pib : 0 1 1 2 3 5 8 13 21 33 54

# 0 : 0
# 1 => 0 : 1
# 2 => 0 1 : 2
# 3 => 0 1 2 : 3
# 4 => 1 2 3 : 0
# 5 => 0 2 3 4 : 1
# 6 => 1 3 4 5 : 2
# 7 => 2 4 5 6 : 3
# 8 => 0 3 5 6 7 : 4
# 9 => 1 4 6 7 8 : 5
# 10 => 2 5 7 8 9 : 0
# 11 => 3 6 8 9 10 : 1
# 12 => 4 7 9 10 11 : 2
# 13 => 0 5 8 10 11 12 : 3
# 14 => 1 6 9 11 12 13 : 0
# 15 => 2 7 10 12 13 14 : 1
# 16 => 3 8 11 13 14 15 : 2
# 17 => 4 9 12 14 15 16 : 3
# 18 => 5 10 13 15 16 17 : 4
# 19 => 6 11 14 16 17 18 : 5
# 20 => 7 12 15 17 18 19 : 0
# 21 => 0 8 13 16 18 19 20 : 1

fib = [0, 1]

idx = 2
while True:
    next_fib = fib[idx-2] + fib[idx-1]
    if next_fib > 3*(10**6):
        break
    fib.append(next_fib)
    idx += 1

dp = [0]

for i in range(1, 3*(10**6)+1):
    grundy_set = set()
    for j in range(1, len(fib)):
        if i - fib[j] >= 0:
            grundy_set.add(dp[i-fib[j]])
        else:
            break
    for n in range(0, i+1):
        if n not in grundy_set:
            dp.append(n)
            break

num = 0

for s in stone_lst:
    num ^= dp[s]
print('cubelover' if num == 0 else 'koosaga')