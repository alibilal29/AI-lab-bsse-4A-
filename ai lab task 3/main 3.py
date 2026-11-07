import heapq
graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 3), ("E", 6)],
    "C": [("F", 2)],
    "D": [],
    "E": [("G", 1), ("F", 1)],
    "F": [("E", 1)],
    "G": []
}
def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, cost, visited
        for next_node, weight in graph[node]:
            heapq.heappush(
                queue,
                (cost + weight, next_node, path + [next_node])
            )
path, cost, order = ucs("A", "G")
print("Path:", path)
print("Cost:", cost)
print("Processing Order:", order)
