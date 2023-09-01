import sys
input = sys.stdin.readline

ans = 0
for n in bin(int(input())):
    if n == '1':
        ans += 1

print(ans)