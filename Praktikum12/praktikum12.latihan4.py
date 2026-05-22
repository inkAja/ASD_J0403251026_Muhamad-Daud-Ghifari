# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 12 -  Graph II: Shortest Path
# ====================================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ====================================================================
import heapq

#graph lokasi kampus
# bobot menunjukan waktu tempuh dalam menit
graph ={
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor,weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari gerbang kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, '=', jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
"""Kantin yaitu 2 menit """
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
""" 7 menit"""
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
""" Tidak, karena bisa saja melalui titik/node lain bisa lebih cepat karena total dari titik a ->b -> c, lebih cepat dari pada a -> c."""
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
""" Karena tidak ada yang bernilai negatif, dan pilihan sementara yang lebih cepat selalu benar sampai seterusnya"""