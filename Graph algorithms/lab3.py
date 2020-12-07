from graph import Graph
from graph import read_graph_from_file
import sys


def bellman_ford(graph,source_vertex,target_vertex):
    distances = {}
    previous = {}
    # initialise distances
    for vertex in graph.get_verteces():
        distances[vertex] = float('inf')
    # relax edges
    distances[source_vertex] = 0
    changed = True
    while changed:
        changed = False
        for edge_source in graph.get_verteces():
            for edge_target in graph.get_outbound_neighbors(edge_source):
                if distances[edge_target] > distances[edge_source] + graph.get_associated_information(edge_source,edge_target):
                    distances[edge_target] = distances[edge_source] + graph.get_associated_information(edge_source,edge_target)
                    previous[edge_target] = edge_source
                    changed = True
    # check negative cycles
    for edge_source in graph.get_verteces():
            for edge_target in graph.get_outbound_neighbors(edge_source):
                if distances[edge_target] > distances[edge_source] + graph.get_associated_information(edge_source,edge_target):
                    raise("Negative cycle!")

    return distances, previous


def minimum_cost_walk(graph,source_vertex,target_vertex):
    try:
        distances, previous = bellman_ford(graph,source_vertex,target_vertex)
    except Exception as caught_exception:
        print(caught_exception)
    else:
        if distances[target_vertex] == float('inf'):
            print('Walk does not exist!')
        else:
            # building the walk
            walk = []
            current_vertex = target_vertex
            walk.append(target_vertex)
            while current_vertex != source_vertex:
                previous_vertex = previous[current_vertex]
                walk.append(previous_vertex)
                current_vertex = previous_vertex

            # printing result
            walk_string = ""
            for i in range(len(walk)):
                #walk_string = walk_string + ' -' + str(distances[walk[len(walk) - i - 1]]) + '- '
                walk_string = walk_string + str(walk[len(walk) - i - 1]) + ', '
            walk_string = walk_string + ': ' + str(distances[target_vertex])
            print(walk_string)


def file_minimum_cost_walks(graph,source_vertex,target_vertex,output_file):
    try:
        distances, previous = bellman_ford(graph,source_vertex,target_vertex)
    except Exception as caught_exception:
        print(caught_exception)
    else:
        if distances[target_vertex] == float('inf'):
            print('Walk does not exist!')
        else:
            # building the walk
            walk = []
            current_vertex = target_vertex
            walk.append(target_vertex)
            while current_vertex != source_vertex:
                previous_vertex = previous[current_vertex]
                walk.append(previous_vertex)
                current_vertex = previous_vertex
            # write to file
            walk_string = ""
            for i in range(len(walk)):
                #walk_string = walk_string + ' -' + str(distances[walk[len(walk) - i - 1]]) + '- '
                walk_string = walk_string + str(walk[len(walk) - i - 1]) + ', '
            walk_string = walk_string + ': ' + str(distances[target_vertex]) + '\n'
            output_file.write(walk_string)


def write_to_file():
    # runs the required example for the graph files
    file_name = 'results.txt'
    output_file = open(file_name,'w')
    # graph1k
    graph = read_graph_from_file('graph.txt')
    output_file.write('Graph1k:\n')
    file_minimum_cost_walks(graph,1,100,output_file)
    file_minimum_cost_walks(graph,100,1,output_file)
    #graph10K
    graph = read_graph_from_file('graph10k.txt')
    output_file.write('Graph10k:\n')
    file_minimum_cost_walks(graph,1,100,output_file)
    file_minimum_cost_walks(graph,100,1,output_file)
    #graph100K
    graph = read_graph_from_file('graph100k.txt')
    output_file.write('Graph100k:\n')
    file_minimum_cost_walks(graph,1,100,output_file)
    file_minimum_cost_walks(graph,100,1,output_file)


def init_graph(graph):
    graph.add_edge(0,1,5)
    graph.add_edge(0,2,20)
    graph.add_edge(1,2,10)
    graph.add_edge(1,3,30)
    graph.add_edge(2,3,5)
    return graph


if __name__ == "__main__":
    # small example
    nr_of_verteces = 4
    source_vertex = 0
    target_vertex = 3
    graph = Graph(nr_of_verteces)
    graph = init_graph(graph)

    minimum_cost_walk(graph, source_vertex, target_vertex)

    # graph files
    write_to_file()
