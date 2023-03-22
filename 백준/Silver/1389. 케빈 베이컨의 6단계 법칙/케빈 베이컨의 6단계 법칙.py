import sys
input = sys.stdin.readline
from collections import deque
INF = 9999999999999

N, M = map(int, input().split())

edges = [[0 for _ in range(N+1)] for _ in range(N)]
edges.insert(0, 0)
for _ in range(M):
    A, B = map(int, input().split())
    edges[A][B], edges[B][A] = 1, 1

def bfs(start_node):  # start_node부터 다른 노드들까지의 거리가 모두 정해질 때까지 반복
    queue = deque()
    node_to_node = [0] * (N+1)
    node_to_node.insert(0, 0)
    queue.append((start_node, 0))
    while queue:
        now, distance = queue.popleft()
        for next in range(1, N+1):
            if edges[now][next] and not node_to_node[next]:
                queue.append((next, distance + 1))
                node_to_node[next] = distance + 1
    return sum(node_to_node)


answer, smallest = 0, INF

for bi in range(1, N+1):
    distance_sum = bfs(bi)
    if distance_sum < smallest:
        smallest = distance_sum
        answer = bi

print(answer)