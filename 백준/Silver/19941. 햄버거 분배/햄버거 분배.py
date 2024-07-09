import sys
input = sys.stdin.readline

N, K = map(int, input().split())

str_lst = list(input().strip())  # input
visited_lst = [0 for _ in range(N)]

hq = []

ans = 0
for now in range(N):
    # 사람이 햄버거를 먹을 수 있는 수를 카운트
    if str_lst[now] == 'H':
        continue
    for idx in range(max(0, now-K), min(N, now+K+1)):
        if str_lst[idx] == 'H' and visited_lst[idx] == 0:
            visited_lst[idx] = 1
            ans += 1
            break

print(ans)