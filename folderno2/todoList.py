from abc import ABC, abstractmethod

# Antarmuka Perintah
class Perintah(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Implementasi Perintah
class TambahTugas(Perintah):
    def __init__(self, daftar_tugas, tugas):
        self.daftar_tugas = daftar_tugas
        self.tugas = tugas

    def execute(self):
        self.daftar_tugas.tambah_tugas(self.tugas)

    def undo(self):
        self.daftar_tugas.hapus_tugas(self.tugas)

class HapusTugas(Perintah):
    def __init__(self, daftar_tugas, tugas):
        self.daftar_tugas = daftar_tugas
        self.tugas = tugas

    def execute(self):
        self.daftar_tugas.hapus_tugas(self.tugas)

    def undo(self):
        self.daftar_tugas.tambah_tugas(self.tugas)

class TandaiSelesai(Perintah):
    def __init__(self, daftar_tugas, tugas):
        self.daftar_tugas = daftar_tugas
        self.tugas = tugas

    def execute(self):
        if self.tugas in self.daftar_tugas.tugas:
            self.daftar_tugas.tandai_selesai(self.tugas)
        else:
            print("Tugas tidak ditemukan.")

    def undo(self):
        if self.tugas in self.daftar_tugas.tugas:
            self.daftar_tugas.tandai_belum_selesai(self.tugas)

# Kelas DaftarTugas
class DaftarTugas:
    def __init__(self):
        self.tugas = {}

    def tambah_tugas(self, tugas):
        self.tugas[tugas] = False
        print(f"Tugas '{tugas}' ditambahkan.")

    def hapus_tugas(self, tugas):
        if tugas in self.tugas:
            del self.tugas[tugas]
            print(f"Tugas '{tugas}' dihapus.")

    def tandai_selesai(self, tugas):
        self.tugas[tugas] = True
        print(f"Tugas '{tugas}' ditandai selesai.")

    def tandai_belum_selesai(self, tugas):
        self.tugas[tugas] = False
        print(f"Tugas '{tugas}' ditandai belum selesai.")

    def tampilkan_tugas(self):
        print("Daftar Tugas:")
        for tugas, selesai in self.tugas.items():
            status = "Selesai" if selesai else "Belum Selesai"
            print(f"- {tugas}: {status}")

# Kelas ManajerPerintah
class command:
    def __init__(self):
        self.riwayat = []
        self.tumpukan_ulangi = []

    def jalankan_perintah(self, perintah):
        perintah.execute()
        self.riwayat.append(perintah)
        self.tumpukan_ulangi.clear()

    def batal(self):
        if self.riwayat:
            perintah = self.riwayat.pop()
            perintah.undo()
            self.tumpukan_ulangi.append(perintah)
        else:
            print("Tidak ada yang bisa dibatalkan.")

    def ulangi(self):
        if self.tumpukan_ulangi:
            perintah = self.tumpukan_ulangi.pop()
            perintah.execute()
            self.riwayat.append(perintah)
        else:
            print("Tidak ada yang bisa diulangi.")

# Program Utama
daftar_tugas = DaftarTugas()
manajer = command()

while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Hapus Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Batalkan Operasi")
    print("5. Ulangi Operasi")
    print("6. Tampilkan Daftar Tugas")
    print("7. Keluar")

    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        perintah = TambahTugas(daftar_tugas, tugas)
        manajer.jalankan_perintah(perintah)

    elif pilihan == "2":
        daftar_tugas.tampilkan_tugas()
        tugas = input("Masukkan nama tugas yang akan dihapus: ")
        perintah = HapusTugas(daftar_tugas, tugas)
        manajer.jalankan_perintah(perintah)

    elif pilihan == "3":
        daftar_tugas.tampilkan_tugas()
        tugas = input("Masukkan nama tugas yang akan ditandai selesai: ")
        perintah = TandaiSelesai(daftar_tugas, tugas)
        manajer.jalankan_perintah(perintah)

    elif pilihan == "4":
        manajer.batal()

    elif pilihan == "5":
        manajer.ulangi()

    elif pilihan == "6":
        daftar_tugas.tampilkan_tugas()

    elif pilihan == "7":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
