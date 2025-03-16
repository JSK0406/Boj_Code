import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())

gift_lst = sorted(list(map(int, input().split())))
for i in range(N):
    gift_lst[i] *= -1
children_lst = list(map(int, input().split()))

heapq.heapify(gift_lst)
hq = gift_lst
c = 0
while c < M:
    now_children = children_lst[c]
    while True:
        if not hq:
            break
        avail = -heapq.heappop(hq)
        if now_children <= avail:
            if avail - now_children > now_children:
                heapq.heappush(hq, -(avail - now_children))
            c += 1
            break
    if not hq:
        break

if not hq and c < M:
    print(0)
else:
    print(1)