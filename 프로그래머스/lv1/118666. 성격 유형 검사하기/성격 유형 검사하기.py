def solution(survey, choices):
    answer = ''
    find_lst = "RTCFJMAN"
    result_lst = [0, 0, 0, 0]
    for case in range(len(survey)):
        alpha_loc = find_lst.find(list(survey[case])[0])
        if alpha_loc % 2 == 0:
            result_lst[alpha_loc // 2] -= choices[case] - 4
        else:
            result_lst[alpha_loc // 2] += choices[case] - 4
    
    for i in range(4):
        if result_lst[i] >= 0:
            answer += find_lst[(2*i)]
        else:
            answer += find_lst[(2*i) + 1]

    return answer