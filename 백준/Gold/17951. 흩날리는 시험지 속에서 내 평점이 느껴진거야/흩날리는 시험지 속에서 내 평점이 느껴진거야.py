import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 시험지 개수, 그룹 수
score_lst = list(map(int, input().split()))

lower = 0
upper = ((10**5) * 20) + 1

if K == 1:
    print(sum(score_lst))
else:
    while lower <= upper:
        mid = (lower + upper) // 2
        left_group = K
        now_sum = 0
        now_idx = 0
        while now_idx < N:
            now_sum += score_lst[now_idx]
            now_idx += 1
            if mid <= now_sum:
                left_group -= 1
                now_sum = 0
            if left_group == 1:
                break
        if now_idx < N and mid <= sum(score_lst[now_idx:]):
            lower = mid + 1
        else:
            upper = mid - 1

    print(upper)