import sys

A, B = map(int, sys.stdin.readline().split())

dp = [1] * (A + 1)

for i in range(A):
	dp[i+1] *= dp[i] * (i+1)

print((dp[A] // dp[B] // dp[A - B]) % 10007)