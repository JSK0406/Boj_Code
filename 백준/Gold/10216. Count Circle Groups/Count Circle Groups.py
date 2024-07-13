import sys
input = sys.stdin.readline

parent = []

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(int(input())):
    N = int(input())
    parent = [i for i in range(N+1)]
    info_lst = [list(map(int, input().split())) for _ in range(N)]  # x, y, r
    info_lst.sort(key=lambda x:(x[0], x[1], -x[2]))

    for now_idx in range(N):
        for next_idx in range(N):
            if now_idx == next_idx:
                continue
            now_x, now_y, now_r = info_lst[now_idx][0], info_lst[now_idx][1], info_lst[now_idx][2]
            next_x, next_y, next_r = info_lst[next_idx][0], info_lst[next_idx][1], info_lst[next_idx][2]

            # 겹치는 경우
            if (now_x-next_x) ** 2 + (now_y-next_y) ** 2 <= (now_r+next_r) ** 2:
                union(now_idx, next_idx)
    
    for idx in range(N):
        parent[idx] = find(idx)
    print(len(set(parent))-1)


    # 답에서 0 제외 or 전체에서 -=1