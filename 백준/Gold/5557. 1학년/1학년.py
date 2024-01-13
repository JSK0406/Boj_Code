import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
lst.insert(0, 0)
count_lst = [[0 for _ in range(21)] for _ in range(N)]

count_lst[1][lst[1]] = 1

for now in range(2, N):
    for num in range(0, 21):
        if count_lst[now-1][num]:
            if 0 <= num + lst[now] <= 20:
                count_lst[now][num+lst[now]] += count_lst[now-1][num]
            if 0 <= num - lst[now] <= 20:
                count_lst[now][num-lst[now]] += count_lst[now-1][num]

print(count_lst[-1][lst[-1]])