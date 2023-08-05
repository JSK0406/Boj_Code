import sys
input = sys.stdin.readline

N = int(input())

x_lst = []
y_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

x_lst.append(x_lst[0])
y_lst.append(y_lst[0])

ans = 0
for i in range(N):
    ans += x_lst[i] * y_lst[i + 1]

for i in range(N):
    ans -= y_lst[i] * x_lst[i + 1]

print(round(abs(ans) / 2, 1))