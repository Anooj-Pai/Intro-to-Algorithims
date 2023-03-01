import sys

# Step 1: Create GR
GR = {}
with open(sys.argv[1]) as f:
    for line in f:
        u, v = map(int, line.split())
        if v not in GR:
            GR[v] = []
        GR[v].append(u)

# Step 2: Compute DFS interval on GR for each node
post_order = []
visited = set()


def dfs_post(u):
    visited.add(u)
    for v in GR.get(u, []):
        if v not in visited:
            dfs_post(v)
    post_order.append(u)


for u in GR:
    if u not in visited:
        dfs_post(u)

# Step 3: Output strongly connected components
visited = set()


def dfs_scc(u, component):
    visited.add(u)
    component.append(u)
    for v in G.get(u, []):
        if v not in visited:
            dfs_scc(v, component)


G = {}
with open(sys.argv[1]) as f:
    for line in f:
        u, v = map(int, line.split())
        if u not in G:
            G[u] = []
        G[u].append(v)

sccs = []
for u in reversed(post_order):
    if u not in visited:
        component = []
        dfs_scc(u, component)
        sccs.append(component)

# Output all strongly connected components
for scc in sccs:
    print(' '.join(str(node) for node in scc))
