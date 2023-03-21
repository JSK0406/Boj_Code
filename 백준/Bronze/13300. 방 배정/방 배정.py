import sys
input = sys.stdin.readline

N, K = map(int, input().split())
men = [0] * 6
women = [0] * 6

for _ in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        women[grade-1] += 1
    else:
        men[grade-1] += 1

result_lst = men + women
answer = 0

for li in result_lst:
    if li == 0:
        pass
    elif li // K == 0:
        answer += 1
    else:
        if answer % K == 0:
            answer += li // K
        else:
            answer += (li // K) + 1

print(answer)