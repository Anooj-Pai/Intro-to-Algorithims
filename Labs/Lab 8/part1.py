def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[y] = x
        rank[x] += 1


V = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
E = [("A", "B", 10), ("A", "C", 12), ("B", "C", 9), ("B", "D", 8), ("C", "E", 3),
     ("C", "F", 1), ("D", "E", 7), ("D", "G", 8), ("D", "H", 5), ("E", "F", 3), ("F", "H", 6), ("G", "H", 9), ("G", "I", 2), ("H", "I", 11)]
U = ["A", "E", "F"]

if __name__ == "__main__":
    Vp = [v for v in V if v not in U]
    Ep = [edge for edge in E if edge[0] in Vp and edge[1] in Vp]

    E_sorted = sorted(Ep, key=lambda x: x[2])
    parent = [ord(v) - 65 for v in V]
    rank = [0 for i in range(len(V))]
    Mst = []
    for edge in E_sorted:
        x = find(parent, ord(edge[0]) - 65)
        y = find(parent, ord(edge[1]) - 65)
        if x != y:
            Mst.append(edge)
            union(parent, rank, x, y)
    E2 = sorted([edge for edge in E if edge[0] in U and edge[1]
                not in U or edge[1] in U and edge[0] not in U], key=lambda x: x[2])
    for edge in E2:
        x = find(parent, ord(edge[0]) - 65)
        y = find(parent, ord(edge[1]) - 65)
        if x != y:
            Mst.append(edge)
            union(parent, rank, x, y)
    totalWeight = sum([edge[2] for edge in Mst])
    for edge in Mst:
        print(edge)
