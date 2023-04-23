import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[set(), set()] for _ in range(N+1)]
# 작은 것 0번째, 큰 것 1번째
for _ in range(M):
    smaller, taller = map(int, input().split())
    graph[smaller][1].add(taller)
    graph[taller][0].add(smaller)  

answer = 0

for Ni in range(N+1):
    for si in graph[Ni][0]:  # smaller보다 작은 사람은 taller보다도 작다
        graph[Ni][0] = graph[Ni][0].union(graph[si][0])
    for ti in graph[Ni][1]:   # taller보다 큰 사람은 smaller에게도 크다
        graph[Ni][1] = graph[Ni][1].union(graph[ti][1])

for Ni in range(N, -1, -1):
    cnt = 0
    for si in graph[Ni][0]:  # smaller보다 작은 사람은 taller보다도 작다
        graph[Ni][0] = graph[Ni][0].union(graph[si][0])
    for ti in graph[Ni][1]:   # taller보다 큰 사람은 smaller에게도 크다
        graph[Ni][1] = graph[Ni][1].union(graph[ti][1])
    if (len(graph[Ni][0]) + len(graph[Ni][1])) == N-1:
        answer += 1

print(answer)