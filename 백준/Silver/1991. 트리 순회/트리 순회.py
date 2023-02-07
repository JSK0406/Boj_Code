import sys

N = int(sys.stdin.readline())

node_dic = {}

for _ in range(N):
    A, B, C = sys.stdin.readline().split()
    node_dic[A] = [B,C]

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(node_dic[node][0])
    preorder(node_dic[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(node_dic[node][0])
    print(node, end='')
    inorder(node_dic[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(node_dic[node][0])
    postorder(node_dic[node][1])
    print(node, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')