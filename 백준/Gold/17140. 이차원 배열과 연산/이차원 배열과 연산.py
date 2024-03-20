import sys
input = sys.stdin.readline
from collections import defaultdict

# 횟수가 작을 수록, 숫자가 작을 수록
# 3*3

# 행 개수 >= 열 개수 => 행에 대해서 정렬
# 행 개수 < 열 개수 => 열에 대해서 정렬

# row, col => K가 되는 것
R, C, K = map(int, input().split())

num_matrix = [list(map(int, input().split())) for _ in range(3)]

def is_row_sort():
    global num_matrix
    
    # 행 개수 >= 열 개수
    if len(num_matrix) >= len(num_matrix[0]):
        return True
    return False

def sort_row():
    global num_matrix

    row_lst = []
    for num_row in num_matrix:
        num_dict = defaultdict(int)
        for num in num_row:
            if num != 0:
                num_dict[num] += 1
        row_lst.append(sorted(list(num_dict.items()), key=lambda x:(x[1], x[0])))  # 숫자, 개수

    max_length = 0
    for row in row_lst:
        max_length = max(max_length, len(row)*2)
    
    num_matrix = []

    for row in row_lst:
        new_row = []
        for n, c in row:
            new_row += [n, c]

        new_row += [0 for _ in range(max_length-len(new_row))]
        if len(new_row) > 100:
            num_matrix.append(new_row[:100])
        else:
            num_matrix.append(new_row)

def sort_col():
    global num_matrix

    col_lst = []  # len(col_lst) => col
    for c in range(len(num_matrix[0])):
        num_col = []
        num_dict = defaultdict(int)
        for r in range(len(num_matrix)):
            num_col.append(num_matrix[r][c])
        for num in num_col:
            if num != 0:
                num_dict[num] += 1
        col_lst.append(sorted(list(num_dict.items()), key=lambda x:(x[1], x[0])))  # 숫자, 개수
    
    max_length = 0  # row
    for col in col_lst:
        max_length = max(max_length, len(col)*2)
    
    num_matrix = []

    for col in col_lst:
        new_col = []
        for n, c in col:
            new_col += [n, c]

        new_col += [0 for _ in range(max_length-len(new_col))]
        if len(new_col) > 100:
            num_matrix.append(new_col[:100])
        else:
            num_matrix.append(new_col)

    num_matrix = list(zip(*num_matrix))

def check_finish():
    global num_matrix

    if R-1 < len(num_matrix) and C-1 < len(num_matrix[0]):
        if num_matrix[R-1][C-1] == K:
            return True
    return False

ans = 0

if not check_finish():
    for _ in range(101):
        ans += 1
        if is_row_sort():
            sort_row()
        else:
            sort_col()
        if check_finish():
            break

if ans == 101:
    print(-1)
else:
    print(ans)