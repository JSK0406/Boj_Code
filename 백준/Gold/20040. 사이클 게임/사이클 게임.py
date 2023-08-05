import sys
input = sys.stdin.readline

def parent_find(N):
    if parent_lst[N] == N:
        return N
    else:
        return parent_find(parent_lst[N])

n, m = map(int, (input().split()))  # 수의 개수, 입력 개수

parent_lst = [i for i in range(n)]

edge_lst = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    A, B = edge_lst[i]
    A_parent = parent_find(A)
    B_parent = parent_find(B)

    if A_parent == B_parent:
        print(i+1)
        break
    if A_parent > B_parent:
        parent_lst[A_parent] = B_parent
    else:
        parent_lst[B_parent] = A_parent
else:
    print(0)