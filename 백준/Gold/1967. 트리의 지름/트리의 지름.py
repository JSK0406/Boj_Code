import sys
input = sys.stdin.readline

N = int(input())  # 노드의 수

edge_dict = dict()

for _ in range(N-1):
    inp = list(map(int, input().split()))
    try:
        edge_dict[inp[0]].append((inp[1], inp[2]))
    except:
        edge_dict[inp[0]] = [(inp[1], inp[2])]
    try:
        edge_dict[inp[1]].append((inp[0], inp[2]))
    except:
        edge_dict[inp[1]] = [(inp[0], inp[2])]
    

def find_farthest(start, visited):
    stack = [start]
    visited[start] = 0
    while stack:
        now = stack.pop()
        try:
            next_lst = edge_dict[now]
            for next, cost in next_lst:
                if next != start and not visited[next]:
                    visited[next] = visited[now] + cost
                    stack.append(next)
        except:
            continue
    max_idx = None
    max_ans = 0
    for i in range(len(visited)):
        if max_ans < visited[i]:
            max_idx = i
            max_ans = visited[i]
    return (max_ans, max_idx)

if N == 1:
    print(0)
else:
    n1 = find_farthest(1, [0] * (N + 1))[1]
    print(find_farthest(n1, [0] * (N + 1))[0])