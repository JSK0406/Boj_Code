import sys
input = sys.stdin.readline

N = int(input())
fee_Y, fee_M = 0, 0

for fee in list(map(int, input().split())):
    fee_Y += ((fee // 30) + 1) * 10
    fee_M += ((fee // 60) + 1) * 15

result = ['M', fee_M] if fee_M < fee_Y else ['Y', fee_Y] if fee_M > fee_Y else ['Y', 'M', fee_M]
print(*result)