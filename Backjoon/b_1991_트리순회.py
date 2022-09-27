import sys

def preorder(root, res, tree):
    if root != '.':
        res.append(root)
        preorder(tree[root][0], res, tree)
        preorder(tree[root][1], res, tree)

def inorder(root, res, tree):
    if root != '.':
        inorder(tree[root][0], res, tree)
        res.append(root)
        inorder(tree[root][1], res, tree)

def postorder(root, res, tree):
    if root != '.':
        postorder(tree[root][0], res, tree)
        postorder(tree[root][1], res, tree)
        res.append(root)

input = sys.stdin.readline
n = int(input())
tree = {}
pre_res = []
in_res = []
post_res = []
for i in range(n):
    parent, left_child, right_child = map(str, input().rstrip().split(" "))
    tree[parent] = [left_child, right_child]


preorder('A', pre_res, tree)
inorder('A', in_res, tree)
postorder('A', post_res, tree)
print("".join(pre_res))
print("".join(in_res))
print("".join(post_res))