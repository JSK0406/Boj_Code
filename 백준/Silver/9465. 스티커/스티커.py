import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    dp1 = [lst1[0], lst1[0]]
    dp2 = [lst2[0], lst2[0]]

    for i in range(1, N):
        dp1[0] = dp1[1]
        dp2[0] = dp2[1]
        dp1[1] = max(dp2[0]+lst1[i], dp1[0])
        dp2[1] = max(dp1[0]+lst2[i], dp2[0])
    print(max(dp1[1], dp2[1]))