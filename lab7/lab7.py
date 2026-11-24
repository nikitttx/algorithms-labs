# Варіант 15: вхідна послідовність ключів.
values = [19, 75, 43, 31, 5, 66, 62, 34, 76]

class Node:
    def __init__(self, key, color='B'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

def bst_insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = bst_insert(root.left, key)
    elif key > root.key:
        root.right = bst_insert(root.right, key)
    return root

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def bst_delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = bst_delete(root.left, key)
    elif key > root.key:
        root.right = bst_delete(root.right, key)
    elif root.left is not None and root.right is not None:
        root.key = find_min(root.right).key
        root.right = bst_delete(root.right, root.key)
    else:
        root = root.left if root.left is not None else root.right
    return root

def inorder(x, out):
    if x is not None:
        inorder(x.left, out)
        out.append(x.key)
        inorder(x.right, out)

def preorder(x, out):
    if x is not None:
        out.append(x.key)
        preorder(x.left, out)
        preorder(x.right, out)

def postorder(x, out):
    if x is not None:
        postorder(x.left, out)
        postorder(x.right, out)
        out.append(x.key)

def height(x):
    if x is None:
        return 0
    return 1 + max(height(x.left), height(x.right))

def color_of(x):
    return 'B' if x is None else x.color

def left_rotate(root, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return root

def right_rotate(root, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x
    x.right = y
    y.parent = x
    return root

def rb_insert(root, key):
    z = Node(key, 'R')
    y = None
    x = root
    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right
    z.parent = y
    if y is None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    while z.parent is not None and z.parent.color == 'R':
        g = z.parent.parent
        if z.parent == g.left:
            u = g.right
            if color_of(u) == 'R':
                z.parent.color = 'B'
                u.color = 'B'
                g.color = 'R'
                z = g
            else:
                if z == z.parent.right:
                    z = z.parent
                    root = left_rotate(root, z)
                z.parent.color = 'B'
                g.color = 'R'
                root = right_rotate(root, g)
        else:
            u = g.left
            if color_of(u) == 'R':
                z.parent.color = 'B'
                u.color = 'B'
                g.color = 'R'
                z = g
            else:
                if z == z.parent.left:
                    z = z.parent
                    root = right_rotate(root, z)
                z.parent.color = 'B'
                g.color = 'R'
                root = left_rotate(root, g)
    root.color = 'B'
    return root

def rb_delete(root, key):
    z = root
    while z is not None and z.key != key:
        z = z.left if key < z.key else z.right
    if z is None:
        return root
    if z.left is not None and z.right is not None:
        s = find_min(z.right)
        z.key = s.key
        z = s
    child = z.left if z.left is not None else z.right
    p = z.parent
    removed = z.color
    if child is not None:
        child.parent = p
    if p is None:
        root = child
    elif p.left == z:
        p.left = child
    else:
        p.right = child
    if removed == 'B':
        x = child
        while x != root and color_of(x) == 'B':
            if x == p.left:
                b = p.right
                if color_of(b) == 'R':
                    b.color = 'B'
                    p.color = 'R'
                    root = left_rotate(root, p)
                    b = p.right
                if color_of(b.left) == 'B' and color_of(b.right) == 'B':
                    b.color = 'R'
                    x = p
                    p = x.parent
                else:
                    if color_of(b.right) == 'B':
                        b.left.color = 'B'
                        b.color = 'R'
                        root = right_rotate(root, b)
                        b = p.right
                    b.color = p.color
                    p.color = 'B'
                    b.right.color = 'B'
                    root = left_rotate(root, p)
                    x = root
            else:
                b = p.left
                if color_of(b) == 'R':
                    b.color = 'B'
                    p.color = 'R'
                    root = right_rotate(root, p)
                    b = p.left
                if color_of(b.left) == 'B' and color_of(b.right) == 'B':
                    b.color = 'R'
                    x = p
                    p = x.parent
                else:
                    if color_of(b.left) == 'B':
                        b.right.color = 'B'
                        b.color = 'R'
                        root = left_rotate(root, b)
                        b = p.left
                    b.color = p.color
                    p.color = 'B'
                    b.left.color = 'B'
                    root = right_rotate(root, p)
                    x = root
        if x is not None:
            x.color = 'B'
    if root is not None:
        root.color = 'B'
    return root

bst = None
rb = None
for v in values:
    bst = bst_insert(bst, v)
    rb = rb_insert(rb, v)

for name, tree in [('BST', bst), ('RB', rb)]:
    ino, pre, post = [], [], []
    inorder(tree, ino)
    preorder(tree, pre)
    postorder(tree, post)
    print(name, 'height:', height(tree))
    print(name, 'inorder:', ino)
    print(name, 'preorder:', pre)
    print(name, 'postorder:', post)

for k in [75, 5, 19]:
    bst = bst_delete(bst, k)
res = []
preorder(bst, res)
print('BST after delete 75, 5, 19 (preorder):', res)

for k in [43, 62, 66]:
    rb = rb_delete(rb, k)
res = []
preorder(rb, res)
print('RB after delete 43, 62, 66 (preorder):', res)
