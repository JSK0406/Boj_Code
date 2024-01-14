import sys
input = sys.stdin.readline
from collections import deque

S = int(input())

count_lst = [[0 for _ in range(2002)] for _ in range(2002)]

q = deque()
q.append((1, 1, 1))  # num, duplicated_num, count

while q:
    num, duplicated_num, count = q.popleft()
    if num == S:
        print(count)
        break
    # 기존 복사본으로 붙여넣기
    if 0 <= num + duplicated_num < 2002 and not count_lst[num][num+duplicated_num]:
        count_lst[num][num+duplicated_num] = count+1
        q.append((num+duplicated_num, duplicated_num, count+1))
    # 하나 빼기
    if 0 <= num - 1 < 2002 and not count_lst[num][num-1]:
        count_lst[num][num-1] = count+1
        q.append((num-1, duplicated_num, count+1))
    # 지금 상태 복사하기
    if num != duplicated_num:
        q.append((num, num, count+1))