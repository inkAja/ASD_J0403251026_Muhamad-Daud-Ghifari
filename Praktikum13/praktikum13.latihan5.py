# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 13 - Minimum Spanning Tree
# ====================================================================
# latihan 5 : Studi kasus 2 Jaringan Komputer
# ====================================================================
import heapq
# 1. Representasi Weighted Graph menggunakan Adjacency List (Dictionary)
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}
def prim(graph, start):
    # mencatat router yang sudah dimasukan
    visited = set([start])
    # menyimpan daftar edge
    edges = []
    # 
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    
    # Pindahkan blok while ke luar dari loop for di atas
    while edges:
        # Ambil edge dengan bobot paling kecil
        weight, u, v = heapq.heappop(edges)
        # memilih edge yang belum dikunjungi/dimasukan  
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            # memasukan semua edge yang terhubung ke dalam heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'RouterA')
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total)


# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
"""
Kasus 2 . Jaringan Komputer
RouterA - RouterB = 3
RouterA - RouterC = 2
RouterB - RouterD = 5
RouterC - RouterD = 1
RouterB - RouterC = 4

"""
# 2. Algoritma apa yang digunakan?
"""
Algoritma Prim
"""
# 3. Edge mana saja yang dipilih dalam MST?
"""
('RouterA', 'RouterC', 2)
('RouterC', 'RouterD', 1)
('RouterA', 'RouterB', 3)
"""
# 4. Berapa total bobot MST?
"""
6 bobot
"""
# 5. Mengapa edge tertentu tidak dipilih?
"""
Karena kedua router dalam edge tersebut sudah dicatat dalam variabel visited
"""