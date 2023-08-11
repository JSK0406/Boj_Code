import sys
input = sys.stdin.readline
import itertools

def mbti_cnt(A, B):
    cnt = 0
    for i in range(4):
        if A[i] == B[i]:
            pass
        else:
            cnt += 1
    return cnt

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N = int(input())  # mbti 수
    mbti_lst = input().split()
    ans = 999_999_999
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if not i == j and not j == k and not i == k:
                        tmp_ans = mbti_cnt(mbti_lst[i], mbti_lst[j])
                        tmp_ans += mbti_cnt(mbti_lst[j], mbti_lst[k])
                        tmp_ans += mbti_cnt(mbti_lst[k], mbti_lst[i])
                        ans = min(ans, tmp_ans)
        print(ans)
        