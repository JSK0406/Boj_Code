import sys
input = sys.stdin.readline
import heapq

N = int(input())  # 도시 개수
M = int(input())  # 버스 수

bus_lst = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, p = map(int, input().split())
    bus_lst[s].append((e, p))

start, end = map(int, input().split())

dist_lst = [999_999_999 for _ in range(N+1)]
dist_lst[start] = 0

hq = []
heapq.heappush(hq, (0, start))

while hq:
    now_p, now = heapq.heappop(hq)
    now_lst = bus_lst[now]

    if dist_lst[now] < now_p:
        continue

    for e, p in now_lst:
        next_p = now_p + p
        if next_p < dist_lst[e]:
            heapq.heappush(hq, (next_p, e))
            dist_lst[e] = next_p

print(dist_lst[end])