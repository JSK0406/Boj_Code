import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    dp10, dp11 = lst1[0], lst1[0]
    dp20, dp21 = lst2[0], lst2[0]

    for i in range(1, N):
        dp10 = dp11
        dp20 = dp21
        dp11 = max(dp20+lst1[i], dp10)
        dp21 = max(dp10+lst2[i], dp20)
    print(max(dp11, dp21))