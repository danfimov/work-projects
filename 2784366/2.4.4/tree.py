class TNode:
    pass


def newNode(d):
    node = TNode()
    node.data = d
    node.left = None
    node.right = None
    return node


def priority(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 100


def lastOp(s):
    minPrt = 50  # любое между 2 и 100
    k = -1
    for i in range(len(s)):
        if priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            k = i
    return k


def makeTree(s):
    k = lastOp(s)
    if k < 0:  # создать лист
        Tree = newNode(s)
    else:  # создать узел-операцию
        Tree = newNode(s[k])
        Tree.left = makeTree(s[:k])
        Tree.right = makeTree(s[k + 1:])
    return Tree


def calcTree(Tree):
    if Tree.left is None:
        return int(Tree.data)
    else:
        n1 = calcTree(Tree.left)
        n2 = calcTree(Tree.right)
        if Tree.data == "+":
            res = n1 + n2
        elif Tree.data == "-":
            res = n1 - n2
        elif Tree.data == "*":
            res = n1 * n2
        else:
            res = n1 // n2
        return res


def printTree_prefix(Tree):
    stack = list()
    stack.append(Tree)
    while stack:
        node = stack.pop(-1)
        print(node.data, end=' ')
        if not (node.right is None):
            stack.append(node.right)
        if not (node.left is None):
            stack.append(node.left)


def printTree_postfix(Tree):
    if Tree.left is None:
        print(Tree.data, end=' ')
    else:
        printTree_postfix(Tree.left)
        printTree_postfix(Tree.right)

        print(Tree.data, end=' ')


def tree_width_traversal(Tree):
    queue = list()
    queue.append(Tree)
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)