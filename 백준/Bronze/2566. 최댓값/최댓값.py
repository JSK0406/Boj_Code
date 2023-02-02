import sys

final_max, row, col = 0, 0, 0

for r in range(9):
    tmp_lst = list(map(int, sys.stdin.readline().split()))
    tmp_max = max(tmp_lst)
    if tmp_max > final_max:
        final_max = tmp_max
        row, col = r, tmp_lst.index(final_max)

print(final_max)
print(row+1, col+1)