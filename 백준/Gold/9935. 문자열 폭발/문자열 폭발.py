import sys

stack = []

str_input = list(sys.stdin.readline().strip())
find = list(sys.stdin.readline().strip())
last = find[-1]

for i in str_input:
    stack.append(i)
    if i == last:
        if find == stack[len(stack)-len(find):len(stack)]:
            del stack[len(stack)-len(find):len(stack)]

if stack:
    print(*stack, sep='')
else:
    print("FRULA")