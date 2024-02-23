import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())  # 과목 수, 선수 조건 수

in_orders = [0 for _ in range(N+1)]  # 들어오는 리스트 => A->B라면 B들
edge_lst = [[] for _ in range(N+1)]  # A에서 B로 연결되었다면 => [A]에 B가 저장
visited_lst = [0 for _ in range(N+1)]  # 해당 노드를 몇번째에 방문

for _ in range(M):
    A, B = map(int, input().split())
    in_orders[B] += 1
    edge_lst[A].append(B)

q = deque()
for idx in range(1, N+1):
    # 이전의 노드들이 모두 처리 됐고, 방문을 하지 않았으면
    if in_orders[idx] == 0 and not visited_lst[idx]:
        visited_lst[idx] = 1
        q.append(idx)

while q:
    now_idx = q.popleft()
    for next_idx in edge_lst[now_idx]:
        # 현재 노드를 고려했으니 in_orders의 다음 인덱스에서 1을 뺀다
        in_orders[next_idx] -= 1
        # 0이 되었다면 q에 넣는다, 방문 확인
        if in_orders[next_idx] == 0 and not visited_lst[next_idx]:
            # 방문처리한 후 q에 삽입
            visited_lst[next_idx] = visited_lst[now_idx] + 1
            q.append(next_idx)

print(*visited_lst[1:])


