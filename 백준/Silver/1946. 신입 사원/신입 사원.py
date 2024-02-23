import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    rank_lst = [list(map(int, input().split())) for _ in range(N)]
    rank_lst.sort(key=lambda x:(x[0]))

    meet_lst = [0 for _ in range(N)]

    meet = 999_999_999
    for i in range(N):
        meet = min(meet, rank_lst[i][1])
        meet_lst[i] = meet

    # 끝에서부터 처음으로 오면서 meet_lst가 자신의 meet보다 크거나 같다면 +=1

    ans = 0

    for i in range(N-1, -1, -1):
        if meet_lst[i] >= rank_lst[i][1]:
            ans += 1

    print(ans)
    