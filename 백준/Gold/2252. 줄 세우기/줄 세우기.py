import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())  # 학생 수, 비교한 횟수
lst = [[i, 0, []] for i in range(N+1)]  # 노드마다 인덱스, 연결된 횟수, 연결된 노드 저장 
lst[0][1] = 999_999_999

for _ in range(M):
    a, b = map(int, input().split())  # from, to
    lst[a][2].append(b)
    lst[b][1] += 1

q = deque()
ans = []
for idx, cnt, tmp_lst in lst:
    if not cnt:
        q.append(idx)

while q:
    now = q.popleft()
    ans.append(now)

    idx, cnt, tmp_lst = lst[now]

    for tmp_i in tmp_lst:
        lst[tmp_i][1] -= 1
        if not lst[tmp_i][1]:
            q.append(tmp_i)

print(*ans)