import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 신맛, 쓴맛

ans = abs(lst[0][0] - lst[0][1])
for i in range(1, 1 << N):
    sour, bitter = 1, 0
    for j in range(N):
        if i & (1 << j):
            sour *= lst[j][0]
            bitter += lst[j][1]
    ans = min(ans, abs(sour - bitter))
print(ans)