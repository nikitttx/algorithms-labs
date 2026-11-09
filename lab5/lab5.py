edges = [
    (8, 1, 2), (1, 1, 3), (5, 1, 4), (3, 1, 5),
    (6, 2, 5), (1, 2, 6), (6, 3, 4), (7, 3, 6),
    (3, 3, 8), (2, 4, 5), (9, 5, 7), (3, 6, 7),
    (1, 6, 8), (4, 7, 8)
]
n = 8
matrix = []
for i in range(n):
    matrix.append([None] * n)
for w, u, v in edges:
    matrix[u - 1][v - 1] = w
    matrix[v - 1][u - 1] = w


def prim(matrix):
    n = len(matrix)
    selected = [False] * n
    distance = [float('inf')] * n
    parent = [-1] * n
    distance[0] = 0
    tree = []
    total = 0
    for step in range(n):
        v = -1
        for i in range(n):
            if not selected[i]:
                if v == -1 or distance[i] < distance[v]:
                    v = i
        selected[v] = True
        if parent[v] != -1:
            tree.append((parent[v] + 1, v + 1, distance[v]))
            total += distance[v]
        for u in range(n):
            w = matrix[v][u]
            if w is not None and not selected[u]:
                if w < distance[u]:
                    distance[u] = w
                    parent[u] = v
    return tree, total


def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v


def kruskal(edges, n):
    parent = list(range(n + 1))
    tree = []
    total = 0
    for w, u, v in sorted(edges):
        a = find(parent, u)
        b = find(parent, v)
        if a != b:
            parent[a] = b
            tree.append((u, v, w))
            total += w
            if len(tree) == n - 1:
                break
    return tree, total


print('Алгоритм Прима:')
tree, total = prim(matrix)
for u, v, w in tree:
    print(u, '-', v, ':', w)
print('Загальна вага:', total)

print('Алгоритм Крускала:')
tree, total = kruskal(edges, n)
for u, v, w in tree:
    print(u, '-', v, ':', w)
print('Загальна вага:', total)
