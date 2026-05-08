# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Tugas Praktikum 1 - Membuat Adjacency Matrix Dari graph berikut
# 0 -- 1
# |  / 
# | /
# 2 -- 3    
# ====================================================================

def createGraph(V, edges):
    # Membuat matriks V x V dengan nilai awal 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Mengisi matriks dengan nilai 1 untuk setiap edge
    for it in edges:
        u = it[0]
        v = it[1]

        mat[u][v] = 1
        mat[v][u] = 1  # Karena graph tidak berarah

    return mat

# Jalankan program 

if __name__ == "__main__":
    # karena 0,1,2,3 jadi ada 4 vertex
    V = 4

    # mengisi hubungan antar vertex 
    edges = [[0,1],[0,2],[1,2],[2,3]]

    mat = createGraph(V, edges)
    print("Representasi antar vertex:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

