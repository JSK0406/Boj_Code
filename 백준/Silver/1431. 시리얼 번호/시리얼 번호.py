import sys
input = sys.stdin.readline

N = int(input())
lst = [input().strip() for _ in range(N)]

def toSum(num):
    tmp_sum = 0
    for x in list(num):
        try:
            tmp_sum += int(x)
        except:
            pass
    return tmp_sum

lst.sort(key= lambda x: (len(x), toSum(x), x))

for i in range(len(lst)):
    print(lst[i])