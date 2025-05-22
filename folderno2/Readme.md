Interface Command
•	• execute() == jalankan()): Menjalankan perintah menambah, menghapus, atau menandai tugas.
•	• undo() == batal()): Membatalkan dari perintah sebelumnya.
Implementasi Perintah
a. AddTaskCommand (TambahTugasPerintah)
• execute(): Menjalankan method tambah_tugas() dari objek DaftarTugas.
• undo(): Menghapus tugas dengan method hapus_tugas().
b. RemoveTaskCommand (HapusTugasPerintah)
• execute(): menjalankan method hapus_tugas().
• undo(): mengembalikan command  yang dihapus menggunakan tambah_tugas().
c. MarkAsDoneCommand (TandaiSelesaiPerintah)
• execute(): Menjalankan method tandai_selesai().
• undo(): Mengubah status menggunakan method tandai_belum_selesai().
Kelas TodoList dan CommandManager
a. DaftarTugas: Menyimpan dan menampilkan daftar tugas serta info nya apa sudah dikerjakan atau belum, dengan method seperti tambah_tugas(), hapus_tugas(), tandai_selesai(), tandai_belum_selesai(), dan tampilkan_tugas().
b. ManajerPerintah: Menjalankan dan menyimpan riwayat perintah yaitu jalankan_perintah(perintah), batal(), dan ulangi().
