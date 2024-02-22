import sys
input = sys.stdin.readline
import math

tree_dict = dict()

while True:
    now_tree = input().strip()
    if now_tree == '':
        break

    if now_tree in tree_dict:
        tree_dict[now_tree] += 1
    else:
        tree_dict[now_tree] = 1

tree_lst = list(tree_dict.items())  # 나무 이름, 수
tree_lst.sort(key=lambda x:x[0])

tot_cnt = 0
for tree, cnt in tree_lst:
    tot_cnt += cnt

for tree, cnt in tree_lst:
    print(f'{tree} {cnt/tot_cnt*100:.4f}')