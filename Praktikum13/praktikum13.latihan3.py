# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 13 - Minimum Spanning Tree
# ====================================================================
# latihan 3 : Implementasi Algoritma Prim
# ====================================================================

import heapq
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    
    # Pindahkan blok while ke luar dari loop for di atas
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total)


# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
"""
Node a, sesuai dengan baris ke 42,
mst, total = prim(graph, 'A')
"""
# 2. Edge mana yang dipilih pertama kali?
"""
A,C karena C memiliki bobot yang lebih kecil jika dibandingkan dengan tetangga A yang lain
"""
# 3. Bagaimana Prim menentukan edge berikutnya?
"""
Mencari bobot terkecil dari seluruh pilihan edge 
"""
# 4. Berapa total bobot MST yang dihasilkan?
"""
6 bobot,
('A', 'C', 2)
('C', 'D', 1)
('D', 'B', 3)
"""
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
"""
Algoritma prim dapat mulai dari mana saja, dan memilih jalur selanjutnya berdasarkan tetangga dari edge yang sudah 
tercantum dan memiliki bobot terkecil

Algoritma Kruskal mulai dari bobot yang paling kecil, memilih jalur berdasarkan bobot paling kecil juga selama tidak membentuk cycle
"""
