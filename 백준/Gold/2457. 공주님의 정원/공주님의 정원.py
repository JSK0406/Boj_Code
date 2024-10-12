import sys
input = sys.stdin.readline

N = int(input())
flower_lst = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    flower_lst.append((a * 100 + b, c * 100 + d))

flower_lst.sort(key= lambda x: (x[0], x[1]))

now = 301 # 시작하는 날이 같거나 작아야함
selected_finish = 0

# 현재 날짜 이후로 가장 오래 지속되는 꽃

i = 0
ans = 0
while i < N and now < 1201:
    start, end = flower_lst[i]
    if now >= start:
        selected_finish = max(selected_finish, end)
        if selected_finish > 1130:
            ans += 1
            break
        i += 1
    elif selected_finish == now:
        ans = 0
        break
    else:
        ans += 1
        now = selected_finish

if selected_finish <= 1130:
    ans = 0
print(ans)