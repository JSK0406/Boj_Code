import sys
input = sys.stdin.readline

N = int(input())
bin_N = bin(N)[2:]

exp = 0
ans = 0
for i in range(len(bin_N) - 1, -1, -1):
    if bin_N[i] == '1':
        ans += 3 ** exp
    exp += 1
    
print(ans)