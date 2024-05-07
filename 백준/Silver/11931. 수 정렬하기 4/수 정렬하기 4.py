import sys
input = sys.stdin.readline

N = int(input())
num_lst = [int(input()) for _ in range(N)]
num_lst.sort(reverse=True)

for n in num_lst:
    print(n)