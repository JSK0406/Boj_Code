import sys

n, m = map(int, sys.stdin.readline().split())

def func_2(num):
	i = 2
	result = 0
	while i <= num:
		result += num // i
		i *= 2
	return result

def func_5(num):
	i = 5
	result = 0
	while i <= num:
		result += num // i
		i *= 5
	return result

sum_2 = func_2(n) - func_2(m) - func_2(n-m)
sum_5 = func_5(n) - func_5(m) - func_5(n-m)

print(min(sum_2, sum_5))