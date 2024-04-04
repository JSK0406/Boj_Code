import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent_lst[x] == x:
        return x
    p = find(parent_lst[x])
    weight_lst[x] += weight_lst[parent_lst[x]]
    parent_lst[x] = p
    return p

def union(x, y, w):
    px = find(x)
    py = find(y)

    if px == py:
        return
    
    weight_lst[py] = weight_lst[x] - weight_lst[y] + w
    parent_lst[py] = px
    return

while True:
    N, M = map(int, input().split())  # 샘플 개수, 일한 수
    
    # 종료 조건
    if N == 0 and M == 0:
        break

    parent_lst = [i for i in range(N+1)]
    weight_lst = [0 for _ in range(N+1)]
    for _ in range(M):
        tmp_lst = input().strip().split()
        question = tmp_lst[0]
        
        # 측정
        if question == '!':
            light, heavy, amount = map(int, tmp_lst[1:])
            union(light, heavy, amount)
        
        if question == '?':
            A, B = map(int, tmp_lst[1:])
            if find(A) != find(B):
                print('UNKNOWN')
            else:
                print(weight_lst[B] - weight_lst[A])