# metpen-ai-lab

Lab reproducible berbasis VS Code + Python + Jupyter untuk belajar metode riset dengan bantuan AI yang bertanggung jawab.

## Mulai dari sini

Gunakan alur Dev Container.

1. Instal Docker.
2. Instal VS Code.
3. Instal ekstensi Dev Containers.
4. Buka folder ini di VS Code.
5. Jalankan `Dev Containers: Reopen in Container`.
6. Buka `notebooks/00_orientation.ipynb`.

## Yang akan dipelajari mahasiswa

- Memuat dan memeriksa dataset.
- Mengidentifikasi isu kualitas data dasar.
- Membersihkan data dan menyimpan hasil olahan.
- Membuat visualisasi sederhana.
- Menghitung statistik deskriptif.
- Mengeksplorasi korelasi dan regresi sederhana.
- Menyusun analisis studi kasus kecil.
- Menulis interpretasi secara hati-hati.
- Menggunakan AI secara bertanggung jawab dan transparan.

## Panduan folder

- `notebooks/`: notebook pembelajaran terpandu.
- `data/synthetic/`: dataset sintetis untuk latihan.
- `data/processed/`: output bersih hasil notebook.
- `docs/`: catatan setup dan kebijakan AI.
- `prompts/`: prompt AI yang dapat digunakan ulang.
- `templates/`: template pembelajaran yang dapat digunakan ulang.
- `scripts/`: skrip generator dataset.
- `tests/`: pengecekan proyek dasar.

## Catatan penting tentang data

Versi pertama menggunakan data sintetis untuk latihan. Data sintetis berguna untuk mempelajari alur kerja, tetapi tidak boleh diperlakukan sebagai bukti empiris dunia nyata.

## Catatan Dev Container

Dependensi diinstal saat build image Docker melalui `.devcontainer/Dockerfile`. Proyek ini sengaja tidak menggunakan `postCreateCommand` untuk instalasi dependensi.
