def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    
    for move in moves:
        move -= 1
        for row in board:
            if row[move]:
                stack.append(row[move])
                row[move] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                
    return answer