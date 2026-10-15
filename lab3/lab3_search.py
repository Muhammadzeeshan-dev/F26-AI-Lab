graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": []
}

visited_bfs = []
queue = []

def bfs(node):
    queue.append(node)
    while queue:
        temp = queue.pop(0)
        if temp not in visited_bfs:
            visited_bfs.append(temp)
            for child in graph[temp]:
                queue.append(child)

bfs("A")
print("BFS:", visited_bfs)


visited_dfs = []
stack = []

def dfs(node):
    stack.append(node)
    while stack:
        temp = stack.pop()
        if temp not in visited_dfs:
            visited_dfs.append(temp)
            for child in graph[temp]:
                stack.append(child)

dfs("A")
print("DFS:", visited_dfs)
