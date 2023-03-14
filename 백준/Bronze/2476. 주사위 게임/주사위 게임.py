import sys
input = sys.stdin.readline

N = int(input())
prize_lst = []

for _ in range(N):
    num_lst = list(map(int ,input().split()))
    num_lst.sort()
    if num_lst[0] == num_lst[2]:
        prize_lst.append(10000 + (num_lst[0] * 1000))
    elif num_lst[0] == num_lst[1] or num_lst[1] == num_lst[2]:
        prize_lst.append(1000 + (num_lst[1] * 100))
    else:
        prize_lst.append(num_lst[2] * 100)

print(max(prize_lst))