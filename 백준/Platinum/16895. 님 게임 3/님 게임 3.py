import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

whole_nim = 0
for n in num_lst:
    whole_nim ^= n

ans = 0
for i in range(N):
    for j in range(1, num_lst[i]+1):
        num = num_lst[i] - j
        num ^= num_lst[i]
        num ^= whole_nim
        if num == 0:
            ans += 1

print(ans)