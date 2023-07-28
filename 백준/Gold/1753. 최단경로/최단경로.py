import sys
input = sys.stdin.readline
import heapq
INF = 999_999_999

V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
start_node = int(input())
edge_dict = dict()  # 저장되는 데이터 [도착지점, 비용]
lst = [INF for _ in range(V + 1)]
lst[start_node] = 0

for _ in range(E):  # 딕셔너리에 edge 추가
    start, end, price = map(int, input().split())
    try:
        edge_dict[start].append((price, end))
    except:
        edge_dict[start] = [(price, end)]

hq = []
heapq.heappush(hq, (0, start_node))

while hq:
    distance, now_node = heapq.heappop(hq)
    try:
        now_edgelst = edge_dict[now_node]
        if lst[now_node] < distance:
            continue
        for d, n in now_edgelst:
            next_price = distance + d
            if next_price < lst[n]:
                lst[n] = next_price
                heapq.heappush(hq, (next_price, n))
    except:
        continue

for i in range(1, V + 1):
    if lst[i] == INF:
        print("INF")
        continue
    print(lst[i])