import sys
input = sys.stdin.readline

N = int(input().strip())
num_lst = list(map(int, input().split()))
num_lst.sort()

ans = 0
for i in range(N):
    ans += (num_lst[i] * pow(2, i)) % 1000000007
    ans -= (num_lst[i] * pow(2, N - 1 - i)) % 1000000007

print(ans % 1_000_000_007)