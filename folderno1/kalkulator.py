from abc import ABC, abstractmethod

# Antarmuka strategi operasi
class StrategiOperasi(ABC):
    @abstractmethod
    def eksekusi(self, a: int, b: int) -> int:
        pass

# Strategi Penjumlahan
class tambah(StrategiOperasi):
    def eksekusi(self, a: int, b: int) -> int:
        return a + b

# Strategi Pengurangan
class kurang(StrategiOperasi):
    def eksekusi(self, a: int, b: int) -> int:
        return a - b

# Strategi Perkalian
class kali(StrategiOperasi):
    def eksekusi(self, a: int, b: int) -> int:
        return a * b

# Strategi Pembagian
class bagi(StrategiOperasi):
    def eksekusi(self, a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol.")
        return a // b  # gunakan // untuk hasil bilangan bulat

# Kelas Kalkulator
class Kalkulator:
    def __init__(self, strategi: StrategiOperasi):
        self.strategi = strategi

    def atur_strategi(self, strategi: StrategiOperasi):
        self.strategi = strategi

    def hitung(self, a: int, b: int) -> int:
        return self.strategi.eksekusi(a, b)

# Fungsi utama dengan input dari pengguna
def main():
    print("=== Kalkulator Sederhana dengan Strategy Pattern ===")
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        print("Pilih operasi:")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            strategi = tambah()
        elif pilihan == "2":
            strategi = kurang()
        elif pilihan == "3":
            strategi = kali()
        elif pilihan == "4":
            strategi = bagi()
        else:
            print("Pilihan tidak valid.")
            return

        kalkulator = Kalkulator(strategi)
        hasil = kalkulator.hitung(angka1, angka2)
        print("Hasil:", hasil)

    except ValueError as e:
        print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    main()
