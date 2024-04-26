import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num_lst = list(map(int, input().split()))
num_set = set(num_lst)

ans = 0
for num in num_lst:
    if num * 2 == M:
        continue
    if M-num in num_set:
        ans += 1

print(ans//2)