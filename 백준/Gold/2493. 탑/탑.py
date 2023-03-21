import sys
input = sys.stdin.readline

N = int(input())
tops_height = list(map(int, input().split()))
answers = []
stack = []

for ti in range(N):
    if not stack or stack[0][0] <= tops_height[ti]:  # stack이 비어있거나 stack의 가장 큰 높이보다 지금 탑이 더 크다면 stack 새로 만들기
        stack = [[tops_height[ti], ti]]
        answers.append(0)
    else:
        for si in range(len(stack)-1, -1, -1):
            if stack[si][0] > tops_height[ti]:  # stack의 stack iter를 역순으로 반복하여 현재 탑의 높이보다 stack의 탑의 높이가 더 큰 순간에 stack의 idx+1을 답으로 추가하고 stack에 현재 탑 추가
                answers.append(stack[si][1]+1)
                stack.append([tops_height[ti], ti])
                break
            else:  # 반복 중에 현재 iter의 탑 높이가 현재 탑 높이보다 작다면 현재 탑이 iter의 탑을 가려 iter의 탑 높이가 쓰이지 않으므로 pop을 한다.
                stack.pop()
print(*answers)