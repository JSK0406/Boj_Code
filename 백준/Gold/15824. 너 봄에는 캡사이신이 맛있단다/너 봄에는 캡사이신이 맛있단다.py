import sys
input = sys.stdin.readline

N = int(input().strip())
num_lst = list(map(int, input().split()))
num_lst.sort()

def num_pow(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if not n % 2:
        return (num_pow(n//2) ** 2) % 1_000_000_007
    else:
        return (num_pow(n//2) ** 2 * 2) % 1_000_000_007

ans = 0
for i in range(N):
    ans += (num_lst[i] * num_pow(i)) % 1000000007
    ans -= (num_lst[i] * num_pow(N - 1 - i)) % 1000000007

print(ans % 1_000_000_007)