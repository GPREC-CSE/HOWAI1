def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, m, colors, node):
    if node == len(graph):
        return True
    
    for color in range(1, m + 1):
        if is_safe(graph, colors, node, color):
            colors[node] = color
            if graph_coloring(graph, m, colors, node + 1):
                return True
            colors[node] = 0
    
    return False

def main():
    # Example graph as an adjacency list
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }
    
    num_colors = int(input("Enter the number of colors: "))
    colors = [0] * len(graph)
    
    if graph_coloring(graph, num_colors, colors, 0):
        print("Solution exists: Following are the assigned colors")
        print(colors)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()