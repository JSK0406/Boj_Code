import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards_sizes = []

for _ in range(N):
    heapq.heappush(cards_sizes, int(input()))

answer = 0

if N == 1:
    print(answer)
else:
    while len(cards_sizes) > 1:
        tmp = heapq.heappop(cards_sizes) + heapq.heappop(cards_sizes)
        answer += tmp
        heapq.heappush(cards_sizes, tmp)
    print(answer)