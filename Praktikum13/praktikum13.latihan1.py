# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 13 - Minimum Spanning Tree
# ====================================================================
# latihan 1 : Memahami Konsep Spanning Tree
# ====================================================================

# edge graph 
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# spanning tree
# jumlahnya selalu jumlah node - 1
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Jumlah dge pada graph:")
for edge in edges:
 print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree:
 print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Pertanyaan Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
"""
struktur Graph memiliki cycle dan jumlah edgenya lebih banyak
sedangkan struktur Spanning Tree tidak memiliki cycle
"""
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
"""
Karena dasar dari sebuah struktur Tree tidak memiliki cycle. Jika ada cycle maka akan ada jalur ganda menuju titik yang sama 
yang tidak sesuai dengan sifat dasar tree 
"""
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
"""
karena rumus dari spanning tree adalah jumlah titik - 1
"""