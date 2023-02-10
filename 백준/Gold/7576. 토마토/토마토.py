import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#first

q_plus1 = deque()
q_minus1 = deque()


for x in range(N):
    for y in range(M):
        if graph[x][y]==1:
            q_plus1.append((x,y))
        elif graph[x][y]==-1:
            q_minus1.append((x,y))

while q_plus1:
    x,y = q_plus1.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            q_plus1.append((nx,ny))
            graph[nx][ny]=graph[x][y]+1

answer = graph[x][y]

for test in q_minus1:
    x,y = test
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            if graph[nx][ny]==0:
                answer=0
    if answer==0:
        break

print(answer-1)

