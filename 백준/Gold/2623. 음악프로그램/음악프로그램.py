import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 출연자 수, 보조작가 수

pointed_lst = [[0, []] for _ in range(N+1)]  # 지목된 횟수, 해당 인덱스에 지목한 인덱스

for _ in range(M):
    tmp_lst = list(map(int, input().split()))
    for i in range(1, tmp_lst[0]):
        pointed_lst[tmp_lst[i]][1].append(tmp_lst[i+1])
        pointed_lst[tmp_lst[i+1]][0] += 1

cnt = 0
ans = []
while cnt < N:
    minus_lst = []
    for idx in range(1, N+1):
        pointed_cnt, pointing_lst = pointed_lst[idx]
        if pointed_cnt == 0 and idx not in ans:
            cnt += 1
            ans.append(idx)
            minus_lst += pointing_lst

    if not minus_lst:
        break
    else:
        for i in minus_lst:
            pointed_lst[i][0] -= 1

if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)