import sys
input = sys.stdin.readline
import heapq
INF = 999_999_999  # 문제에 따라 바뀔 수 있음

V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
edge_lst = [[] for _ in range(V+1)]  # 노드가 1번부터 시작이기에 V+1로 처리

for _ in range(E):
    start, end, price = map(int, input().split())  # from, to, price
    edge_lst[start].append((end, price))
    edge_lst[end].append((start, price))

def dijkstra(start_num):
    dist_lst = [INF for _ in range(V+1)]  # 최단 거리를 보관하는 리스트
    hq = []  # 우선 순위 큐 선언, (dist, node_num)의 원소들이 추가될 것
    dist_lst[start_num] = 0  # 출발 노드는 dist = 0
    heapq.heappush(hq, (0, start_num))  # 우선순위 큐에 출발 노드 추가
    visited_lst = [False for _ in range(V+1)]

    while hq:
        dist, now = heapq.heappop(hq)
        visited_lst[now] = True

        for next, price in edge_lst[now]:
            if not visited_lst[next] and dist_lst[next] > dist + price:
                dist_lst[next] = dist + price
                heapq.heappush(hq, (dist_lst[next], next))
            
    return dist_lst

dist_lst = dijkstra(1)
print(dist_lst[V])