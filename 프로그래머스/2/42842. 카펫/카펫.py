def solution(brown, yellow):
    answer = []
    
    for yellow_row in range(1, yellow+1):
        if yellow % yellow_row != 0:
            continue
        yellow_col = yellow // yellow_row
        
        if (yellow_row * 2 + yellow_col * 2 + 4 == brown):
            whole_row, whole_col = max(yellow_row+2, yellow_col+2), min(yellow_row+2, yellow_col+2)
            answer = [whole_row, whole_col]
            break
            
    return answer

# yellow의 세로 * 2
# yellow의 가로 * 2
# + 4
# 일치한다면 답은 => [yellow의 가로+2, yellow의 세로 + 2]