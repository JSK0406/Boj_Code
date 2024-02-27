import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 스크린 너비, 바구니 너비
J = int(input())

apple_lst = [int(input()) for _ in range(J)]

ans = 0
left_idx = 1
right_idx = M

for now_apple in apple_lst:
    if left_idx <= now_apple and now_apple <= right_idx:
        continue
    elif left_idx > now_apple:  # 왼쪽 이동
        ans += abs(now_apple - left_idx)
        left_idx = now_apple
        right_idx = left_idx + M - 1
    else:  # 오른쪽 이동
        ans += abs(now_apple - right_idx)
        right_idx = now_apple
        left_idx = right_idx - M + 1

print(ans)