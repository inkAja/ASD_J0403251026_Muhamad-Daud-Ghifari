# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Mempelajari Adjacency Matriks (Undirected Graph)
# ====================================================================

def createGraph(V, edges):
    # Undirected graph
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # Jika undirected graph
        mat[v][u] = 1
    return mat


if __name__ == "__main__":
    V = 3

    edges = [[0, 1], [0, 2], [1, 2]]

    mat = createGraph(V, edges)
    print("Adjacency Matrix Representation: ")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()
