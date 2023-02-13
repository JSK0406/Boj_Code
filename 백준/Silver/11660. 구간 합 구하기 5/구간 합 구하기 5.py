import sys

N, M = map(int, sys.stdin.readline().split())

nums = [0]
for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))
    nums[-1].insert(0, 0)

sum_lst = [[0]*(N+1) for _ in range(N)]
sum_lst.insert(0,[0]*(N+1))

for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        tmp+=nums[i][j-1]
        if i == 1:
            sum_lst[i][j] = tmp + nums[i][j]
        else:
            sum_lst[i][j] = tmp + nums[i][j] + sum_lst[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = sum_lst[x2][y2] - sum_lst[x1-1][y2] - sum_lst[x2][y1-1] + sum_lst[x1-1][y1-1]
    # print(sum_lst[y2][x2], sum_lst[y1-1][x2], sum_lst[y2][x1-1], sum_lst[y1-1][x1-1])
    print(answer)