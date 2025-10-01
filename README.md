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


<details> <summary><b>Tugas 4 PBP — Jawaban</b></summary> <br/>
  
## 1) Apa itu Django AuthenticationForm? Kelebihan & Kekurangan

AuthenticationForm adalah form bawaan Django (django.contrib.auth.forms.AuthenticationForm) untuk login dengan kredensial (biasanya username & password). Ia melakukan validasi terintegrasi dengan sistem autentikasi Django.

Kelebihan:

- Built-in & aman: validasi password, status user (aktif/nonaktif), pesan error standar.
- Terintegrasi dengan authenticate()/login() dan middleware sesi.
- Mudah dipakai: cukup instansiasi di view; bisa dipakai di template dengan {{ form.as_p }}.
- Extensible: bisa di-subclass untuk menambah field/aturan.

Kekurangan:

- Terikat skema default: login berbasis username. Untuk skema email/SSO perlu kustomisasi tambahan.
- UI minimal: styling & UX harus diurus sendiri di template.
- Tidak menyertakan fitur non-inti: mis. rate-limit, CAPTCHA, “remember me” — perlu implementasi manual atau paket pihak ketiga.

## 2) Autentikasi vs Otorisasi & Implementasi di Django

1. Autentikasi (Authentication): verifikasi siapa pengguna (login).

2. Otorisasi (Authorization): menentukan boleh apa setelah dikenali (hak akses).

Di Django:

1. Autentikasi: authenticate() memverifikasi kredensial → login(request, user) menyimpan identitas user di session → tersedia sebagai request.user (via AuthenticationMiddleware).

2. Otorisasi: sistem permissions & groups (user.has_perm('app_label.codename'), user.is_staff, user.is_superuser), decorator @login_required, @permission_required, dan mixins seperti LoginRequiredMixin. (Object-level perms perlu kustom/paket tambahan.)

## 3) Session vs Cookies (menyimpan state)

1. Session (server-side)

Kelebihan: data tidak terlihat di klien (lebih aman), kapasitas lebih besar, mudah di-invalidate dari server.

Kekurangan: butuh penyimpanan di server/DB, ada overhead manajemen & skalabilitas (sticky session/central store).

2. Cookies (client-side)

Kelebihan: sederhana, tidak perlu storage server untuk data kecil, baik untuk preferensi ringan.

Kekurangan: terlihat & dapat dimodifikasi di klien (harus diasumsikan tidak tepercaya), ukuran terbatas, rentan XSS/CSRF jika tak dikonfigurasi aman.

Praktik umum: simpan identifier (session id) di cookie; simpan state sensitif di server (session).

## 4) Keamanan cookies: aman by default? Bagaimana Django menanganinya?

Cookies tidak otomatis aman. Risiko: XSS (mencuri cookie), CSRF, session fixation, pencurian di jaringan non-HTTPS.

Django membantu lewat opsi cookie & middleware:

Flag: HttpOnly (blok akses JS), Secure (hanya via HTTPS), SameSite (mitigasi CSRF lintas-situs). Bisa set untuk session & CSRF cookie:
SESSION_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY, SESSION_COOKIE_SAMESITE, CSRF_COOKIE_SECURE, CSRF_COOKIE_HTTPONLY, CSRF_COOKIE_SAMESITE.

CSRF protection: CsrfViewMiddleware + token {% csrf_token %} pada form.

Session framework: menyimpan data di server; cookie hanya pegang session id.



## 5) Implementasi Step-by-Step 
A. Registrasi, Login, Logout

Siapkan template: halaman register, login, dan tombol/tautan logout (mis. di navbar).

Form: gunakan form bawaan Django untuk registrasi dan login (cukup instansiasi dan render di template).

View Alur:

Register: terima input, validasi, buat akun, tampilkan pesan sukses, arahkan ke login.

Login: validasi kredensial, set sesi user (logged in), set cookie last_login, arahkan ke halaman utama.

Logout: hapus sesi user (logged out), hapus cookie last_login, arahkan ke halaman login.

Proteksi halaman: terapkan pembatasan akses dengan mewajibkan login pada halaman utama/fitur tertentu.

Routing: buat rute untuk register, login, logout, dan halaman utama.

B. Buat 2 Akun & 3 Dummy Data per Akun (lokal)

Buat 2 user: lewat admin panel atau shell (pilih yang nyaman).

Isi data: untuk tiap user, buat 3 data produk menggunakan model yang sudah ada (total 6 entri).

Verifikasi: cek di admin/list view bahwa data tersimpan dan dimiliki oleh user yang tepat.

C. Hubungkan Product dengan User

Relasi: pastikan model produk memiliki relasi ke user (sebagai pemilik/creator).

Migrasi: buat & jalankan migrasi agar skema DB terbarui.

Pemanfaatan: di halaman daftar, tampilkan hanya produk milik user yang sedang login (opsional sesuai kebutuhan).

D. Tampilkan Username & Cookie last_login di Halaman Utama

Konteks tampilan: kirim informasi username user yang sedang login ke template.

Cookie last_login:

Set saat login sukses (waktu saat itu).

Hapus saat logout.

Render di halaman utama: tampilkan username dan waktu last_login jika ada.

## 6) Gambar tampilan halaman utama saat ini

<img width="399" height="937" alt="Screenshot 2025-09-17 161816" src="https://github.com/user-attachments/assets/bef32772-e971-437f-b3c8-61e7d5c2197a" />
<img width="436" height="922" alt="Screenshot 2025-09-17 161755" src="https://github.com/user-attachments/assets/5881ce9c-03d8-4f04-a2a8-8a93fcff0626" />




</details>

<details> <summary><b>Tugas 5 PBP — Jawaban</b></summary> <br/>

 # 1) Urutan Prioritas CSS Selector

Dalam CSS, aturan yang dipakai ditentukan oleh specificity dan urutan:

Inline style (langsung di atribut style) paling tinggi.

ID selector (#id) lebih kuat dibanding class, pseudo-class, maupun attribute selector.

Class selector (.class), pseudo-class (:hover), dan attribute selector ([type="text"]) berada di bawah ID.

Tag/element selector (div, p, h1) paling rendah.

Jika spesifisitas sama, aturan yang ditulis terakhir yang menang.

!important bisa memaksa aturan dipakai, tapi penggunaannya sebaiknya minimal.

# 2) Pentingnya Responsive Design

Desain responsif penting karena aplikasi web diakses dari berbagai perangkat (mobile, tablet, desktop). Dengan responsive design:

Tampilan otomatis menyesuaikan ukuran layar.

Pengguna lebih nyaman tanpa harus zoom atau geser berlebihan.

Contoh aplikasi responsif: Twitter Web (layout berubah di mobile, navbar jadi menu sederhana).
Contoh yang tidak responsif: website forum/blog lama (tampilan desktop dipaksa tampil di mobile → teks terlalu kecil, navigasi sulit).

# 3) Perbedaan Margin, Border, Padding

Margin: jarak di luar elemen (antar elemen).

Border: garis yang mengelilingi elemen.

Padding: ruang antara isi elemen dengan border.



# 4) Konsep Flexbox & Grid Layout

Flexbox (satu dimensi) → fokus row/column. Cocok untuk navbar, toolbar, alignment komponen kecil.

Mudah mengatur spacing, alignment, wrapping.



Grid Layout (dua dimensi) → bekerja di baris + kolom sekaligus. Cocok untuk dashboard, galeri, layout utama dengan header/content/sidebar/footer.

Bisa definisi presisi area, track size fr/px/%, dan responsif.



# 5) Step-by-Step Implementasi

- Langkah 1 — Persiapan

Setup Django project + TailwindCSS.

Tambah model Product dengan field (name, description, thumbnail, category, user, created_at, dll).

- Langkah 2 — Routing & Views (Edit & Delete)

Tambah rute edit_product dan delete_product di urls.py.

Buat view dengan get_object_or_404, ProductForm, validasi form, redirect, dan proteksi @login_required.

- Langkah 3 — Tambah Tombol Aksi di Card

Tambahkan tombol Edit (link ke edit_product) dan Delete (form POST dengan CSRF token).

- Langkah 4 — Styling Form & Komponen

Gunakan Tailwind untuk input, textarea, select → ada efek focus, border, dan dark mode.

- Langkah 5 — Responsive List & Empty State

Jika product_list kosong → tampilkan ilustrasi empty.png.

Jika ada data → render dalam grid responsif (grid-cols-1, md:grid-cols-2, lg:grid-cols-3).

- Langkah 6 — Navbar Responsive

Navbar pakai flex + tombol ☰ untuk versi mobile.

Tambahkan JS sederhana toggle class hidden untuk mobile menu.

- Langkah 7 — Kustomisasi Halaman Auth & Produk

Terapkan tema konsisten: background gelap, card dengan shadow, button hover.

- Langkah 8 — Testing & Dokumentasi

Cek di resolusi mobile & desktop.

Update README (tambahkan subbab Tugas 5).

- Langkah 9 — Final Checklist

Validasi media thumbnail.

Pastikan permission edit/delete hanya bisa dilakukan oleh pemilik produk.

Tombol delete aman → hanya POST dengan CSRF.

</details>