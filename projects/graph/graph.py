"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # visited = None
        if not visited:
            visited = set() 
        if starting_vertex in visited:
            return
        else:
            visited.add(starting_vertex)
            print(starting_vertex) 
            for g in self.get_neighbors(starting_vertex):
                self.dft_recursive(g, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a Set to store visited vertices
        q1 = Queue()
        visited = set()
        p = [starting_vertex]
        q1.enqueue(p)
		# While the queue is not empty...
        while q1.size() > 0:
			# Dequeue the first PATH
            path = q1.dequeue()                 
			# Grab the last vertex from the PATH
            l = path[-1]
			# If that vertex has not been visited...
            if l not in visited:  
				# CHECK IF IT'S THE TARGET
                if l == destination_vertex: 
				  # IF SO, RETURN PATH
                  return path
				# Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(l):
                    newPath = path + [next_vert]
                    q1.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()                 
            l = path[-1]
            if l not in visited:
                if l == destination_vertex: 
                  return path
                for next_vert in self.get_neighbors(l):
                    newPath = path + [next_vert]
                    stack.push(newPath)
				
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            if path is None:
                path = [starting_vertex]
                visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        else:
            return
        if destination_vertex in path:
            return path
        vertex = path[-1]
        visited.add(vertex)
        for next_vert in self.get_neighbors(vertex):
            newPath = path + [next_vert]
            x = self.dfs_recursive(next_vert, destination_vertex, visited, newPath)
            if x:
                return x 
            
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
