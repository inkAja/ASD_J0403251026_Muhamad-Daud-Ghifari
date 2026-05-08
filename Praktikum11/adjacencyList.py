# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Mempelajari Adjacency List 
# ====================================================================

def createUndirectedGraph(V, edges):
    adj = [[] for _ in range(V)]

    # add edge to adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # Jika undirected graph
        adj[v].append(u)

    return adj
def createDirectedGraph(V, edges):
    adj = [[] for _ in range(V)]

    # add edge to adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
    return adj

if __name__ == "__main__":
    V = 3

    edges = [[0,1], [0,2], [1,2]]
    edges2 = [[1,0], [1,2], [2,0]]
    adj = createUndirectedGraph(V, edges)
    
    adj2 = createDirectedGraph(V, edges2)

    print("Adjacency List Representation(Undirected):")
    for i in range(V):
        # Print vertex 
        print(f"{i}: ", end=" ")
        for j in adj[i]:
            # print its adjacent
            print(f"{j}", end=" ")
        print()

    print("=================================================")

    print("Adjacency List Representation(Directed):")
    for i in range(V):
        # Print vertex 
        print(f"{i}: ", end=" ")
        for j in adj2[i]:
            # print its adjacent
            print(f"{j}", end=" ")
        print()