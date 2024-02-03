def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = []  # price, idx
    
    for idx in range(len(prices)):
        price = prices[idx]
        if not stack:
            stack.append((price, idx))
            continue
        while True:
            if stack and stack[-1][0] > price:
                p, i = stack.pop()
                answer[i] = idx - i
            else:
                stack.append((price, idx))
                break
    
    while stack:
        p, i = stack.pop()
        answer[i] = len(prices) - i - 1

    return answer