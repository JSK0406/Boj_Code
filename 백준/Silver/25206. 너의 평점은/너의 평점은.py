import sys
import math
tot_div = 0
tot_sum = 0
for _ in range(20):
    name, num, grade = input().split()
    num = float(num)
    if grade =='A+':
        tot_div += num
        tot_sum += num * 4.5
    elif grade =='A0':
        tot_div += num
        tot_sum += num * 4.0
    elif grade =='B+':
        tot_div += num
        tot_sum += num * 3.5
    elif grade =='B0':
        tot_div += num
        tot_sum += num * 3.0
    elif grade =='C+':
        tot_div += num
        tot_sum += num * 2.5
    elif grade =='C0':
        tot_div += num
        tot_sum += num * 2.0
    elif grade =='D+':
        tot_div += num
        tot_sum += num * 1.5
    elif grade =='D0':
        tot_div += num
        tot_sum += num * 1.0
    elif grade =='F':
        tot_div += num
    elif grade =='P':
        pass
print(f'{tot_sum/tot_div:.6f}')