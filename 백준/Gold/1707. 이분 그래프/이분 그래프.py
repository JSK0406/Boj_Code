import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    V, E = map(int, input().split())  # 정점 수, 간선 수
    edge_lst = [[] for _ in range(V+1)]
    visited_lst = [0 for _ in range(V+1)]  # 1, 2로 색
    for _ in range(E):
        u, v = map(int, input().split())
        edge_lst[u].append(v)
        edge_lst[v].append(u)

    Flag = True
    for i in range(1, V+1):
        if not visited_lst[i]:
            q = deque()
            q.append(i)
            visited_lst[i] = 1
            while q and Flag:
                now = q.popleft()
                now_status = visited_lst[now]
                for next in edge_lst[now]:
                    if not visited_lst[next]:
                        visited_lst[next] = 2 if now_status == 1 else 1
                        q.append(next)
                    elif now_status != visited_lst[next]:
                        continue
                    else:
                        Flag = False
                        break
        if not Flag:
            break
    print('YES' if Flag else 'NO')