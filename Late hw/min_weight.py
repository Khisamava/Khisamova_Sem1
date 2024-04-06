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


def Min_weight(graph, v):
    # в этой функции выводиться минимальное ребро на самом неоптимальном пути, т.е.
    d = {}
    w = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('-inf')
        w[key] = float('inf')
    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph[c[1]]:
            # if neigh[0] not in end:
            if (d[c[1]] + neigh[1]) > d[neigh[0]]:
                d[neigh[0]] = (d[c[1]] + neigh[1])
                if w[c[1]] > neigh[1]:
                    w[neigh[0]] = neigh[1]
                else:
                    w[neigh[0]] = w[c[1]]

            visited.append(neigh[::-1])


    return d, w


def Min_weight2(graph, v):
    # Эта функция выводит в качетсве оптимального пути, минимальное ребро из максимальных ребер на
    # на каждом из путей
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = [0]

    d[v] = [0]
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph[c[1]]:
            # if neigh[0] not in end:
            if (d[c[1]][-1] + neigh[1]) > d[neigh[0]][-1]:
                if d[c[1]][0] < neigh[1]:
                    d[neigh[0]].append(neigh[1])
                    d[neigh[0]].sort()
                else:
                    d[neigh[0]].append(d[c[1]][-1])
                    d[neigh[0]].sort()
            visited.append(neigh[::-1])

    res = {}
    for key in d:
        if len(d[key]) == 1:
            res[key] = float('infinity')
        else:
            res[key] = int(d[key][1])

    res[v] = 0

    return res


graph = read_list()
d, w = Min_weight(graph, 1)
m = Min_weight2(graph, 1)
print(graph)
print(d)
print(w)