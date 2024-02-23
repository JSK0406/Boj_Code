import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parent_lst = [i for i in range(V+1)]

def find(x):
    global parent_lst
    if parent_lst[x] == x:
        return parent_lst[x]
    parent_lst[x] = find(parent_lst[x])
    return parent_lst[x]

def union(x, y):
    global parent_lst
    x, y = find(x), find(y)
    if x < y:
        parent_lst[x] = y
    else:
        parent_lst[y] = x

# edge1, edge2, price
lst = [list(map(int, input().split())) for _ in range(E)]
lst.sort(key=lambda x:x[2])

cnt = 0  # V-1이 되면 스탑

ans = 0
for idx in range(len(lst)):
    if cnt == V-1:
        break
    A, B, C = lst[idx]
    parent_A, parent_B = find(A), find(B)

    if parent_A != parent_B:
        union(A, B)
        ans += C
        cnt += 1

print(ans)
