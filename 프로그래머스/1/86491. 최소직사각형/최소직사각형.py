def solution(sizes):
    answer = 0
    
    first = 0
    second = 0
    for w, h in sizes:
        f, s = max(w, h), min(w, h)
        first = max(first, f)
        second = max(second, s)
        
    answer = first * second
    
    return answer