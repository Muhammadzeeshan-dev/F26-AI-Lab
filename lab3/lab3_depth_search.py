# Graph
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

# Depth-Limited Search (DLS)
def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        return "CUTOFF", path
    
    cutoff_occurred = False
    
    for neighbor in graph[node]:
        if neighbor not in path: # Path-local cycle check
            status, result_path = dls(neighbor, goal, limit - 1, path + [neighbor])
            if status == "FOUND":
                return "FOUND", result_path
            elif status == "CUTOFF":
                cutoff_occurred = True
                
    if cutoff_occurred:
        return "CUTOFF", path
    else:
        return "FAILURE", path

# Iterative Deepening DFS (IDDFS)
def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        print("Checking limit:", limit)
        status, path = dls(start, goal, limit, [start])
        if status == "FOUND":
            print("Goal Found!")
            return path
        else:
            print("Result at limit", limit, "is", status)
    return "Not Found"

print("Running IDDFS ")
print("Final Path:", iddfs("A", "G", 4))