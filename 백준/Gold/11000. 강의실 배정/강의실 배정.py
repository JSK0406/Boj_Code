import sys
input = sys.stdin.readline
import heapq

N = int(input())

hq = []
class_room = []

for _ in range(N):
    S, T = map(int, input().split())
    heapq.heappush(hq, [S, T])

ans = 0
while hq:
    S, T = heapq.heappop(hq)
    if not class_room:
        heapq.heappush(class_room, T)
        ans += 1
        continue
    if class_room[0] <= S:
        heapq.heappop(class_room)
        heapq.heappush(class_room, T)
    else:
        heapq.heappush(class_room, T)
        ans += 1

print(ans)