
## main
- Operasi dasar: Penjumlahan, Pengurangan, Perkalian, Pembagian
- Penanganan error untuk pembagian dengan nol

## Run
1. Clone/Jalankan file:
```bash
python kalkulator.py


# Inisialisasi
kalkulator = Kalkulator(tambah()) 

# Operasi
print(kalkulator.hitung(5,3))  # 8 (5+3)

# Ganti strategi
kalkulator.atur_strategi(kurang())
print(kalkulator.hitung(10,4)) # 6 (10-4)

# Pembagian dengan error handling
try:
    kalkulator.atur_strategi(bagi())
    print(kalkulator.hitung(20,5))  # 4
    print(kalkulator.hitung(8,0))   # Error
except ValueError as e:
    print(e)  # "Tidak bisa membagi dengan nol."

