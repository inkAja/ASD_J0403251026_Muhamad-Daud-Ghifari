# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 13 - Minimum Spanning Tree
# ====================================================================
# latihan 4 : Jaringan Kabel Antar Gedung
# ====================================================================
# Program Menentukan Jaringan Kabel Internet Kampus Minimum
# Menggunakan Algoritma Kruskal (Greedy Approach)

# 1. Representasi Weighted Graph menggunakan daftar Edge (Bobot, Node1, Node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]
edges.sort()

mst = []
total_weight = 0

connected = set()
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # menyimpan ke mst
        mst.append((u, v, weight))
        # menyimpan bobot
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
"""
Algoritma kruskal, karena algoritma ini selalu mencari bobot/harga minimum
"""
# 2. Edge mana saja yang dipilih?
"""
('GedungC', 'GedungD', 1)
('GedungA', 'GedungC', 2)
('GedungB', 'GedungD', 3)
"""
# 3. Berapa total biaya minimum?
"""
6 bobot
"""
# 4. Mengapa MST cocok digunakan pada kasus ini?
"""
Karena studi kasus tersebut mencari biaya minimum, maka dari itu MST cocok karena karakteristik MST yang menghubungkan titik tanpa
ada cycle sehingga biayanya lebih murah
"""