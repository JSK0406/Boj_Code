import sys
input = sys.stdin.readline
import bisect

# 점 개수, 선분 개수
N, M = map(int, input().split())
point_lst = list(map(int, input().split()))
point_lst.sort()

ans_lst = []
for _ in range(M):
    s, e = map(int, input().split())
    s_idx = bisect.bisect_left(point_lst, s)
    e_idx = bisect.bisect_right(point_lst, e)
    
    ans_lst.append(e_idx-s_idx)
    
for ans in ans_lst:
    print(ans)