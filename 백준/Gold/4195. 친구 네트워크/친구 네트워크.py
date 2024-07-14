import sys
input = sys.stdin.readline

group_people_dict = dict()  # 그룹 이름 : [사람들]
people_group_dict = dict()  # 사람 이름 : 속한 그룹

def find(x):
    if x == people_group_dict[x]:
        return x
    people_group_dict[x] = find(people_group_dict[x])
    return people_group_dict[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return x
    if x < y:
        next_group = people_group_dict[x]
        group_people_dict[x] += group_people_dict[y]

        for p in group_people_dict[y]:
            people_group_dict[p] = next_group
        group_people_dict.pop(y)
        return x
    else:
        next_group = people_group_dict[y]
        group_people_dict[y] += group_people_dict[x]

        for p in group_people_dict[x]:
            people_group_dict[p] = next_group
        group_people_dict.pop(x)
        return y
    
for _ in range(int(input())):
    F = int(input())  # 친구 관계 수
    
    group_people_dict = dict()  # 그룹 이름 : [사람들]
    people_group_dict = dict()  # 사람 이름 : 속한 그룹

    for _ in range(F):
        A, B = input().split()
        if A not in people_group_dict:
            people_group_dict[A] = A
            group_people_dict[A] = [A]
        if B not in people_group_dict:
            people_group_dict[B] = B
            group_people_dict[B] = [B]

        print(len(group_people_dict[union(A, B)]))