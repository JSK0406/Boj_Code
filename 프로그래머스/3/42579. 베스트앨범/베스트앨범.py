def solution(genres, plays):
    answer = []
    
    info_lst = []  # 해당 장르의 총 플레이 횟수, 해당 곡의 플레이 횟수, 고유번호
    
    genre_dict = dict()
    
    for i in range(len(plays)):
        genre = genres[i]
        try:
            genre_dict[genre] += plays[i]
        except:
            genre_dict[genre] = plays[i]

    for i in range(len(plays)):
        info_lst.append((genre_dict[genres[i]], plays[i], i))        
    
    check_dict = dict()
    
    info_lst.sort(key=lambda x: (-x[0], -x[1], x[2]))
    
    for info in info_lst:
        tot_cnt, this_cnt, idx = info
        try:
            if check_dict[tot_cnt] == 1:
                check_dict[tot_cnt] += 1
                answer.append(idx)
        except:
            check_dict[tot_cnt] = 1
            answer.append(idx)
    
    return answer