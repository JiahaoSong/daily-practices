from data_structures.priority_queue import PriorityQueue
from data_structures.graph import Graph
import heapq
import math

def generate_path(edge_to, src, tar):
    ans = []
    def gen_path_aux(cur):
        if (cur != src):
            gen_path_aux(edge_to[cur])
        ans.append(cur)

    gen_path_aux(tar)
    return ans


def my_dijkstra(graph : Graph, src):
    """
    Implements dijkstra algorithm using my own priority queue
    """
    dist_to = {}
    edge_to = {}
    pq = PriorityQueue()
    visited = set()

    pq.push(0, src)
    while (pq.size() != 0):
        dist_u, u = pq.pop()
        visited.add(u)
        dist_to[u] = dist_u

        for v, w in graph.neighbors(u):
            if (v not in visited):
                dist_v = math.inf
                if (v in dist_to):
                    dist_v = dist_to[v]

                if (dist_u + w < dist_v):
                    dist_v = dist_u + w
                    if (pq.contains(v)):
                        # Relaxation
                        pq.change_priority(dist_v, v)
                    else:
                        pq.push(dist_v, v)
                    
                    dist_to[v] = dist_v
                    edge_to[v] = u
        
    return dist_to, edge_to


def built_in_dijkstra(graph : Graph, src):
    dist_to = {}
    edge_to = {}
    pq = []
    visited = set()

    heapq.heappush(pq, (0, src))
    while (pq):
        dist_u, u = heapq.heappop(pq)
        if (u in visited):
            continue

        visited.add(u)
        dist_to[u] = dist_u

        for v, w in graph.neighbors(u):
            if (v not in visited):
                dist_v = math.inf
                if (v in dist_to):
                    dist_v = dist_to[v]

                if (dist_u + w < dist_v):
                    dist_v = dist_u + w
                    heapq.heappush(pq, (dist_v, v))
                    
                    dist_to[v] = dist_v
                    edge_to[v] = u
        
    return dist_to, edge_to