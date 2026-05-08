# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Tugas Praktikum 4 - Studi kasus Dunia nyata
# Studi kasus Peta Kota
# Node(Vertex) = kota -> (Bekasi, Depok, Karawang, Subang, Purwakarta, Cirebon)
# Edge = Jalan penghubung
# ====================================================================


def adjacency_matrix(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]

        mat[u][v] = 1
        mat[v][u] = 1  # graph nya tidak berarah, rutenya dua arah
    return mat


def adjacency_list(V, edges):
    # buat dictionary
    adj = {}
    for it in edges:
        u = it[0]
        v = it[1]

        # inisialisasi vertex u jika belum ada di dictionary
        if u not in adj:
            adj[u] = []
        # menambahkan vertex v ke dalam list adjacency vertex u, begitu juga yang v ke u
        adj[u].append(v)

        if v not in adj:
            adj[v] = []
        adj[v].append(u)
    return adj


if __name__ == "__main__":
    # karena ada 6 kota, maka vertex nya 6
    V = 6
    # (Bekasi, Depok,  Karawang, Subang, Purwakarta, Cirebon)
    # mengisi hubungan antar kota
    edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]]

    mat = adjacency_matrix(V, edges)
    print("Representasi Rute jalan antar kota dalam bentuk Matriks:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

    # Adjacency List
    # Membuat hubungan antar kota yang sesuai dengan gambar
    print("====================================================\n")
    print("Representasi Rute jalan antar kota dalam bentuk List")
    edgesAdj = [
        ["Bekasi", "Depok"],
        ["Bekasi", "Karawang"],
        ["Depok", "Karawang"],
        ["Karawang", "Subang"],
        ["Karawang", "Purwakarta"],
        ["Subang", "Purwakarta"],
        ["Subang", "Cirebon"],
        ["Purwakarta", "Cirebon"],
    ]
    adj = adjacency_list(V, edgesAdj)

    for i in adj:
        print(f"{i} : {adj[i]}")
