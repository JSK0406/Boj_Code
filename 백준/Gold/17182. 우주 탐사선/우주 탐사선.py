import sys
input = sys.stdin.readline
import itertools

# map_lst에서 [i][j]는 i행성에서 j행성까지의 시간

# 모든 행성 탐사
# 중복 방문도 가능

N, K = map(int, input().split())

dist_lst = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            dist_lst[i][j] = min(dist_lst[i][j], dist_lst[i][k] + dist_lst[k][j])

dijk_lst = [sys.maxsize for _ in range(N)]

ans = sys.maxsize
for i in itertools.permutations([i for i in range(N)], N):
    tmp = 0
    if i[0] != K:
        continue
    for j in range(N-1):
        now, next = i[j], i[j+1]
        tmp += dist_lst[now][next]
    ans = min(ans, tmp)

print(ans)