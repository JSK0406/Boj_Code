import sys
input = sys.stdin.readline


# 테스트 개수, 기준 문자열
N, M = map(int, input().split())

tested_lst = [input().strip() for _ in range(N)]
testing_lst = [input().strip() for _ in range(M)]

tested_lst.sort()

def bisect(tested_lst, testing_str):
    left = 0
    right = N-1
    while (left <= right):
        mid = (left + right) // 2
        if tested_lst[mid] <= testing_str:
            left = mid + 1
        else:
            right = mid - 1
    return left

ans = 0
for testing_str in testing_lst:
    found_idx = bisect(tested_lst, testing_str)
    if found_idx - 1 >= 0:
        tested_str = tested_lst[found_idx-1]
        if len(tested_str) >= len(testing_str):
            if tested_str.startswith(testing_str):
                ans += 1
                continue
    if found_idx < N:
        tested_str = tested_lst[found_idx]
        if len(tested_str) >= len(testing_str):
            if tested_str.startswith(testing_str):
                ans += 1

print(ans)