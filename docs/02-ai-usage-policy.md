# Penggunaan AI yang Bertanggung Jawab

## Prinsip Umum

AI adalah alat bantu pembelajaran, bukan pengganti pemahaman atau verifikasi independen Anda. Penggunaan AI yang bertanggung jawab berarti Anda tetap aktif, kritis, dan transparan dalam setiap langkah analisis.

---

## Diizinkan: Bagaimana AI Dapat Membantu

AI dapat digunakan untuk:

- menjelaskan kode atau dokumentasi yang tidak jelas;
- membantu debug error dalam script atau notebook;
- membandingkan kemungkinan metode statistik untuk pertanyaan riset Anda;
- meningkatkan kejelasan tulisan, grammar, atau struktur penjelasan;
- membantu menyusun outline atau alur notebook;
- memberikan contoh kode yang kemudian Anda verifikasi dan adaptasi;
- menjelaskan asumsi di balik teknik statistik tertentu.

### Contoh Penggunaan yang Diizinkan
- **Penjelasan kode**: "Jelaskan apa yang dilakukan fungsi ini" → AI menjelaskan → Anda memverifikasi terhadap dokumentasi dan test case.
- **Debug**: Anda sudah mencoba debugging sendiri, kemudian bertanya ke AI → AI menyarankan pendekatan → Anda menjalankan dan verifikasi hasilnya.
- **Pemilihan metode**: "Apakah Pearson atau Spearman lebih cocok untuk data ini?" → AI membandingkan → Anda membaca [`prompts/prompt_02_choose_method.md`](../prompts/prompt_02_choose_method.md) dan memutuskan berdasarkan data Anda sendiri.

---

## Dilarang: Apa yang Tidak Boleh Dilakukan dengan AI

AI tidak boleh digunakan untuk:

- **memalsukan asal-usul data** (menyatakan data sintetis sebagai real atau sebaliknya);
- **memalsukan temuan atau hasil analisis** (mengubah hasil untuk menjawab pertanyaan yang belum dijawab data);
- **mengumpulkan analisis lengkap tanpa verifikasi mandiri** (AI melakukan 100% analisis, Anda hanya copy-paste);
- **menggantikan penalaran metodologis Anda** (AI memilih metode tanpa Anda pahami alasannya);
- **menyajikan data sintetis sebagai bukti dunia nyata** (misalnya, "berdasarkan data nyata mahasiswa Indonesia..." padahal data sintetis);
- **menyembunyikan aliran logika atau asumsi** yang Anda gunakan dalam analisis.

### Contoh Penggunaan yang Dilarang
- Meminta AI menulis interpretasi hasil tanpa Anda baca atau verifikasi terlebih dahulu.
- Menggunakan output AI langsung tanpa memahami apa yang dilakukan atau mengapa.
- Mengklaim menemukan sesuatu tanpa benar-benar melihat data atau hasil numerik.
- Meminta AI mengisi AI Usage Log *untuk Anda* (Anda harus mengisinya dengan jujur).

---

## Kewajiban Mahasiswa

Anda wajib:

1. **Memverifikasi seluruh kode sebelum dikumpulkan**
   - Jalankan kode Anda sendiri.
   - Periksa hasilnya terhadap data dan tujuan Anda.
   - Jangan asumsikan output AI benar hanya karena terlihat rapi.

2. **Menjelaskan alasan pemilihan metode**
   - Tidak cukup bilang "AI menyarankan metode ini."
   - Jelaskan: mengapa metode ini cocok untuk pertanyaan dan data Anda?
   - Gunakan [`templates/method_selection_template.md`](../templates/method_selection_template.md) untuk menyusun justifikasi.

3. **Mengungkapkan bantuan AI yang substansial**
   - Lihat definisi "substansial" di bagian berikutnya.
   - Jika Anda menerima bantuan substansial, log-kan di [`templates/ai_usage_log_template.md`](../templates/ai_usage_log_template.md).

4. **Meninjau ulang teks hasil AI secara kritis**
   - AI dapat membuat kesalahan atau generalisasi berlebihan.
   - Baca penjelasan AI → bandingkan dengan pengetahuan Anda dan literatur → edit atau tolak jika tidak akurat.
   - Jangan percaya seratus persen pada AI.

5. **Mengisi AI Usage Log jika AI berpengaruh besar pada pekerjaan**
   - Lihat poin "Kapan Mengisi AI Usage Log" di bawah.

---

## Definisi: "Bantuan AI yang Substansial"

Bantuan dianggap **substansial** jika salah satu kondisi berikut terpenuhi:

1. **Durasi interaksi**: Anda menghabiskan ≥ 10 menit dalam interaksi AI untuk satu pertanyaan/tugas (termasuk prompt, diskusi, verifikasi).

2. **Cakupan output**: AI menghasilkan ≥ 30% dari kode atau narasi dalam subbab yang Anda kumpulkan.

3. **Pengaruh keputusan**: AI mempengaruhi **metodologi utama** pilihan Anda (misalnya, AI menyarankan Anda menggunakan regresi logistik alih-alih t-test, dan Anda mengikuti saran itu).

4. **Struktur atau arah analisis**: AI membantu Anda merumuskan pertanyaan riset, membagi langkah analisis, atau mengorganisir alur notebook.

5. **Debugg masalah kompleks**: Anda memiliki bug yang tidak dapat diselesaikan dalam waktu wajar, dan AI memberikan solusi yang Anda adopsi.

### Contoh Bantuan yang Substansial
- Bertanya ke AI: "Bagaimana cara melakukan regresi logistik di Python?" → AI menulis function skeleton → Anda adaptasi untuk data Anda. **Durasi**: 15 menit → **Substansial**.
- Bertanya: "Apa perbedaan antara Pearson dan Spearman?" → AI menjelaskan → Anda membaca penjelasan (2 menit) dan memilih method. **Durasi**: 2 menit + baca jelas → **Tidak substansial** (AI hanya menjelaskan, keputusan Anda independen).
- AI menulis 50% kode pembersihan data Anda, Anda adaptasi dan verify sisanya → **Substansial** (cakupan output ≥ 30%).

---

## Kapan Mengisi AI Usage Log

**Wajib** mengisi [`templates/ai_usage_log_template.md`](../templates/ai_usage_log_template.md) jika:

- [ ] Anda menerima **bantuan AI yang substansial** (lihat definisi di atas) untuk subbab atau notebook.
- [ ] Anda tidak bisa menjelaskan sendiri mengapa Anda memilih metode X (karena AI menyarankan).
- [ ] Output AI menyumbang ≥ 30% dari pekerjaan Anda dalam subbab itu.
- [ ] Anda tidak yakin apakah bantuan "cukup substansial" → **log-kan saja** untuk transparansi.

**Opsional** mengisi (tapi rekomendasi: catat sesaat) jika:

- AI membantu dengan penjelasan singkat atau debugging kecil (durasi < 5 menit).
- Anda hanya bertanya satu atau dua kali untuk klarifikasi konsep.

### Cara Mengisi AI Usage Log

1. Buka [`templates/ai_usage_log_template.md`](../templates/ai_usage_log_template.md).
2. Salin template ke dalam notebook atau dokumen Anda.
3. Isi setiap bagian dengan jujur:
   - **Pertanyaan/tugas** yang Anda minta ke AI.
   - **Respons/bantuan** apa yang Anda terima.
   - **Verifikasi** apa yang Anda lakukan.
   - **Pengaruh** pada pekerjaan Anda.
   - **Kepuasan/catatan** tentang seberapa membantu (atau tidak).
4. Masukkan log ke dalam notebook dengan judul jelas: `## AI Usage Log — [Topik]`.

Contoh (lihat notebook `06_case_study_template.ipynb` untuk contoh lengkap):

```markdown
## AI Usage Log — Pemilihan Metode Regresi

**Pertanyaan**: "Bagaimana cara memilih antara regresi linear dan regresi logistik untuk variabel target binary?"

**Respons AI**: [penjelasan singkat tentang kondisi penggunaan setiap metode]

**Verifikasi**: Saya membaca dokumentasi statsmodels dan buku "Regression Models for Categorical Dependent Variables" oleh Long & Freese. Metode yang AI rekomendasikan sesuai dengan literatur.

**Pengaruh**: Saya memilih regresi logistik karena target saya binary (pass/fail). Tanpa AI, saya hanya tahu regresi linear.

**Kepuasan**: Sangat membantu. AI menjelaskan dengan cara yang mudah dimengerti.
```

---

## Ringkasan Checklist

Sebelum mengumpulkan pekerjaan Anda:

- [ ] Saya telah menjalankan semua kode dan memverifikasi hasilnya.
- [ ] Saya dapat menjelaskan mengapa saya memilih setiap metode.
- [ ] Saya telah meninjau penjelasan dari AI secara kritis.
- [ ] Jika saya menerima bantuan substansial, saya telah mengisi AI Usage Log.
- [ ] Data sintetis saya label dengan jelas sebagai sintetis, bukan real.
- [ ] Interpretasi saya tidak melebihi apa yang dapat ditarik dari data.

---

## Pertanyaan atau Ketidakjelasan?

Jika Anda ragu:

- Tanyakan diri sendiri: "Apakah saya bisa menjelaskan pilihan ini kepada dosen tanpa mengutip AI?"
- Jika jawabnya tidak → **log-kan bantuan AI-nya**.
- Jika Anda masih ragu, lebih baik **log-kan** untuk transparansi daripada tidak log-kan.
- Hubungi instruktur jika ada pertanyaan tentang kebijakan ini.
