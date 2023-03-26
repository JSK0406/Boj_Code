import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
order_lst = []

# N개 start -> end // N-1개 start -> mid and 1개의 기둥을 start -> end and N-1개 mid -> end
def hanoi_print(N, start, mid, end):
    global cnt, order_lst
    if N == 1:
        cnt += 1
        order_lst.append([start, end])
        return
    elif N == 2:
        cnt += 3
        order_lst.append([start, mid])
        order_lst.append([start, end])
        order_lst.append([mid, end])
    else:
        hanoi_print(N-1, start, end, mid)
        hanoi_print(1, start, mid, end)
        hanoi_print(N-1, mid, start, end)

if N <= 20:
    hanoi_print(N, 1, 2, 3)
else:
    cnt = 2**N-1

print(cnt)
if order_lst:
    for order in order_lst:
        print(*order)