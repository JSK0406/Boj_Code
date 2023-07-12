import sys
input = sys.stdin.readline

N = int(input())  # 수열 길이
seq_lst = list(map(int, input().split()))
seq_lst.insert(0, None)

larger_lst = [1] * (N+1)  # 왼쪽에서 오른쪽으로 커져감
smaller_lst = [1] * (N+1)  # 오른쪽에서 왼쪽으로 커져감

for i in range(1, N+1):
    for j in range(i-1, 0, -1):
        if seq_lst[i] > seq_lst[j]:
            larger_lst[i] = max(larger_lst[i], larger_lst[j] + 1)

for i in range(N, 0, -1):
    for j in range(i+1, N+1):
        if seq_lst[i] > seq_lst[j]:
            smaller_lst[i] = max(smaller_lst[i], smaller_lst[j] + 1)

result_lst = [larger_lst[i] + smaller_lst[i] - 1 for i in range(N+1)]  # 두 리스트를 더하고 겹치는 값인 해당 인덱스를 고려해 -1을 함
print(max(result_lst))