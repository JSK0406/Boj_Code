import sys

N = int(sys.stdin.readline())

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    px, py = map(int, sys.stdin.readline().split())
    for x in range(px, px+10):
        for y in range(py, py+10):
            paper[x][y] = 1

result = 0

for lst in paper:
    result += sum(lst)

print(result)