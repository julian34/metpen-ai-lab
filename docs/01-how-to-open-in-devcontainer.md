# Cara Membuka Proyek di Dev Container

Ikuti langkah berikut agar lingkungan belajar konsisten untuk semua pengguna.

1. Pastikan Docker sudah terpasang dan berjalan.
2. Buka folder proyek ini di VS Code.
3. Buka Command Palette dengan `Cmd+Shift+P`.
4. Jalankan perintah `Dev Containers: Reopen in Container`.
5. Tunggu proses build image selesai.
6. Setelah masuk container, buka notebook `notebooks/00_orientation.ipynb`.

Catatan:

- Dependensi Python dipasang saat build image melalui `.devcontainer/Dockerfile`.
- Jika `requirements.txt` berubah, rebuild container image.
