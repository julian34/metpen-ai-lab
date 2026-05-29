# metpen-ai-lab

Lab reproducible berbasis VS Code + Python + Jupyter untuk belajar metode riset dengan bantuan AI yang bertanggung jawab.

## Mulai dari sini

Gunakan alur Dev Container.

1. Instal Docker.
2. Instal VS Code.
3. Instal ekstensi Dev Containers.
4. Buka folder ini di VS Code.
5. Jalankan `Dev Containers: Reopen in Container`.
6. Tunggu container build selesai.
7. Buka `notebooks/00_orientation.ipynb` dan mulai dari sana.

**Penting**: Jalankan notebook **berurutan dari 00 sampai 06**. Setiap notebook membangun di atas yang sebelumnya.

## Yang akan dipelajari mahasiswa

- Memuat dan memeriksa dataset (NB 01)
- Mengidentifikasi dan membersihkan masalah data (NB 02)
- Membuat visualisasi untuk eksplorasi (NB 03)
- Menghitung statistik deskriptif (NB 04)
- Mengeksplorasi korelasi dan regresi sederhana (NB 05)
- Menyusun analisis studi kasus yang lengkap (NB 06)
- Menulis interpretasi secara hati-hati
- Menggunakan AI secara bertanggung jawab dan transparan

## Panduan folder

- `notebooks/`: Tujuh notebook pembelajaran terpandu (NB 00-06)
- `data/synthetic/`: Dataset sintetis untuk latihan
- `data/processed/`: Output bersih hasil notebook 02
- `data/raw/`: Untuk dataset nyata di masa depan (kosong untuk sekarang)
- `docs/`: Catatan setup, kebijakan AI, dan troubleshooting
- `prompts/`: Prompt reusable untuk AI asisten
- `templates/`: Template pembelajaran untuk interpretasi, pemilihan metode, dan logging AI
- `scripts/`: Script generator dataset sintetis
- `tests/`: Pengecekan proyek dasar

## Urutan Workflow

```
00. orientation.ipynb ─→ Mengenal repo dan data
    ↓
01. data_loading.ipynb ─→ Load & inspect raw data
    ↓
02. data_quality_cleaning.ipynb ─→ Cleaning & output processed data
    ↓
03. exploratory_analysis.ipynb ─→ Visualize patterns
    ↓
04. descriptive_statistics.ipynb ─→ Quantify patterns
    ↓
05. correlation_regression.ipynb ─→ Model & association
    ↓
06. case_study_template.ipynb ─→ Apply learning: full analysis cycle
```

**Note**: Notebook 03-06 memerlukan output dari NB 02. Jangan lewati!

## Catatan penting tentang data

### Data Sintetis
Versi pertama menggunakan data sintetis untuk latihan. 

- **Sintetis, bukan real**: Data dibuat simulasi untuk workflow practice, bukan bukti empiris
- **Deterministic**: Random seed=42, jadi data sama setiap kali di-generate
- **Desain realistis**: Hubungan variabel dirancang untuk pembelajaran (misalnya kehadiran → nilai)

**Gunakan untuk**: Belajar teknik analisis dan workflow  
**Jangan gunakan untuk**: Klaim tentang perilaku mahasiswa nyata

**Regenerasi data**: Jika hilang, jalankan:
```bash
python scripts/generate_synthetic_student_data.py
```

Lihat [`data/synthetic/README.md`](data/synthetic/README.md) untuk detail lengkap.

## Catatan Dev Container

Dependensi diinstal saat build image Docker melalui `.devcontainer/Dockerfile`. Proyek ini sengaja **tidak menggunakan `postCreateCommand`** untuk instalasi dependensi karena semuanya ada di image.

Jika `requirements.txt` berubah:
```
Dev Containers: Rebuild Container
```

## Kebijakan AI

Notebook ini dirancang untuk pembelajaran metodologi riset dengan bantuan AI yang bertanggung jawab dan transparan.

**Penting**:
- Gunakan AI untuk menjelaskan, bukan untuk menggantikan pemahaman
- Verifikasi semua output AI sebelum digunakan
- Log penggunaan AI yang substansial di template yang disediakan
- Jangan presentasikan data sintetis sebagai bukti nyata

Lihat [`docs/02-ai-usage-policy.md`](docs/02-ai-usage-policy.md) untuk panduan lengkap.

## Bantuan & Troubleshooting

- **Setup issues**: Lihat [`docs/01-how-to-open-in-devcontainer.md`](docs/01-how-to-open-in-devcontainer.md)
- **Notebook errors**: Lihat [`docs/03-faq-troubleshooting.md`](docs/03-faq-troubleshooting.md)
- **Konvensi repo**: Lihat [`AGENTS.md`](AGENTS.md)

## Developer Notes

- Run tests: `pytest tests/`
- Generated data is deterministic (seed 42)
- All notebooks use Indonesian for student-facing content
- Synthetic data includes intentional quality issues for cleaning practice

---

**Status**: Versi pertama dengan 7 notebook inti dan data sintetis lengkap.
