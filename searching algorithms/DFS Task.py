class Node:
    def __init__(self, value):
        self.value     = value
        self.neighbour = []
        
    def add_neighbour(self , node):
        self.neighbour.append(node)
        
       
class DFS:        
    def dfs(self, start_node , goal):
        self.stack   = [start_node]
        self.visited = set()
        
            
        while self.stack:
            self.current_node = self.stack.pop()
            
            
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
                        self.stack.append(neighbour)
            
            
                        
    
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

depth = DFS()
depth.dfs(node_A, "F")