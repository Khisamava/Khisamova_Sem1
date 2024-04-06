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


def Colors(graph, v):
    d = {}
    colors = {}
    visited = []
    end = []
    for index in graph.keys():
        d[index] = float('infinity')
        colors[index] = float('infinity')
    d[v] = 0
    colors[v] = 0
    visited.append([0, 0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[2])
        for neigh in graph[c[2]]:
            list_c = list(list(graph[c[2]])[0])
            if neigh[1] not in end:
                if list_c[0] == neigh[2]:
                    colors[neigh[1]] = colors[c[2]]
                    if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                        d[neigh[1]] = (d[c[2]] + neigh[3])
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)
                else:
                    if colors[neigh[1]] == float('inf'):
                        colors[neigh[1]] = colors[c[2]] + 1
                        if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                            d[neigh[1]] = (d[c[2]] + neigh[3])
                    if colors[neigh[1]] <= colors[c[2]]:
                        continue
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)

    return d, colors

graph = read_list()
print(graph)
print(graph[1])
d, c = Colors(graph, 1)
print(d)
print(c)
