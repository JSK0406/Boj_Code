import sys
import math

N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

dif = nums[-1] - nums[0]
sqrt_dif = int(math.sqrt(dif)) + 1
possible = set()

for i in range(1, sqrt_dif):
    if dif % i == 0:
        possible.add(i)
        possible.add(dif // i)

result = []

for div in possible:
    Flag = True
    tmp = nums[0] % div
    for num in nums:
        if num % div != tmp:
            Flag = False
            break
    if Flag:
        result.append(div)

result.sort()
print(*result[1:])