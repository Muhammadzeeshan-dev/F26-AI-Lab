import heapq

# Weighted graph
graph = {
    'A': [('B', 1), ('C', 10)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 2), ('G', 2)], # C to G corridor
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

# Uniform Cost Search (UCS)
def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node == goal: return path, cost
        if node in visited: continue
        
        visited.add(node)
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                
    return None, 0

path, cost = ucs('A', 'G')
print("UCS Path:", path)
print("Total Cost:", cost)