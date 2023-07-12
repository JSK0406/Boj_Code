import sys
from collections import deque
input = sys.stdin.readline

T = int(input())  # 테스트케이스 개수

for _ in range(T):
    N, K = map(int, input().split())  # 건물 개수, 규칙 개수
    building_time_lst = list(map(int, input().split()))
    building_time_lst.insert(0, None)

    cnt_nodes_lst = [[i, 0, []] for i in range(1, N+1)]  # (인덱스 번호, 연결된 노드 개수, 해당 인덱스의 다음 건물)
    cnt_nodes_lst.insert(0, None)
    for _ in range(K):
        a, b = map(int, input().split())
        cnt_nodes_lst[a][2].append(b)
        cnt_nodes_lst[b][1] += 1
    W = int(input())  # 목표 건물

    cunstrcted_lst = [0 for _ in range(N)]
    cunstrcted_lst.insert(0, None)
    q = deque()
    for idx, cnt, nodes in cnt_nodes_lst[1:]:
        if not cnt:
            q.append(idx)
            cunstrcted_lst[idx] = building_time_lst[idx]

    while q:
        now = q.popleft()
        idx, cnt, nodes = cnt_nodes_lst[now]
        for next in nodes:
            cnt_nodes_lst[next][1] -= 1
            cunstrcted_lst[next] = max(cunstrcted_lst[next], cunstrcted_lst[now] + building_time_lst[next])
            if not cnt_nodes_lst[next][1]:
                q.append(next)
        if not cnt_nodes_lst[W][1]:
            print(cunstrcted_lst[W])
            break      