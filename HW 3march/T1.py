def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict

def DFS(graph, v, visited=[]):
        print(v)
        visited.append(v)
        for neigh in graph[v]:
            if neigh not in visited:
                DFS(graph, neigh, visited)

def has_cycle(graph, v, visited=[]):
        result = False
        for neigh in graph[v]:
            if neigh in visited:
                result = True
                return result

            visited.append(v)

            if result == False:
                result = has_cycle(graph, neigh, visited)
                visited = []
        return result

def DFS_stack(graph, v, visited=[]):

        stack = []
        visited.append(v)
        stack.append(v)
        while stack:
            v = stack.pop()
            print(v)
            for neigh in graph[v]:
                if neigh not in visited:
                    visited.append(neigh)
                    stack.append(neigh)

def topologicalSortUtil(graph, v, visited, stack):
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                topologicalSortUtil(graph, i, visited, stack)

        stack.insert(0, v)

def topologicalSort(graph):
        V_sum = len(graph)
        visited = [False] * V_sum
        stack = []

        for i in range(V_sum):
            if visited[i] == False:
                topologicalSortUtil(graph, i, visited, stack)

        return stack

def count_paths(graph, start, end):
        paths = {v: 0 for v in graph}
        paths[start] = 1

        order: list = topologicalSort(graph)

        for u in order:
            for v in graph[u]:
                paths[v] += paths[u]

        return paths[end]

def is_the_vertex_an_ancestor(graph):
        print('Введите количество запросов:')
        q = int(input())
        for i in range(q):
            v, u = map(int, input().split())
            print("Да" if ancestor_or_not(graph, v, u) else "Нет")

def ancestor_or_not(graph, v, u):
        if v in graph:
            for child in graph[v]:
                if child == u or ancestor_or_not(graph, child, u):
                    return True
        return False

graph = read_graph_as_neigh_list()
print(topologicalSort(graph))
print(count_paths(graph, 0, 3))
is_the_vertex_an_ancestor(graph)
