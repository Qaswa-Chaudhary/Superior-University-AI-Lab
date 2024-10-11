# Breath First Search

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def bfs(visited, nodes):
    if not nodes:  
        return
    
    # FIFO
    n = nodes.pop(0)  
    
    if n not in visited:
        print(n, end=' ')
        visited.append(n)  
        
        
        for neighbour in tree[n]:
            if neighbour not in visited:
                nodes.append(neighbour)
    
    bfs(visited, nodes)  

# Start BFS from node 'A'
bfs(visited, ["A"])  
print()
print("Visited Nodes:", visited)


            
#%%
# Breath First Search with Queue
tree = {
       'A' : ['B','C'] ,
       'B' : ['D','E'] ,
       'C' : ['F','G'] ,
       'D' : [] ,
       'E' : [] ,
       'F' : [] ,
       'G' : []
        }

visited = []
queue   = []


def bfs(visited,queue,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=' ')
        for neighbour in tree[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            




bfs(visited, queue, "A")
print()
print("Visited Nodes:", visited)
# print(tree)

#%% Breath First Search with Queue and Nodes

class Node:
    def __init__(self, value):
        self.value     = value
        self.neighbour = []
        
    def add_neighbour(self , node):
        self.neighbour.append(node)
        
       
class BFS:        
    def bfs(self, start_node , goal):
        self.queue  = [start_node]
        self.visited = set()
        
            
        while self.queue:
            self.current_node = self.queue.pop(0)
            
            
            # checking if the current node is goal node
            if self.current_node.value == goal:
                print(f"Goal {goal} is found.")
                return True
            
            # adding the node into visited 
            if self.current_node not in self.visited:
                print(f"Visited Node:{self.current_node.value}")
                self.visited.add(self.current_node)
                
                # adding neighbour into stack
                for neighbour in self.current_node.neighbour:
                    if neighbour not in self.visited:
                        self.queue.append(neighbour)
            

        return False        

# initialize nodes                   
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")

# adding node
        
node_A.add_neighbour(node_B)
node_A.add_neighbour(node_C)
node_B.add_neighbour(node_D)
node_B.add_neighbour(node_E)
node_C.add_neighbour(node_F)
node_C.add_neighbour(node_G)


# calling the function

depth = BFS()
depth.bfs(node_A, "E")