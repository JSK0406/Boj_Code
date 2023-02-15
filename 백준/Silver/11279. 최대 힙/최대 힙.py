import sys
import heapq

heap = []  # heap 자료구조는 리스트로 선언하고 작업을 heapq function을 통해 구현
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (-num, num))  # 기본적으로 heappop은 최솟값을 리턴하기에 최소값을 리턴하기 위해서는 튜플 형태로 push