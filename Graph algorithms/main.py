from graph import Graph
from graph import read_graph_from_file
from graph import save_graph_to_file
from graph import create_random_graph
from lab2 import shortest_path_reversed_BFS
from lab3 import minimum_cost_walk
from lab4 import predecessor_counting
from lab4 import highest_cost_path
from lab4 import highest_cost_path


def get_vertices_number(graph):
    verteces_number = graph.get_vertices_number()
    print('Number of verteces: ',verteces_number)

def get_edges_number(graph):
    edges_number = graph.get_edges_number()
    print('Number of edges: ',edges_number)

def get_verteces(graph):
    verteces = graph.get_verteces()
    print('Verteces:')
    print(verteces)

def get_outbound_neighbors(graph):
    vertex = int(input('Vertex = '))
    neighbors = graph.get_outbound_neighbors(vertex)
    print('Outbound neighbors:')
    print(neighbors)

def get_inbound_neighbors(graph):
    vertex = int(input('Vertex = '))
    neighbors = graph.get_inbound_neighbors(vertex)
    print('Inbound neighbors:')
    print(neighbors)

def is_edge(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    is_edge_boolean = graph.is_edge(source_vertex,target_vertex)
    if is_edge_boolean == True:
        print('Edge exists!')
    else:
        print('Edge does not exist!')

def add_vertex(graph):
    vertex = int(input('Vertex = '))
    graph.add_vertex(vertex)
    print('Vertex added!')

def add_edge(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    cost = int(input('Cost = '))
    graph.add_edge(source_vertex,target_vertex,cost)
    print('Edge added!')

def get_in_degree(graph):
    vertex = int(input('Vertex = '))
    degree = graph.get_in_degree(vertex)
    print('Indegree = ',degree)

def get_out_degree(graph):
    vertex = int(input('Vertex = '))
    degree = graph.get_out_degree(vertex)
    print('Outdegree = ',degree)

def get_cost(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    cost = graph.get_associated_information(source_vertex,target_vertex)
    if cost == False:
        print('Edge does not exist!')
    else:
        print('Cost = ',cost)

def update_cost(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    new_cost = int(input('New cost = '))
    operation_performed = graph.update_associated_information(source_vertex,target_vertex,new_cost)
    if operation_performed == False:
        print('Edge does not exist!')
    else:
        print('Updated!')

def remove_vertex(graph):
    vertex = int(input('Vertex = '))
    operation_performed = graph.remove_vertex(vertex)
    if operation_performed == False:
        print('Vertex does not exist!')
    else:
        print('Vertex removed!')

def remove_edge(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    operation_performed = graph.remove_edge(source_vertex,target_vertex)
    if operation_performed == False:
        print('Edge does not exist!')
    else:
        print('Edge removed!')

def save_to_file(graph):
    file_name = input('File name: ')
    save_graph_to_file(graph,file_name)
    print('File saved!')

def read_from_file(graph):
    file_name = input('File name: ')
    try:
        new_graph = read_graph_from_file(file_name)
        graph.load(new_graph)
        print(graph.get_len())
    except:
        print('')

def shortest_path_reversed(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    path = shortest_path_reversed_BFS(graph, source_vertex, target_vertex)
    if len(path) == 0:
        print('There is no path between the given verteces!')
    else:
        print(path)

def lowest_cost_walk(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    minimum_cost_walk(graph, source_vertex, target_vertex)

def highest_cost_path_print(graph):
    source_vertex = int(input('Source vertex = '))
    target_vertex = int(input('Target vertex = '))
    distances = highest_cost_path(graph, source_vertex, target_vertex)
    if distances[target_vertex] == None:
        print("Not a DAG!")
    else:
        if distances[target_vertex] == -100000:
            print("There is no path between the verteces!")
        else:
            print("The highest cost path is:", distances[target_vertex])


def print_menu_options():
    print(
        '''
        1: Print the number of verteces
        2: Print the number of edges
        3: Print verteces
        4: Print the outbound neighbors
        5: Print the inbound neighbors
        6: Check existance of edge
        7: Add vertex
        8: Add edge
        9: Print indegree of vertex
        10: Print outdegree of vertex
        11: Print cost
        12: Update cost
        13: Delete vertex
        14: Delete edge
        15: Save the graph to a file
        16: Load a graph from a file
        17: Print shortest path
        18: Bellman-Ford lowest cost walk
        19: Highest cost path (predecessor counting) 
        ''')

def run_menu():
    # gets user input and calls the required method
    graph_object = Graph(0)
    operations = {1:get_vertices_number,2:get_edges_number,3:get_verteces,4:get_outbound_neighbors,
    5:get_inbound_neighbors,6:is_edge,7:add_vertex,8:add_edge,9:get_in_degree,10:get_out_degree,11:get_cost,
    12:update_cost,13:remove_vertex,14:remove_edge,15:save_to_file,16:read_from_file,17:shortest_path_reversed,
    18:lowest_cost_walk, 19:highest_cost_path_print}

    while True:
        try:
            print_menu_options()
            option=int(input('Option: '))
            print('\n')
            operations[option](graph_object)
        except:
           print('Invalid user input!')


def create_random_graphs():
    # create the random graphs
    random_graph = Graph(0)
    random_graph = create_random_graph(7,20)
    save_graph_to_file(random_graph,'random_graph1.txt')
    random_graph = create_random_graph(6,40)
    save_graph_to_file(random_graph,'random_graph2.txt')

def test_graph():
    #creating a graph object and reading graph1k (graph.txt)
    graph = Graph(0)
    graph = read_graph_from_file('graph.txt')
    
    #testing graph
    assert(graph.get_edges_number()==4000)
    assert(graph.is_edge(0,908)==True)
    assert(graph.get_associated_information(0,908)==52)
    assert(graph.get_in_degree(581)==8)
    assert(graph.get_out_degree(0)==7)
    assert(graph.get_associated_information(2,900)==20)
    graph.update_associated_information(2,900,153)
    assert(graph.get_associated_information(2,900)==153)
    print("All tests passed!")


if __name__ == "__main__":
    #call_tests
    test_graph()

    #call menu
    run_menu()