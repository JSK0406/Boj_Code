str = input().strip()

tmp = ''
for i in str:
    if len(tmp) == 10:
        print(tmp)
        tmp = ''
    tmp += i
print(tmp)