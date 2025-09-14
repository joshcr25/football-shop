Tugas 2



Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Langkah 1. Cara membuat Proyek Django:

Di dalam direktori yang sama, buat berkas `requirements.txt` dan tambahkan beberapa dependencies.



```

django

gunicorn

whitenoise

psycopg2-binary

requests

urllib3

python-dotenv

```



Lakukan instalasi terhadap dependencies yang ada dengan perintah berikut. Jangan lupa jalankan virtual environment terlebih dahulu sebelum menjalankan perintah berikut.



`pip install -r requirements.txt`



Buat proyek Django bernama `football\\\\\\\_shop` dengan perintah berikut.



`django-admin startproject football\\\\\\\_shop .`



Peringatan

Pastikan karakter `.` tertulis di akhir perintah.



Langkah 2. Cara membuat aplikasi dengan nama main pada proyek football-shop:

Jalankan perintah berikut untuk membuat aplikasi baru dengan nama main.



`python manage.py startapp main`



Setelah perintah di atas dijalankan, direktori baru dengan nama main akan terbentuk. Direktori main akan berisi struktur awal untuk aplikasi Django kamu.



Peringatan

Jika kamu masih bingung mengenai istilah-istilah baru seperti direktori utama, direktori proyek, direktori aplikasi, it's' okay! Kamu akan terbiasa seiring berjalannya waktu. Semangat!



Mendaftarkan aplikasi main ke dalam proyek.



Buka berkas `settings.py` di dalam direktori proyek `football\\\\\\\_shop`.



Tambahkan `main` ke dalam daftar aplikasi yang ada sebagai elemen paling terakhir. Daftar aplikasi dapat kamu akses pada variabel `INSTALLED\\\\\\\_APPS`.



```

INSTALLED\\\\\\\_APPS = \\\\\\\[

    ...,

    'main'

]

```



Dengan melakukan langkah-langkah tersebut, kamu telah mendaftarkan aplikasi main ke dalam proyek football shop kamu.





Langkah 3. Cara mengonfigurasikan routing pada proyek agar dapat menjalankan aplikasi main:



Buka berkas urls.py di dalam direktori proyek football-news, bukan yang ada di dalam direktori aplikasi main.

Impor fungsi include dari `django.urls`.



```

...

from django.urls import path, include

...

```



Tambahkan rute URL berikut untuk mengarahkan ke tampilan main di dalam list urlpatterns.



```

urlpatterns = \\\\\\\[

    ...

    path('', include('main.urls')),

    ...

]

```



Jalankan proyek Django kamu dengan python manage.py runserver.

Bukalah `http://localhost:8000/` di web browser untuk melihat halaman yang sudah kamu buat.



Langkah 4. Cara membuat model pada aplikasi main dengan nama Product:

Langkah 1: Mengubah Berkas `models.py` dalam Aplikasi main

Pada langkah ini, kamu akan mengubah berkas `models.py` yang terdapat di dalam direktori aplikasi main untuk mendefinisikan model baru.



Buka berkas `models.py` pada direktori aplikasi main.

Isi berkas `models.py` dengan kode berikut.



```

import uuid

from django.db import models



class Product(models.Model):

    CATEGORY\\\\\\\_CHOICES = \\\\\\\[

        ('transfer', 'Transfer'),

        ('update', 'Update'),

        ('exclusive', 'Exclusive'),

        ('match', 'Match'),

        ('rumor', 'Rumor'),

        ('analysis', 'Analysis'),

    ]

 

    id = models.UUIDField(primary\\\\\\\_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max\\\\\\\_length = 255)

    price = models.IntegerField(default = 0)

    description = models.TextField()

    category = models.CharField(max\\\\\\\_length=20, choices=CATEGORY\\\\\\\_CHOICES, default='update')

    thumbnail = models.URLField(blank=True, null=True)

    quantity = models.PositiveIntegerField(default=0)

    brand = models.CharField(max\\\\\\\_length=255)

    year\\\\\\\_of\\\\\\\_manufacture = models.IntegerField(default=2025) # Tahun pembuatan produk

    year\\\\\\\_of\\\\\\\_product = models.IntegerField(default=2025) # Tahun produk muncul di toko bola

    is\\\\\\\_featured = models.BooleanField(default=False)

 

    def \\\\\\\_\\\\\\\_str\\\\\\\_\\\\\\\_(self):

        return self.title

```



Cara membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`:



Buatlah berkas `urls.py` di dalam direktori `main`.

Isi `urls.py` dengan kode berikut:



```

from django.urls import path

from main.views import show\\\\\\\_main



app\\\\\\\_name = 'main'



urlpatterns = \\\\\\\[

    path('', show\\\\\\\_main, name='show\\\\\\\_main'),

]

```



Langkah 5. Cara membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:

Pada tahap ini, kamu akan menghubungkan komponen view dengan komponen template menggunakan Django.



Langkah 1: Mengintegrasikan Komponen MVT

Kamu akan mengimpor modul yang diperlukan dan membuat fungsi view `show\\\\\\\_main`.



Buka berkas `views.py` yang terletak di dalam berkas aplikasi main.



Apabila belum ada, tambahkan baris-baris import berikut di bagian paling atas berkas.



```

from django.shortcuts import render

```



Penjelasan Kode:



`from django.shortcuts import render` berguna untuk mengimpor fungsi render dari modul `django.shortcuts`.

Fungsi render akan digunakan untuk render tampilan HTML dengan menggunakan data yang diberikan.

Tambahkan fungsi `show\\\\\\\_main` di bawah impor:



```

def show\\\\\\\_main(request):

    context = {

        'npm' : '2406395291',

        'name': 'Josh Christmas Rommlynn',

        'class': 'PBP A'

    }



    return render(request, "main.html", context)

```



Penjelasan Kode:



Potongan kode di atas mendeklarasikan fungsi `show\\\\\\\_main`, yang menerima parameter request. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.



context adalah dictionary yang berisi data untuk dikirimkan ke tampilan. Pada saat ini, terdapat tiga data yang disertakan, yaitu:



`npm`: Data npm-mu.

`name`: Data namamu.

`class`: Data kelasmu.

`return render(request, "main.html", context)` berguna untuk me-render tampilan `main.html` dengan menggunakan fungsi render. Fungsi render mengambil tiga argumen:



`request`: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.

`main.html`: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.

`context`: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.

Langkah 2: Modifikasi Template

Pada tahap ini, kamu akan mengubah template `main.html` agar dapat menampilkan data yang telah diambil dari model.



Buka berkas `main.html` yang telah dibuat sebelumnya dalam direktori templates pada direktori main.



Ubah nama dan kelas menjadi struktur kode Django yang sesuai untuk menampilkan data.



```

...

<h5>NPM: </h5>

<p>{{ npm }}</p>

<h5>Name: </h5>

<p>{{ name }}<p>

<h5>Class: </h5>

<p>{{ class }}</p>

...

```



Penjelasan Kode:



Sintaks `Django {{ npm }}, {{ name }} dan {{ class }}`, disebut template variables, digunakan untuk menampilkan nilai dari variabel yang telah didefinisikan dalam context.



Langkah 6: Cara membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`



Buka berkas `urls.py` di dalam direktori proyek `football-shop`, bukan yang ada di dalam direktori aplikasi main.

Impor fungsi include dari `django.urls`.



```

...

from django.urls import path, include

...

```



Tambahkan rute URL berikut untuk mengarahkan ke tampilan main di dalam list `urlpatterns`.

```

urlpatterns = \\\\\\\[

    ...

    path('', include('main.urls')),

    ...

]

```



 

Langkah 7. Cara men-deploy ke PWS agar teman-teman saya dapat diakses melalui Internet:

Jalankan perintah berikut untuk membuat migrasi model.

`python manage.py makemigrations`



Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal.



`python manage.py migrate`



Simpan semua perubahan ke GitHub dan PWS:

```

git add .

git commit -m "Complete assignment 1: Django MVT implementation"

git push origin master

git push pws master

```





Buatlah bagan yang berisi request client ke web aplikasi berbasis Django berserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`!

Link bagan: https://drive.google.com/file/d/1hoyReMOa3Q3JQk4O3hvuKEK9HosL7BuX/view?usp=sharing

Penjelasan bagan tersebut mengenai kaitan antara urls.py, views.py, models.py, dan berkas html: Di kotak "Client Request (Browser / HTTP)", ada metode show\_main(request) dan metode render(request, "main.html", context) di file views.py yang me-render main.html, lalu di kotak "urls.py Level Projek Django", jalanlah urls.py. Omong-omong, alur permintaan di bagan adalah "jalan" yang dilalui oleh permintaan pengguna, sedangkan models.py adalah "peta" dari data yang ada di "tujuan" jalan tersebut. Permintaan dari pengguna, misalnya untuk mendapatkan daftar produk, akan mengikuti alur di bagan, dan view yang dituju akan berinteraksi dengan model Product untuk mendapatkan data yang diperlukan dari database dan mengirimkannya kembali ke pengguna.



Jelaskan peran `settings.py` dalam proyek Django!

Peran settings.py dalam proyek Django adalah me-load variabel environment dari file .env, meladeni hosts di dalam variabel ALLOWED\_HOSTS yang mengizinkan host tertentu untuk dijalankan sekaligus menghindari serangan HTTP host header, mendefinisikan aplikasi yang diinstal, middleware, konfigurasi root URL, template-template, aplikasi WSGI, konfigurasi database, validasi kata sandi, dan lain-lainnya.



Bagaimana cara kerja migrasi database di Django?

Cara kerja migrasi database di Django adalah menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data dengan menggunakan perintah makemigrations, lalu mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya dengan menggunakan perintah migrate.



Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena framework Django template-nya membantu banget untuk mengembangkan perangkat lunak dengan cepat. Jadi, pengguna hanya perlu memikirkan isi dari HTML utama, tidak perlu memikirkan bagaimana cara membuat proyeknya dari nol dengan kerangka proyeknya.



Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak ada, karena tutorial 1 yang telah saya kerjakan sebelumnya mudah dipahami.



Dari mana SaccerBall berasal?

Nama SaccerBall dibuat karena nama tersebut tidak ada di Google Play Store dan mudah diingat. Nama tersebut berasal dari plesetan dari kata "Soccer ball", yang merupakan salah satu jenis olahraga bola. Nama ini singkat, unik, dan relevan dengan dunia olahraga bola.



Tugas 3

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena dengan data delivery dalam bentuk HTML, XML, dan JSON, kita dapat menampilkan konten website seperti teks, gambar, dan tautan di browser (HTML), mengubah bentuk yang dirancang agar mudah dimengerti hanya dengan membacanya karena self-describing (XML dan JSON).



### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Yang lebih baik adalah JSON karena nama key-nya gk perlu disebutkan dua kali seperti XML. Omong-omong, JSON lebih populer dari XML karena sintaksnya lebih ringan, mudah dibaca manusia dibandingkan XML.





### Jelaskan fungsi dari method is\_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Metode is\_valid() di Django diperlukan untuk memvalidasi data yang dimasukkan pengguna melalui formulir, memastikan data tersebut aman, dan mengecek apakah itu sesuai dengan persyaratan yang ditentukan oleh definisi kolom formulir. Validasi ini penting untuk keamanan aplikasi, mencegah data tidak valid masuk ke basis data, dan menampilkan pesan kesalahan yang relevan kepada pengguna jika ada data yang tidak sesuai format formulir. 



### Mengapa kita membutuhkan csrf\_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf\_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?



csrf\_token saat membuat form di Django bertujuan untuk melindungi dari serangan berbahaya, di mana peretas mengelabui pengguna untuk melakukan tindakan yang tidak diinginkan atas namanya sendiri. Jika kita tidak menambahkannya, maka form Django akan rentan terhadap penyerang yang mengelabuinya.



### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).



#### 



### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?



Tidak ada, karena tutorial 2 udh cukup jelas dan runtut.

