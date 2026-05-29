# FAQ dan Troubleshooting

## Kernel Jupyter tidak muncul

- Pastikan proyek dibuka di Dev Container.
- Pilih kernel `Python (metpen-ai-lab)` di notebook.
- Jika belum ada, rebuild container image dengan `Dev Containers: Rebuild Container`.

## File data sintetis hilang atau corrupted

**Gejala**: Notebook 01 gagal dengan error "File not found" atau data terlihat aneh.

**Solusi**:
1. Jalankan script generator:
   ```bash
   python scripts/generate_synthetic_student_data.py
   ```
2. Atau dari notebook:
   ```python
   from scripts.generate_synthetic_student_data import main
   main()
   ```
3. Verifikasi file baru di `data/synthetic/synthetic_student_performance.csv` (harus ~227KB, 2024 baris)

**Lihat**: [`data/synthetic/README.md`](../data/synthetic/README.md) untuk detail lengkap tentang regenerasi data.

## File data bersih hilang

**Gejala**: Notebook 03-06 gagal dengan error "File not found" untuk `data/processed/student_performance_cleaned.csv`.

**Solusi**:
1. Jalankan notebook 02 (`02_data_quality_cleaning.ipynb`) terlebih dahulu
2. Notebook 02 akan membersihkan data sintetis dan menyimpan hasil ke `data/processed/`
3. Pastikan Anda jalankan hingga sel terakhir di notebook 02

## Gagal membaca file CSV di notebook

- Pastikan Anda sudah menjalankan sel awal notebook yang load data
- Periksa error message untuk lokasi file yang diharapkan
- Jika notebook memberikan error tentang file tidak ada di beberapa lokasi, coba jalankan dari root folder proyek atau dalam Dev Container

## Hasil notebook berbeda antar pengguna

- Pastikan semua pengguna memakai Dev Container yang sama (rebuild jika perlu)
- Pastikan Anda menjalankan notebook dari atas ke bawah tanpa melewati sel
- Dataset sintetis menggunakan random seed deterministic (seed=42), jadi hasil harus sama

## `pytest` gagal

- Periksa apakah struktur folder wajib sudah lengkap:
  ```
  data/raw/            ✓
  data/synthetic/      ✓
  data/processed/      ✓
  notebooks/           ✓
  prompts/             ✓
  templates/           ✓
  scripts/             ✓
  tests/               ✓
  ```
- Pastikan semua notebook dan file template sudah dibuat
- Jalankan dari root folder: `pytest tests/`

## Notebook error "Data bersih tidak ditemukan"

- Ini adalah error yang diharapkan jika Anda menjalankan notebook 03-06 sebelum notebook 02
- **Solusi**: Jalankan notebook 02 (`02_data_quality_cleaning.ipynb`) terlebih dahulu
- Notebook 02 akan membuat file `data/processed/student_performance_cleaned.csv`
- Setelah itu, notebook 03-06 akan menemukan file dan berjalan dengan normal

## Ada masalah lain?

- Lihat [`docs/02-ai-usage-policy.md`](02-ai-usage-policy.md) untuk pertanyaan tentang penggunaan AI
- Lihat [`AGENTS.md`](/AGENTS.md) untuk konvensi repo dan alur workflow
- Tanyakan instruktur atau buat issue di repository jika ada bug yang tidak terdaftar
