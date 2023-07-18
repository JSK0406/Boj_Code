import sys
input = sys.stdin.readline
import math

N = int(input())
num_lst = list(map(int, input().split()))
cnt_lst = [[] for _ in range(1000001)]  # 각 인덱스의 숫자들을 약수로 갖는 num들을 리스트로 추가
ans_lst = [0] * 1000001  # 약수를 가진 수들을 -1 하기 위한 count list

def func(num):
    """ 약수 구하는 함수

    Args:
        num (int): 약수를 찾으려는 num

    Returns:
        list : 약수의 리스트를 반환
    """
    tmp_lst1 = []
    tmp_lst2 = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            tmp_lst1.append(i)
    for j in tmp_lst1:
        append_num = num // j
        if j == append_num:
            continue
        tmp_lst2.append(append_num)
        
    return tmp_lst1 + tmp_lst2

for now_num in num_lst:  # 각자의 숫자들을 약수로 갖는 num(원래 수)들을 리스트에 추가
    div_lst = func(now_num)
    for i in div_lst:
        cnt_lst[i].append(now_num)

for now_num in num_lst:  # 자신을 약수로 갖는 수들의 개수를 cnt하고 약수로 갖게 하는 원래 수들을 -1씩
    ans_lst[now_num] += len(cnt_lst[now_num])
    for i in cnt_lst[now_num]:
        ans_lst[i] -= 1

answer = []
for now_num in num_lst:
    answer.append(ans_lst[now_num])

print(*answer)