import sys

N, M = map(int,sys.stdin.readline().split())

matrix1 = []
matrix2 = []

for _ in range(N):
    matrix1.append(list(map(int, sys.stdin.readline().split())))

for _ in range(N):
    matrix2.append(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append(matrix1[i][j]+matrix2[i][j])
    result.append(tmp)

for i in result:
    print(*i)