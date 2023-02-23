def solution(n, left, right):
    lst = []
    answer = []
    
    for i in range(left // n+1, (right // n) +2):
        for _ in range(i):
            lst.append(i)
        for j in range(n-i):
            lst.append(i+j+1)
    
    answer = lst[left % n : (left % n) + (right - left + 1)]
    
    
    return answer