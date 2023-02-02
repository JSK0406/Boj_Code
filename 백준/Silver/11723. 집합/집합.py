import sys

S = set()

N = int(sys.stdin.readline())
for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0]=='add':
        S.add(int(com[1]))
    elif com[0]=='remove':
        if int(com[1]) in S:
            S.remove(int(com[1]))
    elif com[0]=='check':
        if int(com[1]) in S:
            print(1)
        else:
            print(0)
    elif com[0]=='toggle':
        if int(com[1]) in S:
            S.remove(int(com[1]))
        else:
            S.add(int(com[1]))
    elif com[0]=='all':
        S = {i for i in range(1,21)}
    elif com[0]=='empty':
        S = set()