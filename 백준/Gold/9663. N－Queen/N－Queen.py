import sys
input = sys.stdin.readline

N = int(input())

lst = []
cnt = 0
def func():
    global cnt
    if len(lst) == N:
        cnt += 1
        return
    for i in range(N):
        now = (len(lst), i)  # x, y
        Flag = True  # 추가 가능
        for x, y in lst:
            if abs(x - now[0]) != abs(y - now[1]) and x != now[0] and y != now[1]:
                continue
            else:
                Flag = False  # 추가 불가
                break
        if Flag:
            lst.append(now)
            func()
            lst.pop()
        else:
            continue
    return

func()
print(cnt)