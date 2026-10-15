graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": []
}

def dls(node, goal, limit):
    if node == goal:
        return True
    if limit <= 0:
        return False
    for child in graph[node]:
        if dls(child, goal, limit - 1):
            return True
    return False

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        found = dls(start, goal, depth)
        print("Depth", depth, "-->", found)
        if found:
            return True
    return False

print("DLS limit 2:", dls("A", "G", 2))
iddfs("A", "G", 3)
