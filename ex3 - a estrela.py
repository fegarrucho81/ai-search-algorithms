# Código adaptado de <https://www.geeksforgeeks.org/best-first-search-informed-search/>
# Código para executar o método de busca A*

from heapq import heappush, heappop

def A_StarSearch(edges, src, target, n):
    
    # create the adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2], edge[3]])
        
    # create a visited array to 
    # keep track of visited nodes
    visited = [False] * n
    
    # create the min heap to store the nodes
    # based on the cost
    pq1 = []
    pq2 = []
    
    # push the source node in the min heap
    heappush(pq1, [0, src])
        
    # mark the source node as visited
    visited[src] = True
    
    # to store the path   
    path = []
    
    # loop until the min heap is empty
    while pq1:
        # get the top element of the min heap
        
        y, x = heappop(pq1)#[1]
        if len(pq2) != 0:
            z, w = heappop(pq2)#[1]
    
            # push the current node in the path
            path.append(w)
            print(w)
            
        
            # if the current node is the target node
            # break the loop
            if w == target:
                break
        
        # loop through the edges of the current node
        for edge in adj[x]:
            if not visited[edge[0]]:
                # mark the node as visited
                visited[edge[0]] = True
               
                # push the node in the min heap
                heappush(pq1, [edge[1] + y, edge[0]])
                heappush(pq2, [edge[2] + edge[1] + y, edge[0]])
        
    return path

if __name__ == "__main__":
    n = 6
    edgeList = [
        [0, 1, 13, 17], [0, 2, 15, 9], [0, 5, 10, 15],
        [1, 0, 13, 20], [1, 3, 12, 10],
		[2, 0, 15, 20], [2, 4, 17, 0], [2, 5, 7, 15],
		[3, 1, 12, 17], [3, 4, 20, 0], [3, 5, 9, 15],
        [4, 2, 17, 9], [4, 3, 20, 10],
        [5, 0, 10, 20], [5, 2, 7, 9], [5, 3, 9, 10]
    ]	
    source = 0
    target = 4
    path = A_StarSearch(edgeList, source, target, n)
    for i in range(len(path)):
        print(path[i], end=" ")

