import sys
input = sys.stdin.readline
import heapq

N = int(input())

picked_lst = [int(input()) for _ in range(N)]

hq = []

dasom_cnt = picked_lst[0]
for picked_cnt in picked_lst[1:]:
    heapq.heappush(hq, -picked_cnt)

if N == 1:
    print(0)
else:
    while True:
        poped_cnt = -heapq.heappop(hq)
        if poped_cnt >= dasom_cnt:
            poped_cnt -= 1
            dasom_cnt += 1
        else:
            break
        heapq.heappush(hq, -poped_cnt)

    print(dasom_cnt - picked_lst[0])