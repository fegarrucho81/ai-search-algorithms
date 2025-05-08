# Exercício 3 - A*

from heapq import heappush, heappop

# Mapeamento dos nós
node_map = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'K': 9, 'L': 10
}
reverse_map = {v: k for k, v in node_map.items()}

# Heurística: estimativas de custo até 'I'
heuristic = [67, 80, 45, 18, 60, 45, 28, 15, 0, 58, 34]

def a_star_search(edges, src, target, n):
    adj = [[] for _ in range(n)]
    for u, v, cost in edges:
        adj[u].append((v, cost))

    visited = [False] * n
    g_score = [float('inf')] * n
    g_score[src] = 0

    pq = []
    heappush(pq, (heuristic[src], src))
    parent = [-1] * n

    while pq:
        f, current = heappop(pq)

        if current == target:
            break

        if visited[current]:
            continue
        visited[current] = True

        for neighbor, cost in adj[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heappush(pq, (f_score, neighbor))
                parent[neighbor] = current

    # Reconstrução do caminho
    path = []
    node = target
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

if __name__ == "__main__":
    edges = [
        [0, 1, 12], [1, 0, 12],
        [0, 2, 45], [2, 0, 45],
        [0, 3, 61], [3, 0, 61],
        [1, 4, 38], [4, 1, 38],
        [1, 2, 15], [2, 1, 15],
        [2, 5, 20], [5, 2, 20],
        [2, 6, 50], [6, 2, 50],
        [3, 6, 43], [6, 3, 43],
        [4, 5, 5],  [5, 4, 5],
        [5, 7, 28], [7, 5, 28],
        [6, 7, 13], [7, 6, 13],
        [7, 8, 30], [8, 7, 30],
        [4, 9, 21], [9, 4, 21],
        [9,10, 27], [10,9, 27],
        [10,8, 34], [8,10, 34]
    ]

    source = node_map['A']
    target = node_map['I']
    n = len(node_map)

    path = a_star_search(edges, source, target, n)

    print("Caminho por A* (A estrela):")
    for i in range(len(path)):
        print(reverse_map[path[i]], end=" → " if i < len(path) - 1 else "\n")
