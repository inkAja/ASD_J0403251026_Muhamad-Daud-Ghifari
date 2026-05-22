# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 12 -  Graph II: Shortest Path
# ====================================================================
# Latihan 3: Implementasi Bellman-Ford
# ====================================================================

# Weighted graph dengan bobot negatif
graph = {
    'A' : {'B' : 5, 'C':4},
    'B' : {},
    'C' : {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-ford
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellan-Ford melakukan relaksasi sebanyak jumlah node
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neghbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neghbor]:
                    distances[neghbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A') 
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


    # Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B? 
""" 5 bobot"""
# 2. Berapa total bobot jalur A -> C -> B? 
""" 2 bobot """
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
"""Jalur A -> C -> B"""
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
""" Karena Algoritma ini bersifat relaksasi yaitu mengecek semua kemungkinan lalu memilih yang terbaik. Artinya algoritma ini dapat mengupdate jarak dari suatu node ke node lain jika bobotnya lebih kecil melalui rute lain"""
# 5. Apa yang dimaksud dengan proses relaksasi edge?
"""Relaksasi edge adalah proses pengecekan setiap  edge untuk memperoleh jarak minimum/maksimum yang benar"""
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
"""Perbedaan utamanya ada pada pemilihan edge Bellman-Ford akan melakukan pengecekan setiap edge sedangkan Dijkstra akan langsung memilih bobot terkecil berdasarkan node saat ini"""