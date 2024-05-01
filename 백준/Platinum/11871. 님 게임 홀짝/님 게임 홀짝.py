import sys
input = sys.stdin.readline

# 짝수 제거 => 모두 제거 못함
# 홀수 제거 => 무조건 전부만

# 0 또는 2면 끝

# 0 => (0)
# 1 => 0 : (1)
# 2 => (0)
# 3 => 0, 1 : (2)
# 4 => 2 : (1)
# 5 => 0, 1, 3 : (3)
# 6 => 2, 4 : (2)
# 7 => 0, 1, 3, 5 : (4)
# 8 => 2, 4, 6 : (3)

N = int(input())
stone_lst = list(map(int, input().split()))

num = 0

for s in stone_lst:
    # 짝수
    if s % 2 == 0:
        num ^= (s - 2) // 2
    # 홀수
    else:
        num ^= (s + 1) // 2

print('cubelover' if num == 0 else 'koosaga')