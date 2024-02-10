from collections import deque
import copy

def solution(tickets):
    answer = []

    ticket_dict = dict()  # 출발지 : [[도착지, 티켓 번호]]
    
    for idx in range(len(tickets)):
        ticket = tickets[idx]
        dep, arv = ticket
        try:
            ticket_dict[dep].append([arv, idx])
        except:
            ticket_dict[dep] = [[arv, idx]]
    
    q = deque()  # 현재 도시, 지금까지의 경로, 사용한 티켓 번호
    q.append(('ICN', ['ICN'], set()))
    
    while q:
        now_city, now_dist_lst, now_num_set = q.popleft()
        if now_city in set(ticket_dict.keys()):
            ticket_lst = sorted(ticket_dict[now_city], key=lambda x:x[0])

            for idx in range(len(ticket_lst)):
                next_city, ticket_num = ticket_lst[idx][0], ticket_lst[idx][1]
                if ticket_num in now_num_set:  # 사용한 티켓
                    continue
                next_dist_lst = copy.deepcopy(now_dist_lst)
                next_num_set = copy.deepcopy(now_num_set)
                next_dist_lst.append(next_city)
                next_num_set.add(ticket_num)
                if len(next_dist_lst) == len(tickets)+1:
                    answer.append((next_dist_lst))
                q.append((next_city, next_dist_lst, next_num_set))
                
    answer.sort()
    
    return answer[0]