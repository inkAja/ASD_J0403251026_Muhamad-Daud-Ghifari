# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Tugas Praktikum 2 - Membuat Adjacency List Dari graph berikut
# A -- B
# |    |
# |    |
# C -- D    
# ====================================================================
def createGraph(V, edges):
    # buat dictionary 
    adj = {}

    # mengisi dictionary sesuai hubungan
    for it in edges:
        u, v = it[0], it[1]

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
    # menginisiasi 4 vertex
    V = 4

    # mengisi hubungan antar vertex
    edges = [["A","B"], ["A","C"], ["B","D"], ["C","D"]]
    
    
    adj = createGraph(V, edges)
    print("Representasi graph dalam adjacency list: ")
    for i in adj:
        print(f"{i} : {adj[i]}")
