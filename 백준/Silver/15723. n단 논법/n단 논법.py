import sys
input = sys.stdin.readline

alpha_dict = dict()

for _ in range(int(input())):
    tmp_lst = list(input().split())
    alpha1, alpha2 = tmp_lst[0], tmp_lst[-1]
    alpha_dict[alpha1] = alpha2

for _ in range(int(input())):
    tmp_lst = list(input().split())
    alpha1, alpha2 = tmp_lst[0], tmp_lst[-1]
    try:
        while True:
            if alpha_dict[alpha1]:
                if alpha_dict[alpha1] == alpha2:
                    print('T')
                    break
                else:
                    alpha1 = alpha_dict[alpha1]
    except:
        print('F')