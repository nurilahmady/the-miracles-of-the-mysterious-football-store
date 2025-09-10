# Tugas 2 PBP

## Jawaban 1
### Ceklis 1
Saya membuat sebuah proyek Django baru dimulai dengan menyiapkan direktori dan repositori. Dilanjut dengan membuat environment dengan menginstall beberapa dependencies tertentu seperti `django` dll. Kemudian memulai proyek Django dengan perintah `django-admin startproject` yang membuat proyek awal secara sederhana yang dilanjutkan dengan konfigurasi awal environment variables dan proyek
### Ceklis 2
Saya membuat aplikasi main menggunakan perintah `manage.py startapp`. Kemudian mendaftarkan main ke dalam proyek utama.
### Ceklis 3
Mengonfigurasi routing url proyek dengan menginclude main urls pada url pattern, tapi pastikan dulu urls sudah dibuat pada main.
### Ceklis 4
Mengonfigurasi file models pada main dengan membuat atribut serta tipenya sesuai dengan ketentuan pada soal.
### Ceklis 5
Mengonfigurasi file views agar merender file main.html pada template berisi struktur html sesuai yang diminta soal.
### Ceklis 6
Menambahkan path show_main pada url patterns.
### Ceklis 7
Create new project di pws dan mengizinkan proyek dihosting oleh pws, kemudian push code ke pws.
### Ceklis 8
Menulis readme di github.
  
**Mostly code yang saya bikin(untuk saat ini) mengikuti contoh dari yang diberikan pada tutorial**

## Jawaban 2

<img width="1297" height="770" alt="Screenshot 2025-09-09 191023" src="https://github.com/user-attachments/assets/0df7733c-e89a-435a-8232-13c58fdee343" />
Sumber: PPT 2 PBP

request masuk berupa url

urls.py: berisi peta rute URL yang menunjukkan view mana yang dieksekusi.

views.py: berperan sebagai logika aplikasi. Bisa mengambil/ubah data via model, lalu render template atau return JSON/redirect.

models.py: berisikan data dan logika program proyek.

Template HTML: bagian yang akan ditampilkan sebagai respon. Hanya membaca context dari view untuk ditampilkan.

## Jawaban 3
settings.py dalam proyek Django berperan sebagai pusat konfigurasi proyek. Hal-hal krusial yang diatur di sini misalnya:
- Identitas & Keamanan
- Aplikasi & Middleware
- Database & ORM
dan lain-lain

## Jawaban 4
Alur Kerja migrasi:
1. Definisikan/ubah model di models.py.
2. Buat berkas migrasi (instruksi perubahan skema):
3. Eksekusi(terapkan) migrasi ke DB:
4. Tracking: tabel django_migrations menyimpan migrasi yang sudah diterapkan.

## Jawaban 5
Disamping berbagai kelebihan yang dimiliki Django. Alasan utama dipilihnya framework ini karena Django adalah framework yang ramah pemula(Salah satunya karena pakai python). Hal ini mempercepat pembelajaran “from zero to a production-like app” sambil menanamkan best practices (keamanan, struktur, migrasi). Sehingga ROI yang didapatkan dalam setengah semester pembelajaran bisa didapat dengan cukup tinggi dan diharapkan menjadi fondasi agar mempermudah ketika belajar framework lain yang lebih umum dipakai.

## Jawaban 6
Untuk sementara belum ada kritik. Sudah cukup bagus. Terima kasih
