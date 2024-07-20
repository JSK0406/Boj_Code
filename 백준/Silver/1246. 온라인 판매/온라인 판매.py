import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 달걀 수, 고객 수

price_lst = [int(input()) for _ in range(M)]
price_lst.sort(reverse=True)

ans_ben = 0
ans_pri = 0
for i in range(M):
    if i+1 > N:
        break
    if ans_ben < price_lst[i] * (i+1):
        ans_ben = price_lst[i] * (i+1)
        ans_pri = price_lst[i]

print(ans_pri, ans_ben)
