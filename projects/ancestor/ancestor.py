from util import Queue
from util import Graph


# UPER
    # Understand
        # Write a function that returns the earliest known ancestor (eka)
            # While:
                # having a dataset and and ID of an individual in that set
                # eka being at the farthest distance form individual input
            # Notes:
                # if eka > 1, return eka with lower numeric id
                # if ancestors = 0, return -1
    # Plan
        # Build empty graph
        # add nodes/vertices/edges
        # loop through queue
        # return eka 

def earliest_ancestor(ancestors, starting_node):
    # create empty graph
    graph = Graph()
    # add vertexes
    for x in ancestors:
        graph.add_vertex(x[0])
        graph.add_vertex(x[1])
        # connect edges
    for x in ancestors:
        graph.add_edge(x[1], x[0])
    q = Queue()
    q.enqueue([starting_node])
    # length of a path
    pathLength = 1
    # has no ancestors 
    eka = -1
    # loop through the queue
    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]
        # If the length between the 2 nodes is greater than 1
        if (len(path) >= pathLength and vertex < eka) or (len(path) > pathLength):
            eka = vertex
            pathLength = len(path)
        
            # if eka == 2:
            #     return min(eka)
        # else:
        #     if :
        #         pathLength = len(path)
        #         eka = vertex

        for next_vert in graph.vertices[vertex]:
            newPath = list(path)
            newPath.append(next_vert)
            q.enqueue(newPath) 
    return eka
    