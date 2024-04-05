def read_adjacency_list():
    n, m = map(int, input().split())
    adj_list = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        adj_list[u - 1].append(v - 1)
    print('graph is full')
    return adj_list




graph = read_adjacency_list()
vis = [False for i in range(len(graph))]
timer = [0]
t_in = [0 for j in range(len(graph))]
t_out = [0 for k in range(len(graph))]


def dfs(u):
    if vis[u]:
        return
    vis[u] = True
    t_in[u] = timer[0]
    timer[0] += 1
    for v in graph[u]:
        dfs(v)
    t_out[u] = timer[0]


def query(u, v):
    return t_in[u] <= t_in[v] and t_out[u] >= t_out[v]


n = int(input())
for i in range(n):
    u, v = map(int, input().split())
    if query(u, v):
        print('Yes')
    else:
        print('No)')
