import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    try:
        running_func = input().strip()
        N = int(input())
        nums = deque(input().strip()[1:-1].split(','))
        is_forward = True
        if N == 0:
            nums = deque()
        for fi in running_func:
            if fi == 'R':
                is_forward = not is_forward
            else:
                if is_forward:
                    nums.popleft()
                else:
                    nums.pop()
        if is_forward:
            print('[' + ",".join(nums) + ']')
        else:
            nums.reverse()
            print('[' + ",".join(nums) + ']')
    except:
        print('error')