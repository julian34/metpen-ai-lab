# Data Synthetic

Folder ini berisi data **sintetis** untuk latihan.

## ⚠️ Penting

- Data pada folder ini dibuat secara simulasi dengan algoritma pseudo-random yang deterministik.
- Data ini **bukan** merepresentasikan individu nyata dan tidak boleh digunakan untuk klaim tentang perilaku mahasiswa nyata.
- Data sintetis berguna untuk **belajar workflow analisis**, tetapi **tidak boleh dianggap sebagai bukti empiris dunia nyata**.

## 📋 Dataset: `synthetic_student_performance.csv`

**Deskripsi:**
- 2000+ baris data mahasiswa (sintetis)
- ~19 kolom termasuk performance, engagement, dan faktor kontekstual
- Desain: Hubungan antar variabel dibuat realistis untuk pembelajaran (e.g., kehadiran → nilai)
- Deterministic: Random seed=42, jadi data akan sama setiap kali di-generate

**Kolom utama:**
- `student_id`: ID unik (S100000, S100001, ...)
- `cohort_year`, `program`, `semester`: Konteks latar belakang
- `attendance_rate`, `study_hours_per_week`, `lms_logins`: Engagement
- `assignment_score`, `quiz_average`, `midterm_score`, `final_exam_score`: Performance
- `final_grade`, `passed`: Outcome
- `internet_access`, `part_time_work_hours`, `commute_minutes`: Faktor eksternal
- `missing_reason_flag`: Flag untuk practicing missing data handling

**Karakteristik QA:**
- Sengaja ada missing values (~6-8% per kolom tertentu) untuk latihan pembersihan
- Ada duplikat baris (~12 duplikat) untuk latihan deteksi duplikat
- Non-random missingness: Missingness berkorelasi dengan kondisi (e.g., unstable internet → missing final exam)

## 🔄 Cara Regenerasi Data

Jika file `synthetic_student_performance.csv` hilang atau ingin direset ke versi asli:

### Menggunakan script Python

```bash
cd /workspaces/metpen-ai-lab
python scripts/generate_synthetic_student_data.py
```

**Output yang diharapkan:**
```
Saved synthetic dataset to: data/synthetic/synthetic_student_performance.csv
Rows: 2024, Columns: 19
```

### Dari Python/Jupyter (interaktif)

```python
from pathlib import Path
import sys
sys.path.insert(0, '/workspaces/metpen-ai-lab')

from scripts.generate_synthetic_student_data import generate_synthetic_student_data

# Generate
df = generate_synthetic_student_data(n_rows=2000, random_seed=42)

# Simpan
output_path = Path('data/synthetic/synthetic_student_performance.csv')
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"✓ Data disimpan ke: {output_path}")
```

## 📊 Kapan Perlu Regenerasi

- **Jika file hilang** atau corrupted
- **Jika Anda mengganti random seed** di script (untuk eksperimen)
- **Jika Anda mengubah generator logic** di script dan ingin test hasil baru

**Jangan perlu regenerasi:**
- Saat menjalankan notebook 01-06 (gunakan file yang sudah ada)
- Saat melakukan data cleaning di notebook 02 (yang menghasilkan processed file)

## 🔒 Reproducibility

Karena `random_seed=42` diset di `scripts/generate_synthetic_student_data.py`, data akan **selalu sama** setiap kali di-generate. Ini memastikan:

- Mahasiswa berbeda akan melihat data yang sama
- Hasil analisis dapat di-reproduce
- Pola yang diamati konsisten di seluruh cohort

Jika Anda ingin data yang berbeda (untuk diversitas practice), ubah `random_seed` di script.

## 🎓 Catatan untuk Mahasiswa

Gunakan data ini untuk **latihan teknis**, bukan untuk kesimpulan sosial atau kebijakan. Contoh:

❌ Jangan: "Berdasarkan data ini, siswa dengan internet stabil akan selalu lulus"  
✅ Lakukan: "Dalam dataset latihan ini, ada pola positif antara akses internet dan nilai akhir. Dalam data nyata, hubungan ini mungkin lebih kompleks."

---

Jika ada pertanyaan tentang data, lihat:
- [`scripts/generate_synthetic_student_data.py`](../../scripts/generate_synthetic_student_data.py) untuk logic detail
- [`notebooks/01_data_loading.ipynb`](../../notebooks/01_data_loading.ipynb) untuk contoh loading
- [`docs/02-ai-usage-policy.md`](../../docs/02-ai-usage-policy.md) untuk kebijakan transparansi data
