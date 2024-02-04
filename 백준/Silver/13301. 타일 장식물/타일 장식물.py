import sys
input = sys.stdin.readline

# 1 : 1 + 1 + 2 + 2
# 2 : 2 + 2 + 3 + 3
# 3 : 3 + 3 + 5 + 5
# 5 : 5 + 5 + 8 + 8

N = int(input())

before = 1
after = 1
cnt = 1

while True:
    if cnt == N:
        break
    before, after = after, before + after
    cnt += 1
print(before*2 + after*2)