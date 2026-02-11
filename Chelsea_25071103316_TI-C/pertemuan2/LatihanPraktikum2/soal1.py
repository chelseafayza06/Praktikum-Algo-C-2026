# Menghitung Nilai Rata-Rata

def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong" # Ini utk menampilkan data kosong jika data tsb kosong
    else:
        return sum(nilai) / len(nilai) #operasi menghitung rata2 

# Panggil fungsi
data = [80, 75, 90, 60, 85]
hasil = rata_rata(data)

print("Rata-rata =", hasil)


