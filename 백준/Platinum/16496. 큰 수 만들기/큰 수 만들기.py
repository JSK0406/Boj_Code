import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

9

answer = ''

new_numbers = []

for number in numbers:
    str_number = str(number)
    
    idx = 0
    while True:
        if len(str_number) == 20:
            break
    
        str_number += str_number[idx]
        idx += 1

    new_numbers.append([int(str_number), str(number)])
    
new_numbers.sort(key=lambda x: -x[0])

for new_number in new_numbers:
    answer += new_number[1]
    
if len(list(set(answer))) == 1 and list(set(answer))[0] == '0':
    answer = '0'

print(answer)