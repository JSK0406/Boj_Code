import sys

my_dict = dict()

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
for i in num_lst:
    try:
        my_dict[i] += 1
    except:
        my_dict[i] = 1

answer = []
tmp = []
for i in num_lst:
    tmp.append(my_dict[i])

highest = max(tmp)
for i in range(len(tmp)):
    for j in range(i+1, len(tmp)):
        if tmp[i] == highest:
            answer.append(-1)
            break
        if tmp[i] < tmp[j]:
            answer.append(num_lst[j])
            break
    else:
        answer.append(-1)

print(*answer)