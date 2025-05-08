# Importação de módulos
import heapq  # Usado para manipular uma fila de prioridades eficiente (mín-heap).

# Definição da função dijkstra
def dijkstra(graph, start):
    # Inicializar a distância de todos os vértices para infinito
    distances = {vertex: float('infinity') for vertex in graph}  # Todas as distâncias começam como infinito.
    distances[start] = 0  # A distância do vértice inicial é definida como 0.

    # Inicializar a fila de prioridades
    priority_queue = [(0, start)]  # Fila de prioridades começa com o vértice inicial e sua distância (0).

    # Loop principal
    while priority_queue:  # Enquanto houver elementos na fila de prioridades, continua a busca.
        current_distance, current_vertex = heapq.heappop(priority_queue)  # Remove o vértice com a menor distância.

        # Ignorar se a distância for maior do que já registrada
        if current_distance > distances[current_vertex]:  # Se a distância do vértice atual for maior, ignora.
            continue

        # Iteração sobre os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():  # Percorre todos os vizinhos e seus pesos.
            distance = current_distance + weight  # Soma a distância acumulada com o peso da aresta.

            # Se encontrar um caminho menor, atualizar a distância
            if distance < distances[neighbor]:  # Se a nova distância for menor, atualiza no dicionário.
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Adiciona o vizinho à fila de prioridades.

    return distances  # Retorna o dicionário com as menores distâncias do vértice inicial para todos os outros vértices.

# Exemplo de grafo
graph = {
    'A': {'B': 1, 'C': 4},  # Vértice 'A' conectado a 'B' com peso 1 e a 'C' com peso 4.
    'B': {'A': 1, 'C': 2, 'D': 5},  # Vértice 'B' conectado a 'A', 'C' e 'D' com seus respectivos pesos.
    'C': {'A': 4, 'B': 2, 'D': 1},  # Vértice 'C' conectado a 'A', 'B' e 'D'.
    'D': {'B': 5, 'C': 1}  # Vértice 'D' conectado a 'B' e 'C'.
}

# Encontrar menor caminho a partir de 'A'
start_node = 'A'  # Vértice inicial para iniciar a busca.
distances = dijkstra(graph, start_node)  # Chama a função dijkstra para calcular os menores caminhos.

# Mostrar a lista de distâncias
print("Lista de distâncias:", distances)  # Exibe o resultado do algoritmo.

# Mostrar resultados detalhados
print(f"Menor distância de {start_node}:")  # Exibe as distâncias do vértice inicial para os demais.
for vertex, distance in distances.items():  # Itera sobre o dicionário e imprime cada distância.
    print(f"Para {vertex}: {distance}")