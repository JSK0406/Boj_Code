import sys
input = sys.stdin.readline

color_lst = [str(input().strip()) for _ in range(3)]

my_dict = dict()

my_dict['black'] = 0
my_dict['brown'] = 1
my_dict['red'] = 2
my_dict['orange'] = 3
my_dict['yellow'] = 4
my_dict['green'] = 5
my_dict['blue'] = 6
my_dict['violet'] = 7
my_dict['grey'] = 8
my_dict['white'] = 9

print((my_dict[color_lst[0]] * 10 + my_dict[color_lst[1]])*pow(10, my_dict[color_lst[2]]))

# black	0	1
# brown	1	10
# red	2	100
# orange	3	1,000
# yellow	4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet	7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000