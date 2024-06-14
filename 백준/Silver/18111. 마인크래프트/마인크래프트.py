import sys
input = sys.stdin.readline

# 가장 위의 블록을 제거하여 인벤토리에 넣음 => 2초
# 인벤토리에서 블록을 꺼내 칸 바로 위에 놓음 => 1초

# 500 * 500 = 250000

N, M, B = map(int, input().split())  # row, col, 블록 개수
land_lst = [list(map(int, input().split())) for _ in range(N)]

ans_time = sys.maxsize
ans_height = 0

for now_height in range(0, 257):
    plus_block = 0
    minus_block = 0
    now_B = B
    for r in range(N):
        for c in range(M):
            if land_lst[r][c] > now_height:
                plus_block += land_lst[r][c] - now_height
            else:
                minus_block += now_height - land_lst[r][c]

    if plus_block + now_B >= minus_block:
        if ans_time >= plus_block * 2 + minus_block:
            ans_time = plus_block * 2 + minus_block
            ans_height = now_height

print(ans_time, ans_height)