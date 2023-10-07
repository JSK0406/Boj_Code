import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq_left = []  # - 붙여서
hq_right = []  # 그대로
for _ in range(N):
    num = int(input())

    if len(hq_left) == len(hq_right):
        heapq.heappush(hq_left, (-num, num))
    else:
        heapq.heappush(hq_right, (num, num))

    if hq_right and hq_left[0][1] > hq_right[0][1]:
        left_pop = heapq.heappop(hq_left)[1]
        right_pop = heapq.heappop(hq_right)[1]
        heapq.heappush(hq_left, (-right_pop, right_pop))
        heapq.heappush(hq_right, (left_pop, left_pop))
    print(hq_left[0][1])