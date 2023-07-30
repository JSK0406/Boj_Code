import sys

N, r, c = map(int, input().split())  # 변의 길이, 행, 열
N = pow(2, N)

ans = 0

def recur(N, r, c):
    global ans
    if N == 2:
        if r == 0 and c == 0:
            ans += 1
            return
        elif r == 0 and c == 1:
            ans += 2
            return
        elif r == 1 and c == 0:
            ans += 3
            return
        elif r == 1 and c == 1:
            ans += 4
            return
    if r < N // 2 and c < N // 2:  # 1사분면
        return recur(N // 2, r, c)
    elif r < N // 2 and c >= N // 2:  # 2사분면
        ans += pow(N//2, 2)
        return recur(N // 2, r, c - N // 2)
    elif r >= N // 2 and c < N // 2:  # 3사분면
        ans += pow(N//2, 2) * 2
        return recur(N // 2, r - N // 2, c)
    elif r >= N // 2 and c >= N // 2:  # 4사분면
        ans += pow(N//2, 2) * 3
        return recur(N // 2, r - N // 2, c - N // 2)

recur(N, r, c)
print(ans - 1)