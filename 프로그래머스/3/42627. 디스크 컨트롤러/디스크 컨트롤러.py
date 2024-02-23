# 걸리는 시간이 짧은 것
import heapq
import math

def solution(jobs):
    answer = 0
    visited_lst = [0 for _ in range(len(jobs))]
    
    now = 0
    
    hq = []  # 걸리는 시간, 시작 시간

    # 시작 시간이 지금 시간보다 작아야 가능
    cnt = 0
    while True:
        if cnt == len(jobs):
            break
        for idx in range(len(jobs)):
            # 추가하지 않았고, 지금 시간에 추가가 가능한 경우
            if not visited_lst[idx] and jobs[idx][0] <= now:
                # 추가하고, visited_lst에 반영
                heapq.heappush(hq, (jobs[idx][1], jobs[idx][0]))
                visited_lst[idx] = 1
        # 작업 시작이 불가하다면
        if not hq:
            now += 1
            continue
        # 가능하다면 가장 실행시간이 짧은 것 추출
        else:
            poped_during_time, poped_start_time = heapq.heappop(hq)
            answer += now-poped_start_time+poped_during_time
            now += poped_during_time
            cnt += 1
    
    return math.floor(answer // len(jobs))




























# def solution(jobs):
#     answer = 0

#     duration_lst = []
#     start_lst = []

#     for i in range(len(jobs)):
#         a, b = jobs[i]
#         duration_lst.append([b, a, i])
#         start_lst.append([a, b, i])

#     duration_lst.sort(key=lambda x:(x[0], x[1]))
#     start_lst.sort(key=lambda x:(x[0], -x[1]))

#     is_done = [0 for _ in range(len(jobs))]

#     now_time = 0
#     while True:
#         if sum(is_done) == len(jobs):
#             break

#         is_requested = False
#         next_idx = -1

#         for i in range(len(jobs)):
#             duration, start, idx = duration_lst[i]
#             if start <= now_time and not is_done[idx]:
#                 next_idx = idx
#                 is_requested = True
#                 break

#         if not is_requested:
#             for i in range(len(jobs)):
#                 start, duration, idx = start_lst[i]
#                 if not is_done[idx]:
#                     next_idx = idx
#                     break

#         is_done[next_idx] = 1

#         if jobs[next_idx][0] <= now_time:
#             answer = answer + now_time + jobs[next_idx][1] - jobs[next_idx][0]
#             now_time = now_time + jobs[next_idx][1]
#         else:
#             answer = answer + jobs[next_idx][1]
#             now_time = jobs[next_idx][0] + jobs[next_idx][1]
            
#         print(answer)
#     return answer//len(jobs)

# 0 3
# 1 9
# 2 6

# 현재 작업의 시작시간이 괜찮을 때라면 무조건 작업시간이 짧은 것
# 그게 아니라 시작시간이 아직 되지 않았다면 시작시간이 이전까지의 작업시간이 됨
# 이때는 시작시간+작업시간이 가장 짧은 것을 진행해야 함

# case1
# 0 3
# 1 3+9  12
# 2 3+9+6  18

# case2
# 0 3
# 2 3+6
# 1 3+6+9

# => 왼쪽은 어차피 다 같으므로 오른쪽을 줄여야 함 따라서 끝나는 시간이 적은 순으로 추가해야함

# [[0, 3], [5, 6], [7, 3]]
# testCase 2-1
# 0 3
# 7 7+3+3 = 7
# 5 7+3+6

# testCase 2-2
# 0 3
# 5 (5-3)+6
# 7 5+6+3

# => 왼쪽은 다 같음, 오른쪽은 전이 끝나는 시간과 다음 작업이 시작하는 시간을 따져서 적은 것을 선택
# => 따라서 전 작업이 끝나는 시간과 지금 작업이 시작하는 시간을 비교하여 (더 큰것 + 작업시간)
# => min((max(지난 작업 끝난 시간, 지금 작업 시작하는 시간) + 작업시간))

# 시작이 가능하다면 소요시간이 짧은 것을 실행해야 함
# 결국에 수가 계속 누적되면서 반복