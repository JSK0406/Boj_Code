import sys
input = sys.stdin.readline

target = input()
pattern = input()
if target[-1] == '\n':
    target = target[:len(target)-1]
if pattern[-1] == '\n':
    pattern = pattern[:len(pattern)-1]
    
table = [0 for _ in range(len(pattern))]

left = 0
for right in range(1, len(pattern)):
    while left > 0 and pattern[left] != pattern[right]:
        left = table[left-1]
    
    if pattern[left] == pattern[right]:
        left += 1
        table[right] = left

pi = 0
ans = []
for ti in range(len(target)):
    while pi > 0 and target[ti] != pattern[pi]:
        pi = table[pi-1]
    if target[ti] == pattern[pi]:
        pi += 1
        if pi == len(pattern):
            ans.append(ti-pi+2)
            pi = table[pi-1]

print(len(ans))
for i in ans:
    print(i)
