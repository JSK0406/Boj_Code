import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
weight_price = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

bags.sort()
heapq.heapify(weight_price)

answer = 0
lst_jewels = []
for bag in bags:
    while weight_price and bag >= weight_price[0][0]:
        heapq.heappush(lst_jewels, -heapq.heappop(weight_price)[1])
    if lst_jewels:
        answer -= heapq.heappop(lst_jewels)

print(answer)