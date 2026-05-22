# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 12 -  Graph II: Shortest Path
# ====================================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ====================================================================

import heapq

graph = {
    "Bogor": {"Jakarta": 5, "Depok": 2},
    "Depok": {"Jakarta": 2, "Bandung": 6},
    "Jakarta": {"Bandung": 7},
    "Bandung": {},
}


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        print(distances)
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


hasil = dijkstra(graph, "Bogor")

print("Jarak terpendek dari Bogor ke semua kota:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
"""Bogor"""
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
"""Depok"""
# 3. Node mana yang memiliki jarak paling besar dari node awal?
"""Bandung"""
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
""" 
1. menginisialisasi -> atur jarak awal 
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    semua kota menjadi infinity. lalu mengubah bogor menjadi 0
2. mengevaluasi nilai jarak dengan memeriksa neghbor/tetangga, yaitu depok dan jakarta. lalu memperbarui nilainya menjadi 2(depok) dan 5(jakarta)
3. mengevaluasi nilai tetangga depok(karena depok memiliki nilai yang lebih kecil dari jakarta). kemudian mengecek tetangga depok. Lalu memperbarui nilai Jakarta karena rute jakarta melalui depok lebih cepat dibandingkan langsung / nilainya lebih kecil. lalu memasukan nilai bandung menjadi 8 karena jarak bogor ke depok (2) + jarak depok ke bandung(6) = 8
4. mengevaluasi nilai tetangga jakarta, yaitu bandung karena jarak bogor ke jakarta(4) + jakarta ke bandung(7) = 11. maka nilai 8 yang sudah di set ke bandung tidak berubah.
Selesai
"""
