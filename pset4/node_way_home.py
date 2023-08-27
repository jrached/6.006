from gettext import find
from re import M


def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def reverse(Adj):
    Adj_prime = [[] for _ in range(len(Adj))] #Build list of size (len(Adj)) containing empty lists at each index.
    for v in range(len(Adj)):
        vertices = Adj[v]
        for v_prime in vertices:
            Adj_prime[v_prime].append(v)
    return Adj_prime
    

def find_meeting_point(Adj):
    '''
    inputs:
        Adj - an adjacency list such as [[1,2], [2], []]
    return a meeting point or None if no meeting points exist
    '''
    Adj_reversed = reverse(Adj) #Reverse input adjacency list.
    _, order = full_dfs(Adj_reversed) 
    last_visited = order[-1] #Get last visited vertex by full dfs.
    _, path_to_parent = dfs(Adj_reversed, last_visited) #Get all vertexes that last_visited has a path to.
    for vertex in order[:-1]: #If every node in the graph is path_to_parent, then last_visited is a origin node.
        if vertex not in set(path_to_parent):
            return None
    return last_visited


# ###Testing alg
# my_adj = [[1,2],[2],[]]
# # my_adj = [[1,2],[2],[1],[]]
# r_adj = reverse(my_adj)
# print("List: ", r_adj)
# parent, order = full_dfs(r_adj)
# print("Parent: ", parent)
# meeting = find_meeting_point(my_adj)
# print("Meeting: ", meeting)

# ###Conceptual dfs test
# my_adj = [[1,2],[2],[]]
# parent, order = dfs(my_adj, 0)
# print(parent)

