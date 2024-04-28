import sys
input = sys.stdin.readline

# N개 기차, 기차에는 20개의 좌석

# 명령
# 1 i x : i번째 기차에 x번째 좌석 사람 태우기, 있다면 패스
# 2 i x : i번째 기차에 x번째 좌석 하차, 없다면 패스
# 3 i : i번째 기차에 있는 사람들이 한칸씩 뒤로 간다
# 3 i : i번째 기차에 있는 사람들이 한칸씩 앞으로 간다, 1번째 자리에 사람 있으면 하차

# 기차 수, 명령 수
N, M = map(int, input().split())

train_lst = [0 for _ in range(N+1)]

for _ in range(M):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        i, x = tmp[1], tmp[2] - 1
        train_lst[i] |= 1 << x
    elif tmp[0] == 2:
        i, x = tmp[1], tmp[2] - 1
        train_lst[i] &= ~(1 << x)
    elif tmp[0] == 3:
        i = tmp[1]
        train_lst[i] <<= 1
        train_lst[i] &= ~(1 << 20)
    elif tmp[0] == 4:
        i = tmp[1]
        train_lst[i] >>= 1

print(len(set(train_lst[1:])))