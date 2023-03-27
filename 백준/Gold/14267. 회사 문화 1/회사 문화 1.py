import sys
input = sys.stdin.readline

n, m = map(int, input().split())
myboss_dict = dict()
edge_lst = list(map(int, input().split()))
score = [0] * (n+1)

for i in range(1, n):
    myboss_dict[i+1] = edge_lst[i]  # i번째 부하의 직속상사는 edge_lst[i]

for _ in range(m):
    num, figure = map(int, input().split())
    score[num] += figure

for i in range(2, n+1):
    score[i] += score[myboss_dict[i]]

print(*score[1:])
