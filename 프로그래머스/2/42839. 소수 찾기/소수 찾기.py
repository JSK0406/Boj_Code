import math
import itertools

def solution(numbers):
    answer = 0
    
    prime_lst = [0 for _ in range(10000000)]  # 9999999 넣어보기
    prime_lst[0] = 1  # 0처리
    prime_lst[1] = 1  # 1처리
    
    is_prime = [0 for _ in range(10000000)]
    
    for i in range(2, round(math.sqrt(10000000))+3):
        if prime_lst[i] == 1:
            continue
        for j in range(2, 10000000):
            if i*j > 9999999:  # 범위를 넘어감
                break
            prime_lst[i*j] = 1
    
    for i in range(1, len(numbers)+1):
        for number in itertools.permutations(numbers, i):  # 1개부터 len(numbers)개수까지 확인
            number = int(''.join(list(number)))
            if prime_lst[number] == 0:
                is_prime[number] = 1
    
    answer = sum(is_prime)
            
    return answer



















# import math
# import itertools

# def solution(numbers):
#     answer = 0
    
#     is_prime = [True for _ in range(10000000)]
    
#     for i in range(2, round(math.sqrt(10000000))+5):
#         if is_prime[i] == False:
#             continue
#         for j in range(2, 10000000):
#             now_num = i * j
#             if now_num > 9999999:
#                 break
#             is_prime[now_num] = False
    
#     permutations_lst = []
    
#     for i in range(1, len(numbers)+1):
#         for j in itertools.permutations(numbers, i):
#             permutations_lst.append(int(''.join(j)))
            
#     permutations_lst = list(set(permutations_lst))
    
#     for number in permutations_lst:
#         if number in [0, 1]:
#             continue
#         if is_prime[number]:
#             print(number)
#             answer += 1
    
#     return answer