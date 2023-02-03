import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

def gcd(A, B):
	A, B = max(A, B), min(A, B)
	tmp = 1
	while tmp != 0:
		tmp = A % B
		A = B
		B = tmp
		if A == 1:
			return 1
			break
	return A

first = lst[0]
for num in lst[1:]:
	tmp = gcd(first, num)
	print(first//tmp, "/", num//tmp, sep='')
