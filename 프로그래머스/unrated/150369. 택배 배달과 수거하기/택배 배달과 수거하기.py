def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        cap_deliver = cap
        cap_pick = cap
        while deliveries and deliveries[-1]==0:
            deliveries.pop()
        while pickups and pickups[-1]==0:
            pickups.pop()
        answer += max(len(deliveries), len(pickups)) * 2
        while deliveries and cap_deliver > 0 :
            if deliveries[-1] > cap_deliver:
                deliveries[-1] -= cap_deliver
                cap_deliver = 0
            else:
                cap_deliver -= deliveries[-1]
                deliveries.pop()
        
        while pickups and cap_pick > 0:
            if pickups[-1] > cap_pick:
                pickups[-1] -= cap_pick
                cap_pick = 0
            else:
                cap_pick -= pickups[-1]
                pickups.pop()
            
    return answer