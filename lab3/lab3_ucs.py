graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("D", 2)],
    "C": [("E", 2), ("G", 5)],
    "D": [("C", 1), ("E", 4)],
    "E": [("G", 2)],
    "G": []
}

visited = set()
queue = []

def ucs(node):
    queue.append((0, node))

    while queue:
        print(queue, visited)

        queue.sort()
        cost, temp = queue.pop(0)

        if temp in visited:
            continue

        visited.add(temp)

        if temp == "G":
            print("Goal reached with cost:", cost)
            break

        for child, edge_cost in graph[temp]:
            if child not in visited:
                queue.append((cost + edge_cost, child))

ucs("A")
print(queue, visited)
