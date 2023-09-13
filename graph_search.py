

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

    path = []

    current_node = end_node

    while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
    

    return path[::-1]


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
    came_from = breadth_first_traverse(graph, start_node)
    nodes_discovered = set()
    for key in came_from:
        nodes_discovered.add(key)
    
    return nodes_discovered



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

    queue_frontier_search = []
    came_from_search = {}

    queue_frontier_search.append(start_node)
    came_from_search[start_node] = None

    while queue_frontier_search:
        current_node = queue_frontier_search.pop(0)
        if current_node == end_node:
            break
        for i in range(len(graph[current_node])):
            if graph[current_node][i] not in came_from_search:
                queue_frontier_search.append(graph[current_node][i])
                came_from_search[graph[current_node][i]] = current_node

    if current_node == end_node:
        shortest_path = []
        for key in came_from_search:
            shortest_path.append(key)
    else:
        shortest_path = None

    return came_from_search, shortest_path


graph = {'A':['B'],'B':['A','C'],'C':['B']}

graph2 = {(1, 1): [(2, 1), (1, 2)],
          (1, 2): [(1, 1)],
          (2, 1): [(1, 1)]}

shortest_path = breadth_first_search(graph, 'B', 'A')
print(shortest_path)

