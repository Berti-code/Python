import random


class Graph:
    def __init__(self,verteces_number):
        self.__number_of_vertices = verteces_number
        self.__number_of_edges = 0
        self.__graph_edges_dictionary = {}
        self.__graph_associated_information = {}
        for i in range(verteces_number):
            self.__graph_edges_dictionary[i] = []
            self.__graph_associated_information[i] = []

    def load(self,graph):
        self.__number_of_vertices = graph.__number_of_vertices
        self.__number_of_edges = graph.__number_of_edges
        self.__graph_edges_dictionary = graph.__graph_edges_dictionary
        self.__graph_associated_information = graph.__graph_associated_information

    def get_vertices_number(self):
        # returns the number of vertices
        return self.__number_of_vertices

    def get_edges_number(self):
        # returns the number of edges
        return self.__number_of_edges

    def get_verteces(self):
        # returns a list with all the verteces
        return self.__graph_edges_dictionary.keys()

    def get_outbound_neighbors(self,vertex):
        # returns a list with the verteces that are outbound neighbors for the given vertex
        return self.__graph_edges_dictionary[vertex]

    def get_inbound_neighbors(self,vertex):
        # returns a list with the verteces that are inbound neighbors for the given vertex
        inbound_neighbors = []
        for current_vertex in self.__graph_edges_dictionary.keys():
            if vertex in self.__graph_edges_dictionary[current_vertex]:
                inbound_neighbors.append(current_vertex)
        return inbound_neighbors

    def is_edge(self,source_vertex,target_vertex):
        # checks if there is an edge between 2 verteces
        if source_vertex in self.__graph_edges_dictionary.keys():
            if target_vertex in self.__graph_edges_dictionary[source_vertex]:
                return True
        return False

    def add_vertex(self,vertex):
        # adds a vertex to the graph
        if vertex not in self.__graph_edges_dictionary.keys():
            self.__graph_edges_dictionary[vertex]=[]
            self.__graph_associated_information[vertex]=[]
            self.__number_of_vertices += 1

    def add_edge(self,source_vertex,target_vertex,associated_information):
        # adds an edge to the graph representation
        if source_vertex not in self.__graph_edges_dictionary.keys():
            self.add_vertex(source_vertex)
        if target_vertex not in self.__graph_edges_dictionary.keys():
            self.add_vertex(target_vertex)
        self.__graph_edges_dictionary[source_vertex].append(target_vertex)
        self.__graph_associated_information[source_vertex].append(associated_information)    
        self.__number_of_edges += 1

    def get_in_degree(self,vertex):
        # returns the in degree of a vertex
        in_degree = 0
        for index in self.__graph_edges_dictionary.keys():
            if vertex in self.__graph_edges_dictionary[index]:
                in_degree += 1
        return in_degree

    def get_out_degree(self,vertex):
        return len(self.__graph_edges_dictionary[vertex])

    def get_associated_information(self,source_vertex,target_vertex):
        # returns the associated information of an edge determined by 2 verteces
        if source_vertex in self.__graph_edges_dictionary.keys():
            if target_vertex in self.__graph_edges_dictionary[source_vertex]:
                target_vertex_index = self.__graph_edges_dictionary[source_vertex].index(target_vertex)
                return self.__graph_associated_information[source_vertex][target_vertex_index]
        return False

    def update_associated_information(self,source_vertex,target_vertex,associated_information):
        # updates the associated information of an edge determined by 2 verteces
        if source_vertex in self.__graph_edges_dictionary.keys():
            if target_vertex in self.__graph_edges_dictionary[source_vertex]:
                target_vertex_index = self.__graph_edges_dictionary[source_vertex].index(target_vertex)
                self.__graph_associated_information[source_vertex][target_vertex_index] = associated_information
                return True
        return False

    def remove_vertex(self,vertex):
        # removes given vertex
        if vertex in self.__graph_edges_dictionary.keys():
            number_of_outbound_neighbors = len(self.__graph_edges_dictionary[vertex])
            self.__graph_associated_information.pop(vertex)
            self.__graph_edges_dictionary.pop(vertex)
            self.__number_of_vertices -= 1
            self.__number_of_edges -= number_of_outbound_neighbors
            return True
        return False

    def remove_edge(self,source_vertex,target_vertex):
        # removes given edge
        if source_vertex in self.__graph_edges_dictionary.keys():
            if target_vertex in self.__graph_edges_dictionary[source_vertex]:
                self.__graph_associated_information[source_vertex].pop(target_vertex)
                self.__graph_edges_dictionary[source_vertex].pop(target_vertex)
                self.__number_of_edges -= 1
                return True
        return False


# function for creating a graph file
def save_graph_to_file(graph,filename):
    # input: filename,graph_dictionary,graph_associated_information
    # output: creates a .txt file containing the representation of a graph
    f=open(filename,'w')
    verteces = graph.get_verteces()
    number_of_edges , number_of_vertices = graph.get_edges_number() , graph.get_vertices_number()
    first_line = ''
    first_line = str(number_of_vertices) + ' ' + str(number_of_edges) + '\n'
    f.write(first_line)
    for vertex in verteces:
        line = ''
        outbound_neighbors = graph.get_outbound_neighbors(vertex)
        for index in range(len(outbound_neighbors)):
            line = str(vertex) + ' ' + str(outbound_neighbors[index]) + ' ' + str(outbound_neighbors[index]) + '\n'
            f.write(line)


# function for reading a graph from a file:
def read_graph_from_file(file_name):
    # input: filename
    # returns a graph object
    open_for_read = 'r'
    f = open(file_name, open_for_read)
    line = f.readline()
    [number_of_vertices , number_of_edges] = line.split()
    number_of_vertices = int(number_of_vertices)
    number_of_edges = int(number_of_edges)
    graph = Graph(number_of_vertices)

    for index in range(number_of_edges):
        line = f.readline()
        source_vertex,target_vertex,associated_information = line.split()
        source_vertex = int(source_vertex)
        target_vertex = int(target_vertex)
        associated_information = int(associated_information)
        graph.add_edge(source_vertex,target_vertex,associated_information)

    return graph


# function for creating a random graph
def create_random_graph(number_of_vertices,number_of_edges):
    # input: number_of_vertices,number_of_edges
    # returns a graph object
    # pre: number_of_edges <= n*(n-1)
    # raises: ValueError if pre not met
    if(number_of_edges > number_of_vertices*(number_of_vertices-1)):
        raise ValueError('Precondition not met!')
    graph = Graph(number_of_vertices)
    possible_edges = []
    
    # initialising possible_edges with all the possible combinations of verteces
    for i in range(0,number_of_vertices-1,1):
        for j in range(i+1,number_of_vertices,1):
            possible_edges.append([i,j])
        
    # chosing a random edge from possible_edges for number_of_edges times,
    # each time that certain edge is eliminated from the list of possible_edges
    for i in range(number_of_edges):
        random_edge = random.choice(possible_edges)
        graph.add_edge(random_edge[0],random_edge[1],random.randrange(0,number_of_vertices*2))
    return graph