# 앞에 있는 수가 클 수록 크다
# i와 i+1을 비교하면서 i+1이 크면 i 삭제
# 이게 안된다면 뒤에서 마지막으로 삭제
from collections import deque

def solution(number, k):
    number = str(number)
    is_delete = [0 for _ in range(len(number))]

    stack = []
    
    delete_cnt = 0
    idx = 0
    while idx < len(number):
        # 비어있다면 숫자 채우기
        if not stack:
            stack.append(number[idx])
            idx += 1
            continue
            
        # 들어갈 숫자가 기존 숫자보다 크다면 해당 숫자 삭제
        if int(stack[-1]) < int(number[idx]):
            stack.pop()
            delete_cnt += 1
        # 크지 않다면 숫자 채우기
        else:
            stack.append((number[idx]))
            idx += 1
        
        # 삭제 개수 충족되면 break
        if delete_cnt == k:
            break
            
    # 인덱스가 아직 끝까지 도착 안 한 경우 => 나머지 추가
    if idx < len(number):
        for i in range(idx, len(number)):
            stack.append(number[i])
    
    # 끝까지 도착했는데 삭제 개수가 충족이 안 된 경우 => 끝에서부터 숫자 개수맞춰 제거
    if delete_cnt < k:
        for _ in range(k-delete_cnt):
            stack.pop()
            
    return ''.join(stack)