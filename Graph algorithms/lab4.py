from queue import Queue
from graph import Graph


def highest_cost_path(graph, source, target):
        sorted_list = predecessor_counting(graph)
        if sorted_list == None:
            return None
        dist={}
        for vertex in range(0, graph.get_vertices_number()):
            dist[vertex] = -100000
        dist[source] = 0
        for vertex in sorted_list:
            for neighbour in graph.get_outbound_neighbors(int(vertex)):
                if dist[neighbour] < dist[int(vertex)]+int(graph.get_associated_information(int(vertex), int(neighbour))):
                    if dist[vertex] == -100000:
                        dist[neighbour] = graph.get_associated_information(vertex, neighbour) - 1
                    else:
                        dist[neighbour] = dist[vertex] + graph.get_associated_information(vertex, neighbour)                
        return dist


def predecessor_counting(graph):
    sorted_list = []
    queue = Queue()
    count = {}
    for vertex in graph.get_verteces():
        count[vertex] = graph.get_in_degree(vertex)        
        if count[vertex] == 0:
            queue.put(vertex)
    
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)
        for neighbour in graph.get_outbound_neighbors(vertex):
            count[neighbour] = count[neighbour] - 1
            if count[neighbour] == 0:
                queue.put(neighbour)
    
    if len(sorted_list) < graph.get_vertices_number():
        sorted_list = None
    
    print(sorted_list)
    return sorted_list


def init_graph(graph):
    graph.add_edge(0,1,1)
    graph.add_edge(0,3,4)
    graph.add_edge(1,2,3)
    graph.add_edge(3,4,1)
    graph.add_edge(2,5,1)
    graph.add_edge(4,5,2)
    return graph


def test_topological_sorting():
    test_graph = Graph(6)
    init_graph(test_graph)
    sorted_list = predecessor_counting(test_graph)

    print(sorted_list)


def test_highest_cost_path():
    test_graph = Graph(6)
    init_graph(test_graph)

    print(highest_cost_path(test_graph, 0, 5))


if __name__ == "__main__":
    test_topological_sorting()

    test_highest_cost_path()