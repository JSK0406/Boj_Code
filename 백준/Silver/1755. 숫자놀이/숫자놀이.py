import sys
input = sys.stdin.readline

str_dict = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
}

M, N = map(int, input().split())

sorting_lst = []

for num in range(M, N+1):
    str_num = str(num)
    if len(str_num) == 1:
        sorting_lst.append((num, str_dict[str_num]))
    else:
        sorting_lst.append((num, ' '.join([str_dict[str_num[0]], str_dict[str_num[1]]])))

sorting_lst.sort(key=lambda x: x[1])

for idx in range(len(sorting_lst)):
    print(sorting_lst[idx][0], end=' ')
    if (idx + 1) % 10 == 0:
        print('')