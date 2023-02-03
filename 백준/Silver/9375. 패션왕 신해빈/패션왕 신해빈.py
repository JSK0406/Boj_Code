import sys

n = int(sys.stdin.readline())
for _ in range(n):
	N = int(sys.stdin.readline())
	dic = {}
	for _ in range(N):
		inp = sys.stdin.readline().split()[1]
		if inp in dic.keys():
			dic[inp] += 1
		else:
			dic[inp] = 1
	lst = list(dic.values())
	result = 1
	for i in lst:
		result *= i+1
	print(result - 1)