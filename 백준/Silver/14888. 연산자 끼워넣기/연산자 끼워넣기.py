import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈

max_ans = -9_999_999_999
min_ans = 9_999_999_999
def max_func(tmp_ans, cnt):
    global max_ans
    global min_ans
    if cnt == N:
        max_ans = max(max_ans, tmp_ans)
        min_ans = min(min_ans, tmp_ans)
        return
    for i in range(4):
        if oper_lst[i]:
            oper_lst[i] -= 1
            if i == 0:
                max_func(tmp_ans + num_lst[cnt], cnt+1)
            elif i == 1:
                max_func(tmp_ans - num_lst[cnt], cnt+1)
            elif i == 2:
                max_func(tmp_ans * num_lst[cnt], cnt+1)
            else:
                if tmp_ans < 0:
                    max_func(-(-tmp_ans // num_lst[cnt]), cnt+1)
                else:
                    max_func(tmp_ans // num_lst[cnt], cnt+1)
            oper_lst[i] += 1
max_func(num_lst[0], 1)
print(max_ans)
print(min_ans)