import sys
import heapq

N, M = map(int, input().split())  # 문제 수, 노드 수

lst = [[i, 0, []] for i in range(N + 1)]  # idx, cnt, 연결된 리스트

for _ in range(M):
    A, B = map(int, input().split())
    lst[B][1] += 1
    lst[A][2].append(B)

hq = []
for idx, cnt, node_lst in lst[1:]:
    if not cnt:
        heapq.heappush(hq, idx)

ans = []
while hq:
    now = heapq.heappop(hq)
    ans.append(now)
    for node in lst[now][2]:
        lst[node][1] -= 1
        if not lst[node][1]:
            heapq.heappush(hq, node)

print(*ans)