# 📋 Todo List dengan Command Pattern

Proyek ini menggunakan **Command Pattern** untuk menangani operasi-operasi pada todo list, seperti menambah, menghapus, dan menandai tugas sebagai selesai. Sistem ini juga mendukung fitur **undo** dan **redo** terhadap perintah yang dijalankan.

---

## 🧩 Interface Command

### 🔹 `execute()` → `jalankan()`
Menjalankan perintah seperti menambah, menghapus, atau menandai tugas.

### 🔹 `undo()` → `batal()`
Membatalkan aksi yang sebelumnya dijalankan.

---

## 🛠️ Implementasi Perintah

### ➕ `AddTaskCommand` (`TambahTugasPerintah`)
- `execute()`: Menjalankan method `tambah_tugas()` dari objek `DaftarTugas`.
- `undo()`: Membatalkan penambahan tugas dengan memanggil `hapus_tugas()`.

### ➖ `RemoveTaskCommand` (`HapusTugasPerintah`)
- `execute()`: Menjalankan method `hapus_tugas()` untuk menghapus tugas.
- `undo()`: Mengembalikan tugas yang dihapus menggunakan `tambah_tugas()`.

### ✅ `MarkAsDoneCommand` (`TandaiSelesaiPerintah`)
- `execute()`: Menandai tugas sebagai selesai dengan `tandai_selesai()`.
- `undo()`: Mengubah status tugas kembali menjadi belum selesai dengan `tandai_belum_selesai()`.

---

## 🧾 Kelas Utama

### 📂 `DaftarTugas`
Menyimpan dan menampilkan daftar tugas beserta statusnya:
- `tambah_tugas(tugas)`
- `hapus_tugas(tugas)`
- `tandai_selesai(tugas)`
- `tandai_belum_selesai(tugas)`
- `tampilkan_tugas()`

### 🧠 `ManajerPerintah`
Mengelola riwayat dan alur perintah:
- `jalankan_perintah(perintah)`: Menjalankan dan mencatat perintah.
- `batal()`: Membatalkan perintah terakhir (undo).
- `ulangi()`: Mengulang kembali perintah yang dibatalkan (redo).

---

## 🎮 Cara Kerja
Program ini memungkinkan pengguna untuk:
- Menambahkan tugas baru
- Menghapus tugas
- Menandai tugas sebagai selesai
- Membatalkan perintah (undo)
- Mengulang kembali perintah yang dibatalkan (redo)

Semua perintah dicatat sehingga pengguna bisa melakukan aksi `undo` dan `redo` dengan mudah.

---

## 🧪 Contoh Kasus
1. Tambah tugas "Belajar Python"
2. Tandai "Belajar Python" selesai
3. Undo → status kembali belum selesai
4. Redo → status kembali selesai

---

## 🛠 Teknologi
- Python 3
- Command Pattern

![image](https://github.com/user-attachments/assets/817a1d4d-659c-4d80-a2e0-22df3d96a48e)
