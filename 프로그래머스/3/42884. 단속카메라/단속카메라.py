def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    
    camera = -999_999_999
    for start, end in routes:
        if camera < start:
            answer += 1
            camera = end
    
    return answer