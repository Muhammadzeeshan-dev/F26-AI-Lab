graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

visited = set()
queue = []

def astar(node):
    queue.append((h[node], 0, node))

    while queue:
        print(queue, visited)

        queue.sort()
        f, cost, temp = queue.pop(0)

        if temp in visited:
            continue

        visited.add(temp)

        if temp == "G":
            print("Goal reached with cost:", cost)
            break

        for child, edge_cost in graph[temp]:
            if child not in visited:
                new_cost = cost + edge_cost
                new_f = new_cost + h[child]
                queue.append((new_f, new_cost, child))

astar("S")
print(queue, visited)