from queue import Queue
from graph import Graph


def is_path_BFS(graph,source_vertex,target_vertex):
    next_to_visit = Queue()
    visited = set()
    next_to_visit.put(source_vertex)
    while not next_to_visit.empty():
        current_vertex = next_to_visit.get()
        if current_vertex == target_vertex:
            # vertex found
            return True
        if current_vertex not in visited:
            visited.add(current_vertex)
        # adding children to next to visit
        for child in graph.get_outbound_neighbors(current_vertex):
            if child not in visited:
                next_to_visit.put(child) 
    return False


def shortest_path_BFS(graph, source_vertex, target_vertex):
    queue = Queue()
    visited = set()
    # enqueue the source vertex
    queue.put((source_vertex,[source_vertex]))

    while not queue.empty():
        # get the current vertrex and it's path from the queue
        current_vertex, path = queue.get()
        visited.add(current_vertex)
        # parse all the children of the node
        for child in graph.get_outbound_neighbors(current_vertex):
            # if found return the path
            if child == target_vertex:
                return path + [target_vertex]
            else:
                # if node has not been visited it gets added to the queue
                if child not in visited:
                    visited.add(child)
                    queue.put((child, path + [child]))
    # if no path is found then return empty list
    return []

#----------------------------------------------------------------------------------------

def shortest_path_reversed_BFS(graph,source_vertex,target_vertex):
    # returns the shortest path between 2 verteces, but parses the graph from the target
    # vertex towards the source vertex, return an empty list if path does not exist
    # graph: an object of graph type
    # source_vertex: the vertex from wich the supposed path starts
    # target_vertex: the vertex with wich the supposed path ends
    # returns: a list containing the shortest path, the list is empty if not found
    queue = Queue()
    visited = set()
    # enqueue the target vertex
    queue.put((target_vertex,[target_vertex]))

    while not queue.empty():
        # get the current vertex and it's path
        current_vertex, path = queue.get()
        visited.add(current_vertex)
        # parse all it's inbound neighbors
        for inbound in graph.get_inbound_neighbors(current_vertex):
            # if found return the path
            if inbound == source_vertex:
                return  [source_vertex] + path
            else:
                # if node has not been visited it gets added to the queue
                if inbound not in visited:
                    visited.add(inbound)
                    queue.put((inbound,[inbound] + path))
    # if no path is found then return empty list
    return []

def test_BFS():
    graph = Graph(10)
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,2)
    graph.add_edge(2,3,3)
    graph.add_edge(3,4,4)
    graph.add_edge(4,5,5)
    graph.add_edge(6,5,1)
    graph.add_edge(5,1,2)
    graph.add_edge(1,4,3)
    graph.add_edge(1,7,4)
    graph.add_edge(1,8,5)
    graph.add_edge(8,9,5)

    # testing is_path_BFS
    assert(is_path_BFS(graph,6,9) == True)
    assert(is_path_BFS(graph,6,0) == False)
    # testing shortest_path_BFS
    assert(shortest_path_BFS(graph,6,9) == [6,5,1,8,9])
    assert(shortest_path_BFS(graph,6,0) == [])
    # testing shortest_path_reversed_BFS
    assert(shortest_path_reversed_BFS(graph,6,9) == [6,5,1,8,9])
    assert(shortest_path_reversed_BFS(graph,6,0) == [])

if __name__ == "__main__":
    test_BFS()