# Código adaptado de <https://www.geeksforgeeks.org/best-first-search-informed-search/>
# Código para executar o método de busca pela melhor escolha

from heapq import heappush, heappop

def GreedybestFirstSearch(edges, src, target, n):
    
    # create the adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        
    # create a visited array to 
    # keep track of visited nodes
    visited = [False] * n
    
    # create the min heap to store the nodes
    # based on the cost
    pq = []
    
    # push the source node in the min heap
    heappush(pq, [0, src])
    
    # mark the source node as visited
    visited[src] = True
    
    # to store the path   
    path = []
    
    # loop until the min heap is empty
    while pq:
        # get the top element of the min heap

        y, x = heappop(pq)#[1]
       
        # push the current node in the path
        path.append(x)
           
        # if the current node is the target node
        # break the loop
        if x == target:
            break
        
        # loop through the edges of the current node
        for edge in adj[x]:
            if not visited[edge[0]]:
                # mark the node as visited
                visited[edge[0]] = True
               
                # push the node in the min heap
                heappush(pq, [edge[1], edge[0]])
    return path

if __name__ == "__main__":
    n = 6
    edgeList = [
        [0, 1, 17], [0, 2, 9], [0, 5, 15],
        [1, 0, 20], [1, 3, 10],
		[2, 0, 20], [2, 4, 0], [2, 5, 15],
		[3, 1, 17], [3, 4, 0], [3, 5, 15],
        [4, 2,  9], [4, 3, 10],
        [5, 0, 20], [5, 2, 9], [5, 3, 10]
    ]	
    source = 0
    target = 4
    path = GreedybestFirstSearch(edgeList, source, target, n)
    for i in range(len(path)):
        print(path[i], end=" ")

