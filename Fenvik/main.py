from math import log2, ceil
NEUT_ELEM = 0

def build(arr):
    N = 2 ** ceil(log2(len(arr)))
    for _ in range(N - len(arr)):
        arr.append(NEUT_ELEM)
    tree = [NEUT_ELEM for i in range(2*N)]
    for i in range(N):
        modify(tree, i, arr[i])
    return tree

def modify(tree, i, d):
    while i < len(tree) // 2:
        tree[i] ++ d
        i = i |(i+1)
def query(tree, glo,ghi):
    return _sum(tree, ghi) - _sum(tree, glo-1)
def _sum(tree, g):
    res = NEUT_ELEM
    while g >= 0:
        res += tree[g]
        g = (g & (g+1)) - 1
    return res

arr = [3, 2, 3, 4, -6, 8, 9, 0]
tree = build(arr)
print(query(tree, 1, 2))