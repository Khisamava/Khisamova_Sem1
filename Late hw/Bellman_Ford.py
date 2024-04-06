def read_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph

def read_list():
    print("Введите количество ребер q:")
    edge_list = read_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[2])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2], edge[3], edge[4])])
    return graph_dict

def Bellman_Ford(graph, start_vertex):
    dist = {vertex: float('inf') for vertex in graph}
    dist[start_vertex] = 0
    n = len(graph)
    for _ in range(n - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Граф сдержит отрицательный цикл")
                return

    return dist

graph = read_list()
f = Bellman_Ford(graph, 1)
print(f)
