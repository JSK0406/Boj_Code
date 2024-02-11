# from collections import deque
# import copy

# def solution(name):
#     answer = 999_999_999
#     tot_cnt = len(''.join(name))
#     done_lst = [0 for _ in range(tot_cnt)]
    
#     for idx in range(tot_cnt):
#         if 'A' == name[idx]:
#             done_lst[idx] = 1
    
#     q = deque()
#     q.append((done_lst, 0, 0))
    
#     while q:
#         now_done_lst, now_idx, now_cnt = q.popleft()
#         if sum(now_done_lst) == tot_cnt:
#             answer = min(answer, now_cnt)
#         for idx in range(len(now_done_lst)):
#             if not now_done_lst[idx]:
#                 next_done_lst = copy.deepcopy(now_done_lst)
#                 next_done_lst[idx] = 1
#                 next_cnt = now_cnt
#                 next_cnt += min(abs(now_idx - idx), len(now_done_lst) - abs(now_idx - idx))
                
#                 for_cnt = 26 - abs(ord(name[idx]) - ord('A'))
#                 reverse_cnt = abs(ord(name[idx]) - ord('A'))
#                 next_cnt += min(for_cnt, reverse_cnt)
#                 if sum(next_done_lst) == tot_cnt:
#                     answer = min(answer, next_cnt)
#                 else:
#                     q.append((next_done_lst, idx, next_cnt))
        
#     return answer





from collections import deque
import copy

def solution(name):
    # 현재 인덱스에서 바꿀 것이 있는지 확인하고, 없으면 왼쪽 오른쪽에 가장 가까운 단어를 바꾼다.
    answers = []
    init_name = ['A' for _ in range(len(name))]
    
    q = deque()  # 현재 단어 상태, 현재 인덱스, 지금까지 움직인 횟수
    q.append((init_name, 0, 0))
    
    while q:
        now_name, now_idx, now_cnt = q.popleft()
        now_name = copy.deepcopy(now_name)
        next_cnt, left_idx, right_idx = now_cnt, now_idx, now_idx
        # 현재 인덱스에서 바꿔야할 단어가 있다면 바꿈
        if name[now_idx] != now_name[now_idx]:
            cnt1 = 26 - abs(ord(name[now_idx]) - ord('A'))
            cnt2 = abs(ord(name[now_idx]) - ord('A'))
            next_cnt += min(cnt1, cnt2)
            now_name[now_idx] = name[now_idx]
        
        # 단어가 완성되었는지 체크
        if ''.join(now_name) == name:
            answers.append(next_cnt)
            continue
        
        # 가까운 왼쪽 인덱스로 이동
        left_cnt = 0
        while True:
            left_idx -= 1
            left_cnt += 1
            if left_idx == -1:
                left_idx = len(name) - 1
            if name[left_idx] != now_name[left_idx]:
                q.append((now_name, left_idx, next_cnt + left_cnt))
                break
                
        # 가까운 오른쪽 인덱스로 이동
        right_cnt = 0
        while True:
            right_idx += 1
            right_cnt += 1
            if right_idx == len(name):
                right_idx = 0
            if name[right_idx] != now_name[right_idx]:
                q.append((now_name, right_idx, next_cnt + right_cnt))
                break
        
    return min(answers)
