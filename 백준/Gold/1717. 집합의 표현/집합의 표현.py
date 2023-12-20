import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def find(x):
    if root_arr[x] < 0:
        return x
    root_arr[x] = find(root_arr[x])
    return root_arr[x]

def union(x, y):
    x, y = find(x), find(y)
    
    if x == y:
        return
    
    if root_arr[x] < root_arr[y]:
        root_arr[x] += root_arr[y]
        root_arr[y] = x
    else:
        root_arr[y] += root_arr[x]
        root_arr[x] = y

n, m = map(int, input().split())
root_arr = [-1] * (n + 1)

for _ in range(m):
    comm, a, b = map(int, input().split())
    if comm == 0:
        union(a, b)
    elif comm == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
