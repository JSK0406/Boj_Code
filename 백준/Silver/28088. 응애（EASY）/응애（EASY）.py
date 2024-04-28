import sys
input = sys.stdin.readline

# 16 8 4 2 1
# 4 3 2 1 0

# 1 1 0 0 1
# l: 1 0 0 1 1
# r: 1 1 1 0 0

# 1 1 1 1 0

# 부원 수, 처음 인사하는 수, 인사하는 횟수
N, M, K = map(int, input().split())
now_num = 0

for _ in range(M):
    tmp = int(input())
    now_num += 2**tmp

for _ in range(K):
    left_num = now_num << 1
    if now_num >= 2**(N-1):
        left_num += 1
    left_num %= 2**N
    right_num = now_num >> 1
    if now_num % 2 == 1:
        right_num += 2**(N-1)
    # 하나만 1이면 => 1
    now_num = left_num ^ right_num

ans = 0
while now_num > 0:
    if now_num % 2 == 1:
        ans += 1
    now_num >>= 1

print(ans)