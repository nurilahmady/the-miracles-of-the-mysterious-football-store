<details> <summary><b>Tugas 2 PBP — Jawaban</b></summary> <br/>
Jawaban 1
Ceklis 1

Saya membuat sebuah proyek Django baru dimulai dengan menyiapkan direktori dan repositori. Dilanjut dengan membuat environment dengan menginstall beberapa dependencies tertentu seperti django dll. Kemudian memulai proyek Django dengan perintah django-admin startproject yang membuat proyek awal secara sederhana yang dilanjutkan dengan konfigurasi awal environment variables dan proyek.

Ceklis 2

Saya membuat aplikasi main menggunakan perintah manage.py startapp. Kemudian mendaftarkan main ke dalam proyek utama.

Ceklis 3

Mengonfigurasi routing URL proyek dengan meng-include main.urls pada urlpatterns, tapi pastikan dulu urls sudah dibuat pada main.

Ceklis 4

Mengonfigurasi file models pada main dengan membuat atribut serta tipenya sesuai dengan ketentuan pada soal.

Ceklis 5

Mengonfigurasi file views agar merender file main.html pada template berisi struktur HTML sesuai yang diminta soal.

Ceklis 6

Menambahkan path show_main pada urlpatterns.

Ceklis 7

Create new project di PWS dan mengizinkan proyek di-hosting oleh PWS, kemudian push code ke PWS.

Ceklis 8

Menulis README di GitHub.

Mostly code yang saya bikin (untuk saat ini) mengikuti contoh dari yang diberikan pada tutorial.

Jawaban 2
<img width="1297" height="770" alt="Screenshot 2025-09-09 191023" src="https://github.com/user-attachments/assets/0df7733c-e89a-435a-8232-13c58fdee343" /> Sumber: PPT 2 PBP

request masuk berupa URL

urls.py: peta rute URL yang menunjukkan view mana yang dieksekusi.

views.py: logika aplikasi. Bisa ambil/ubah data via model, lalu render template atau return JSON/redirect.

models.py: definisi data dan logika domain.

Template HTML: bagian yang ditampilkan sebagai respons. Hanya membaca context dari view untuk ditampilkan.

Jawaban 3

settings.py adalah pusat konfigurasi proyek. Contoh yang diatur:

Identitas & Keamanan

Aplikasi & Middleware

Database & ORM

dan lain-lain

Jawaban 4

Alur migrasi:

Definisikan/ubah model di models.py.

Buat berkas migrasi (instruksi perubahan skema).

Eksekusi (terapkan) migrasi ke DB.

Tracking: tabel django_migrations menyimpan migrasi yang sudah diterapkan.

Jawaban 5

Walau banyak framework bagus, Django dipilih karena ramah pemula (Pythonic), cepat untuk belajar from zero to production-like app, sekaligus menanamkan best practices (keamanan, struktur, migrasi). ROI pembelajaran satu semester jadi tinggi dan jadi fondasi saat pindah ke framework lain.

Jawaban 6

Untuk sementara belum ada kritik. Sudah cukup bagus. Terima kasih.

</details>
<details> <summary><b>Tugas 3 PBP — Jawaban</b></summary> <br/>

Jawaban Tugas 3
1) Mengapa kita memerlukan data delivery pada platform?

Agar data bisa dikonsumsi lintas klien (web, mobile, layanan pihak ketiga) secara terstandar dan terpisah dari tampilan. Dengan data delivery, backend menyediakan representasi data (XML/JSON) yang stabil, sementara front-end/consumer bebas berkembang. Dampaknya:
- Integrasi mudah (API-first).
- Reuse dan otomasi (script/ETL).
- Skalabilitas tim (UI/Backend bisa paralel).

2) XML vs JSON — kenapa JSON lebih populer?

- JSON lebih ringkas (kurang verbosity), ukuran payload lebih kecil.
- Mapping natural ke tipe data JS/Python (objek, array, number, boolean).
- Parsing cepat & dukungan luas di ekosistem web modern.
- XML unggul untuk skenario yang butuh schema/namespace/atribut kompleks, namun untuk API aplikasi umum, JSON biasanya lebih praktis → hence lebih populer.

3) Fungsi is_valid() pada Django Form, dan kenapa dibutuhkan?

is_valid() melakukan validasi: type checking, required fields, validasi kustom (clean_*), serta menghasilkan cleaned_data jika lolos. Tanpanya, kita rawan menyimpan data yang tidak sesuai skema/bisnis rule, berujung error, inkonsistensi, atau celah keamanan (mis. input berbahaya).

4) Mengapa perlu {% csrf_token %} saat membuat form? Apa risikonya jika tidak ada?

CSRF token mencegah serangan Cross-Site Request Forgery: penyerang memaksa browser korban mengirim request POST ke situs kita tanpa sepengetahuan korban. Tanpa token, attacker bisa menyisipkan form/skrip di situs lain yang mengeksekusi aksi (mis. tambah/hapus data) memakai cookie sesi korban. Dengan token, request berbahaya gagal karena tidak memiliki token yang valid.

5) Step-by-step implementasi 

Skema data: pastikan model sudah siap untuk ditampilkan/ditambah & lakukan migrasi.

Serialisasi: uji serializers.serialize('xml', queryset) dan 'json' di shell Django untuk memastikan payload valid.

View data delivery: tulis 4 view; uji manual di browser/Postman (/xml/, /json/, /xml/1/, /json/1/).

Routing: tambahkan path, verifikasi reverse() mengembalikan URL yang benar.

Daftar & Detail: buat main.html (loop daftar objek, tombol Add & Detail), dan detail.html.

Form tambah: buat ModelForm, tambahkan {% csrf_token %}, handle POST dengan is_valid() → save() → redirect ke list/detail.

Uji alur end-to-end: tambah item via form → muncul di list → cek halaman detail → cek endpoint JSON/XML untuk item baru.

Deployment: commit, push, dan verifikasi endpoint di lingkungan PWS.

6) Feedback untuk asdos 

Materi jelas dan runut, mantap.

7) gambar pengambilan data pada postman
1. show all of data products as xml
<img width="1918" height="1150" alt="Screenshot 2025-09-16 202538" src="https://github.com/user-attachments/assets/b77de30c-5a0d-4014-bc54-30c72a422722" />


2. show all of data products as json
<img width="1919" height="1199" alt="Screenshot 2025-09-16 202604" src="https://github.com/user-attachments/assets/45d7b583-9691-453c-b19f-0fd3cbd42fa0" />

3. show a data product as xml
<img width="1919" height="1199" alt="Screenshot 2025-09-16 202732" src="https://github.com/user-attachments/assets/12b37a28-c1d7-494f-bb49-f13bcc3967c9" />

4. show a data product as json
<img width="1919" height="1199" alt="Screenshot 2025-09-16 202746" src="https://github.com/user-attachments/assets/b1ab325f-3863-4591-8c94-d7e3059fab72" />


</details>