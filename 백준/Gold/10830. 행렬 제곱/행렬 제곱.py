import sys
input = sys.stdin.readline

N, B = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

def recur(n):
    if n == 1:
        tmp_lst = []
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append(lst[i][j] % 1000)
            tmp_lst.append(tmp)
        return tmp_lst
    if n == 2:
        return calc(lst, lst)
    calculated = recur(n//2)
    if n % 2 == 0:
        return calc(calculated, calculated)
    else:
        return calc(calc(calculated, calculated), lst)
        
def calc(lst1, lst2):
    calculated_lst = []
    for r in range(N):
        row = lst1[r]
        tmp_lst = []
        for c in range(N):
            col = [lst2[i][c] for i in range(N)]
            tmp_num = sum((row[k] * col[k]) % 1000 for k in range(N)) % 1000
            tmp_lst.append(tmp_num)
        calculated_lst.append(tmp_lst)
    return calculated_lst

for i in recur(B):
    print(*i)