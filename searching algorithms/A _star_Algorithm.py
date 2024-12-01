
# A* algorithm

class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def a_star(start, goal, grid):
    open_list = []
    closed_list = []
    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        
        if current_node.position == goal_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        open_list.remove(current_node)
        closed_list.append(current_node)

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for neighbor in neighbors:
            neighbor_pos = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if 0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and grid[neighbor_pos[0]][neighbor_pos[1]] == 0:
                if any(node.position == neighbor_pos for node in closed_list):
                    continue

                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor_pos, goal_node.position)
                neighbor_node = Node(neighbor_pos, g=g_cost, h=h_cost, parent=current_node)

                if any(node.position == neighbor_pos and node.g < neighbor_node.g for node in open_list):
                    continue

                open_list.append(neighbor_node)

    return None

grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found")
