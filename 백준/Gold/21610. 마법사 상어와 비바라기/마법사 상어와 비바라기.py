import sys
input = sys.stdin.readline

# N * N 격자
# 바구니에 저장할 물의 양은 무제한
# (1, 1) ~ (N, N) => -1 해줘야 함
# 격자의 끝은 시작과 연결되어 있음

# 왼쪽 아래의 4칸이 구름의 시작
# 1부터 8까지 => 왼쪽부터 시계방향



N, M = map(int, input().split())  # 격자 크기, 명령 수

map_lst = [list(map(int, input().split())) for _ in range(N)]
order_lst = [list(map(int, input().split())) for _ in range(M)]

cloud_lst = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]  # 초기 구름 위치

def is_in(a):
    return 0 <= a < N

def move_clouds(cloud_lst, dir, dis):
    dr, dc = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)][dir-1]

    new_cloud_lst = []
    for r, c in cloud_lst:
        new_r = (r + dr * dis) % N
        new_c = (c + dc * dis) % N
        new_cloud_lst.append((new_r, new_c))

    return new_cloud_lst

def add_one(cloud_lst):
    global map_lst
    for r, c in cloud_lst:
        map_lst[r][c] += 1

def bug_magic(cloud_lst):
    for r, c in cloud_lst:
        cnt = 0
        
        # 왼쪽 위
        if is_in(r-1) and is_in(c-1) and map_lst[r-1][c-1]:
            cnt += 1
        # 오른쪽 위
        if is_in(r-1) and is_in(c+1) and map_lst[r-1][c+1]:
            cnt += 1
        # 왼쪽 아래
        if is_in(r+1) and is_in(c-1) and map_lst[r+1][c-1]:
            cnt += 1
        # 오른쪽 아래
        if is_in(r+1) and is_in(c+1) and map_lst[r+1][c+1]:
            cnt += 1

        map_lst[r][c] += cnt

def make_clouds(pre_cloud_lst):
    new_cloud_lst = []
    pre_cloud_set = set(pre_cloud_lst)
    for r in range(N):
        for c in range(N):
            if (r, c) not in pre_cloud_set and map_lst[r][c] >= 2:
                map_lst[r][c] -= 2
                new_cloud_lst.append((r, c))
    return new_cloud_lst


for m in range(M):
    now_dir, now_dis = order_lst[m]

    # 모든 구름 이동
        # 모듈러 연산
    cloud_lst = move_clouds(cloud_lst, now_dir, now_dis)

    # 각 구름 칸에 1씩 증가
    add_one(cloud_lst)

    # 각 구름 칸에 물복사 버그
        # 각 대각선 4칸 확인해서 물 있는 거 몇개인지 확인
            # 4칸이 다 차있는지 아닌지 확인해도 될듯
    bug_magic(cloud_lst)

    # 바구니 저장된 물의 양이 2인 칸 -=2 하고 구름 리스트에 넣기
    cloud_lst = make_clouds(cloud_lst)

ans = 0
for r in range(N):
    ans += sum(map_lst[r])

print(ans)
