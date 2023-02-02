import sys
import math

N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

dif = nums[-1] - nums[0]  # 리스트 정렬 후 가장 큰 수와 가장 작은 수의 차이
sqrt_dif = int(math.sqrt(dif)) + 1
possible = set()  # 중복을 막기위해 set사용

for i in range(1, sqrt_dif):  # 1은 답이 될 수 없지만 가장 큰 수가 답이 될 수도 있으므로 1부터
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
print(*result[1:])  # 1도 답에 포함되어 있을 것이므로 1번째 인덱스부터 슬라이싱하여 출력
