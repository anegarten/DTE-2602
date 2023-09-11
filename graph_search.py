

def breadth_first_traverse(graph,start_node):
    """ Traverse a graph breadth-first
    
    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)

    # Returns:
    came_from:  Dictionary where key = node, value = previous node during traversal.
                If node B was discovered from node A, came_from[B] == A.
                The dict includes the start node, came_from[start_node] == None.
                The keys in the came_from dict also acts as a 
                list of all the nodes that have been discovered.
    """


    queue_frontier = []
    came_from = {}

    queue_frontier.append(start_node)
    came_from[start_node] = None

    while queue_frontier:
        current_node = queue_frontier.pop(0)
        for i in range(len(graph[current_node])):
            if graph[current_node][i] not in came_from:
                queue_frontier.append(graph[current_node][i])
                came_from[graph[current_node][i]] = current_node

    return came_from


def path_backtrack(start_node,end_node,came_from):
    """ Construct path from start to end node based on previous traversal 
    
    # Arguments:
    start_node:     Start node (unique identifier)
    end_node:       End node (unique identifier)
                    end_node must be present as a key in came_from
                    (i.e. it is reachable from start_node) 
    came_from:      Dict from previous traversal - see breadth_first_traverse()
                    key = node, value = previous node

    # Returns:
    path:           List, starting with start_node and ending with end_node,
                    containing all nodes on the path taken from start to end     
    """

    print(came_from)


        

graph = {"A": ["B", "C"],
         "B": ["D"],
         "C": ["E"]}

graph2 = {(1, 1): [(2, 1), (1, 2)],
          (1, 2): [(1, 1), (1, 3)],
          (1, 3): [(1, 2), (2, 3), (1, 4)],
          (1, 4): [(1, 3), (1, 5)],
          (1, 5): [(1, 4), (2, 5)],
          (2, 1): [(1, 1)],
          (2, 3): [(3, 3), (1, 3)],
          (2, 5): [(1, 5)],
          (3, 3): [(3, 4), (2, 3)],
          (3, 4): [(3, 3)]}


came_from = breadth_first_traverse(graph2, (1,4))
path_backtrack((1,3), (2,1), came_from[1,3])
        


def get_reachable_nodes(graph,start_node):
    """ Determine which nodes in a graph are reachable from a given start node

    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)
    
    # Returns:
    reachable_nodes:    A set (using set data type) of all the nodes
                        that are reachable from the start node.
    """
    pass


def breadth_first_search(graph,start_node,end_node):
    """ Search a graph for a single node breadth-first
    
    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)
    end_node:   End node (valid key in graph)

    # Returns:
    came_from:  Dictionary where key = node, value = previous node during search.
                If node B was discovered from node A, came_from[B] == A.
                The dict includes the start node, came_from[start_node] == None.
                The keys in the came_from dict also acts as a 
                list of all the nodes that have been discovered.
    path:       List, starting with start_node and ending with end_node,
                containing all nodes on the path taken from start to end
                If the end node is not reachable from the start node,
                path = None.
    """
    

