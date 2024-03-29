import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # 마을 수, 트럭 용량
M = int(input())  # 박스 개수

info_lst = []  # 이동 거리, 보내는 마을, 받는 마을, 박스 개수

for _ in range(M):
    S, E, B = map(int, input().split())  # 보내는 마을, 받는 마을, 박스 개수
    info_lst.append((E-S, S, E, B))

info_lst.sort(key=lambda x:(x[0], -x[2], -x[3]))

start_lst = [0 for _ in range(N+1)]
end_lst = [0 for _ in range(N+1)]
now_lst = [0 for _ in range(N+1)]

for d, s, e, c in info_lst:
    possible_box = 999_999_999
    for town in range(s, e):
        possible_box = min(possible_box, C-now_lst[town])
    possible_box = min(possible_box, c)

    if possible_box == 0:
        continue
    else:
        for town in range(s, e):
            now_lst[town] += possible_box
        end_lst[e] += possible_box

print(sum(end_lst))