import sys
input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort(reverse=True)

minus = 0

ans = 0
for num in lst:
    if num <= minus:
        break
    ans += num - minus
    minus += 1
print(ans)