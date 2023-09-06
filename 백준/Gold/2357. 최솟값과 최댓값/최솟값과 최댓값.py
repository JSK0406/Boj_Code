import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = [int(input()) for _ in range(N)]
tree = [[0, 0] for _ in range(4*N)]  # min, max

def build(node, left, right):
    global tree
    if left == right:
        tree[node][0] = num_lst[left]
        tree[node][1] = num_lst[left]
        return
    
    mid = (left + right) // 2
    build(2*node, left, mid)
    build(2*node+1, mid+1, right)
    tree[node][0] = min(tree[2*node][0], tree[2*node+1][0])
    tree[node][1] = max(tree[2*node][1], tree[2*node+1][1])

def findMin(node, left, right, L, R):
    global tree
    if L > right or R < left:
        return 999_999_999
    if L <= left and right <= R:
        return tree[node][0]
    mid = (left + right) // 2
    return min(findMin(2*node, left, mid, L, R), findMin(2*node+1, mid+1, right, L, R))

def findMax(node, left, right, L, R):
    global tree
    if L > right or R < left:
        return 0
    if L <= left and right <= R:
        return tree[node][1]
    mid = (left + right) // 2
    return max(findMax(2*node, left, mid, L, R), findMax(2*node+1, mid+1, right, L, R))

build(1, 0, N-1)
for _ in range(M):
    A, B = map(int, input().split())
    print(findMin(1, 0, N-1, A-1, B-1), findMax(1, 0, N-1, A-1, B-1))