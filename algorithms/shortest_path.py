from collections import defaultdict
from data_structures.graph import Graph
from data_structures.priority_queue import PriorityQueue
import heapq

def dijkstra(G: Graph, src):
    dist_to = defaultdict(lambda: float("inf"))
    edge_to = defaultdict(lambda: None)
    priority_queue = PriorityQueue()
    for u in range(len(G)):
        priority_queue.push(u, float("inf"))
    
    seen = set()
    dist_to[src] = 0
    while (priority_queue):
        _, u = priority_queue.pop()
        seen.add(u)

        for v, w in G.neighbors(u):
            # Relaxation
            if (dist_to[v] > dist_to[u] + w):
                dist_to[v] = dist_to[u] + w 
                edge_to[v] = u 
                priority_queue.replace(v, dist_to[u] + w)
    
    return dist_to, edge_to, seen


def dijkstra_with_heapq(G: Graph, src):
    dist_to = defaultdict(lambda: float("inf"))
    edge_to = defaultdict(lambda: None)

    priority_queue = [(float("inf"), u) for u in range(len(G))]
    heapq.heapify(priority_queue)

    seen = set()
    dist_to[src] = 0
    while (priority_queue):
        _, u = heapq.heappop(priority_queue)
        if (u in seen):
            continue
        seen.add(u)

        for v, w in G.neighbors(u):
            if (dist_to[v] > dist_to[u] + w):
                dist_to[v] = dist_to[u] + w
                edge_to[v] = u 
                heapq.heappush(priority_queue, (dist_to[u] + w, v))

    return dist_to, edge_to, seen
