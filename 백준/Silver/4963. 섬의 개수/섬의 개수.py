import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y,graph):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            graph[nx][ny]=0
            dfs(nx,ny,graph)


while True:
    w,h = map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    answer = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for x in range(h):
        for y in range(w):
            if graph[x][y]==1:
                graph[x][y]=0
                dfs(x,y,graph)
                answer+=1
    print(answer)

