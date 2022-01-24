```python
import heapq
def dijkstra(graph, num_of_nodes, start):
    visited = [False] * num_of_nodes
    distance = [float('inf')] * num_of_nodes
    prev = {}
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0,0)) #(distance, node_number)
    while len(pq) > 0:
        min_dist, node = heapq.heappop(pq)
        visited[node] = True
        if distance[node] < min_dist: # optimized way t get rid duplicate visit of same node
            continue
        for edge in graph[str(node)]: # edge: edge[0]: neightbor node, edge[1]: edge cost to neighbor
            if visited[edge[0]]:
                continue
            new_dist = distance[node] + edge[1]
            if new_dist < distance[edge[0]]:
                prev[edge[0]] = node
                distance[edge[0]] = new_dist
                heapq.heappush(pq, (new_dist, edge[0]))
        # if we provide the end node
        # if node == end:
            # return distance[end]
        # and in the outer while loop, we return float('inf')
    return distance, prev

def findShortestPath(graph, start, end, num_of_nodes):
    dist, prev = dijkstra(graph, num_of_nodes, start)
    path = []
    if dist[end] == float('inf'):
        return path
    node = end
    while node is not None:
        path.append(node)
        node = prev.get(node, None)
    return path[::-1]

if __name__ == '__main__':
    graph = {
        '0': [(1, 4), (2, 1)],
        '1': [(3, 1)],
        '2': [(1, 2), (3,5)],
        '3': [(4, 3)],
        '4': []
    }
    num_of_nodes = len(graph)
    start = 0
    end = 4
    print(findShortestPath(graph, start, end, num_of_nodes))
```

