# FAQ dan Troubleshooting

## Kernel Jupyter tidak muncul

- Pastikan proyek dibuka di Dev Container.
- Pilih kernel `Python (metpen-ai-lab)` di notebook.
- Jika belum ada, rebuild container image.

## Gagal membaca file CSV

- Pastikan file ada di `data/synthetic/synthetic_student_performance.csv`.
- Jalankan skrip generator data sintetis jika file belum ada.

## Hasil notebook berbeda antar pengguna

- Pastikan semua pengguna memakai Dev Container yang sama.
- Jalankan notebook dari atas ke bawah tanpa melewati sel.

## `pytest` gagal

- Periksa apakah struktur folder wajib sudah lengkap.
- Pastikan semua notebook dan file template sudah dibuat.
