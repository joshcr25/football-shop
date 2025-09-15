# **Tugas Individu 2**

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step **(bukan hanya sekadar mengikuti tutorial).**

### **Langkah 1: Membuat Proyek Django**

Dalam direktori yang sama, buat berkas `requirements.txt` dan tambahkan dependensi berikut:

`django`  
`gunicorn`  
`whitenoise`  
`psycopg2-binary`  
`requests`  
`urllib3`  
`python-dotenv`

Lakukan instalasi dependensi dengan perintah berikut (pastikan Anda sudah mengaktifkan *virtual environment*):

`pip install -r requirements.txt`

Buat proyek Django bernama `football_shop` dengan perintah berikut. Pastikan ada karakter `.` di akhir perintah.

`django-admin startproject football_shop .`

**Peringatan:** Pastikan karakter `.` tertulis di akhir perintah.

### **Langkah 2: Membuat Aplikasi 'main'**

Jalankan perintah berikut untuk membuat aplikasi baru dengan nama main.

`python manage.py startapp main`

Direktori main akan terbentuk dengan struktur awal aplikasi Django Anda.

**Peringatan:** Jika Anda masih bingung mengenai istilah-istilah seperti direktori utama, direktori proyek, dan direktori aplikasi, tidak apa-apa\! Anda akan terbiasa seiring waktu. Semangat\!

**Mendaftarkan aplikasi main ke dalam proyek:**

Buka berkas `settings.py` di dalam direktori proyek `football_shop`. Tambahkan `main` ke dalam daftar `INSTALLED_APPS` sebagai elemen terakhir.

`INSTALLED_APPS = [`  
    `...,`  
    `'main'`  
`]`

Dengan langkah ini, aplikasi main sudah terdaftar di dalam proyek Anda.

### **Langkah 3: Mengonfigurasi Routing Proyek**

Buka berkas `urls.py` di dalam direktori proyek `football_shop` (bukan di dalam aplikasi `main`).

Impor fungsi include dari `django.urls`:

`from django.urls import path, include`

Tambahkan rute URL berikut ke dalam list `urlpatterns` untuk mengarahkan ke tampilan `main`:

`urlpatterns = [`  
    `...,`  
    `path('', include('main.urls')),`  
    `...`  
`]`

Jalankan proyek Django Anda dengan `python manage.py runserver`, lalu buka `http://localhost:8000/` di *browser* Anda.

### **Langkah 4: Membuat Model Product di Aplikasi main**

Buka berkas `models.py` pada direktori aplikasi main dan tambahkan kode berikut untuk mendefinisikan model Product.

`import uuid`  
`from django.db import models`

`class Product(models.Model):`  
    `CATEGORY_CHOICES = [`  
        `('transfer', 'Transfer'),`  
        `('update', 'Update'),`  
        `('exclusive', 'Exclusive'),`  
        `('match', 'Match'),`  
        `('rumor', 'Rumor'),`  
        `('analysis', 'Analysis'),`  
    `]`

    `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`  
    `name = models.CharField(max_length = 255)`  
    `price = models.IntegerField(default = 0)`  
    `description = models.TextField()`  
    `category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')`  
    `thumbnail = models.URLField(blank=True, null=True)`  
    `quantity = models.PositiveIntegerField(default=0)`  
    `brand = models.CharField(max_length=255)`  
    `year_of_manufacture = models.IntegerField(default=2025)`  
    `year_of_product = models.IntegerField(default=2025)`  
    `is_featured = models.BooleanField(default=False)`

    `def __str__(self):`  
        `return self.title`

**Membuat *routing* untuk aplikasi main:**

Buat berkas `urls.py` di dalam direktori main dan isi dengan kode berikut:

`from django.urls import path`  
`from main.views import show_main`

`app_name = 'main'`

`urlpatterns = [`  
    `path('', show_main, name='show_main'),`  
`]`

### **Langkah 5: Membuat Fungsi `show_main` di `views.py`**

Pada tahap ini, Anda akan menghubungkan view dengan template menggunakan Django.

**Langkah 1: Mengintegrasikan Komponen MVT**

Buka berkas `views.py` di direktori `main`. Tambahkan *import* dan fungsi `show_main`:

`from django.shortcuts import render`

`def show_main(request):`  
    `context = {`  
        `'npm' : '2406395291',`  
        `'name': 'Josh Christmas Rommlynn',`  
        `'class': 'PBP A'`  
    `}`

    `return render(request, "main.html", context)`

**Penjelasan Kode:**

* `from django.shortcuts import render`: Mengimpor fungsi render untuk me-render tampilan HTML.  
* `context`: *Dictionary* berisi data yang akan dikirim ke *template*.  
* `return render(...)`: Merender `main.html` dengan data dari context.

**Langkah 2: Memodifikasi *Template***

Buka berkas `main.html` dan ubah isinya untuk menampilkan data dari context.

`<h5>NPM: </h5>`  
`<p>{{ npm }}</p>`

`<h5>Name: </h5>`  
`<p>{{ name }}<p>`

`<h5>Class: </h5>`  
`<p>{{ class }}</p>`

Sintaks `{{ ... }}` adalah *template variables* Django yang digunakan untuk menampilkan nilai dari variabel context.

### **Langkah 6: Cara membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**

Buka berkas urls.py di dalam direktori proyek football-shop, bukan yang ada di dalam direktori aplikasi main.

Impor fungsi include dari `django.urls`.

`...`

`from django.urls import path, include`

`...`

Tambahkan rute URL berikut untuk mengarahkan ke tampilan main di dalam list `urlpatterns`.

`urlpatterns = [`

    `...`

    `path('', include('main.urls')),`

    `...`

`]`

### **Langkah 7: *Deployment* ke PWS**

Jalankan perintah berikut untuk membuat dan menerapkan migrasi database:

`python manage.py makemigrations`  
`python manage.py migrate`

Simpan semua perubahan ke GitHub dan PWS:

`git add .`  
`git commit -m "Complete assignment 1: Django MVT implementation"`  
`git push origin master`  
`git push pws master`

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`\!

Link bagan: [https://drive.google.com/file/d/1hoyReMOa3Q3JQk4O3hvuKEK9HosL7BuX/view?usp=sharing](https://drive.google.com/file/d/1hoyReMOa3Q3JQk4O3hvuKEK9HosL7BuX/view?usp=sharing)

Penjelasan bagan tersebut mengenai kaitan antara urls.py, views.py, models.py, dan berkas html: Di kotak "Client Request (Browser / HTTP)", ada metode show\_main(request) dan metode render(request, "main.html", context) di file views.py yang me-render main.html, lalu di kotak "urls.py Level Projek Django", jalanlah urls.py. Omong-omong, alur permintaan di bagan adalah "jalan" yang dilalui oleh permintaan pengguna, sedangkan models.py adalah "peta" dari data yang ada di "tujuan" jalan tersebut. Permintaan dari pengguna, misalnya untuk mendapatkan daftar produk, akan mengikuti alur di bagan, dan view yang dituju akan berinteraksi dengan model Product untuk mendapatkan data yang diperlukan dari database dan mengirimkannya kembali ke pengguna.

## Jelaskan peran settings.py dalam proyek Django\!

Peran settings.py dalam proyek Django adalah me-load variabel environment dari file .env, meladeni hosts di dalam variabel ALLOWED\_HOSTS yang mengizinkan host tertentu untuk dijalankan sekaligus menghindari serangan HTTP host header, mendefinisikan aplikasi yang diinstal, *middleware*, konfigurasi root URL, *template-template*, aplikasi WSGI, konfigurasi database, validasi kata sandi, dan lain-lainnya.

## Bagaimana cara kerja migrasi database di Django?

Cara kerja migrasi database di Django adalah menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data dengan menggunakan perintah makemigrations, lalu mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya dengan menggunakan perintah migrate.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena framework Django template-nya membantu banget untuk mengembangkan perangkat lunak dengan cepat. Jadi, pengguna hanya perlu memikirkan isi dari HTML utama, tidak perlu memikirkan bagaimana cara membuat proyeknya dari nol dengan kerangka proyeknya.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak ada, karena tutorial 1 yang telah saya kerjakan sebelumnya mudah dipahami.

## Dari mana SaccerBall berasal?

Nama SaccerBall dibuat karena nama tersebut tidak ada di Google Play Store dan mudah diingat. Nama tersebut berasal dari plesetan dari kata "Soccer ball", yang merupakan salah satu jenis olahraga bola. Nama ini singkat, unik, dan relevan dengan dunia olahraga bola.

# **Tugas 3: Data dan Formulir**

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena dengan data delivery dalam bentuk HTML, XML, dan JSON, kita dapat menampilkan konten website seperti teks, gambar, dan tautan di browser (HTML), mengubah bentuk yang dirancang agar mudah dimengerti hanya dengan membacanya karena *self-describing* (XML dan JSON).

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Yang lebih baik adalah JSON karena nama key-nya gk perlu disebutkan dua kali seperti XML. Omong-omong, JSON lebih populer dari XML karena sintaksnya lebih ringan, mudah dibaca manusia dibandingkan XML.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Metode is\_valid() di Django diperlukan untuk memvalidasi data yang dimasukkan pengguna melalui formulir, memastikan data tersebut aman, dan mengecek apakah itu sesuai dengan persyaratan yang ditentukan oleh definisi kolom formulir. Validasi ini penting untuk keamanan aplikasi, mencegah data tidak valid masuk ke basis data, dan menampilkan pesan kesalahan yang relevan kepada pengguna jika ada data yang tidak sesuai format formulir.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf\_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` melindungi formulir dari serangan *Cross-Site Request Forgery* (CSRF), di mana peretas menipu pengguna untuk melakukan tindakan yang tidak diinginkan. Jika `csrf_token` tidak ada, formulir akan rentan dan penyerang dapat memanfaatkan celah ini untuk merusak data atau akun.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### **Langkah 1: Implementasi Skeleton sebagai Kerangka Views**

1. Buat direktori templates di *root folder*, lalu buat berkas base.html sebagai *template* dasar. Isi dengan kode berikut:

`{% load static %}`  
`<!DOCTYPE html>`  
`<html lang="en">`  
`<head>`  
    `<meta charset="UTF-8" />`  
    `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`  
    `{% block meta %} {% endblock meta %}`  
`</head>`  
`<body>`  
    `{% block content %} {% endblock content %}`  
`</body>`  
`</html>`

Baris-baris yang dikurung dalam `{% ... %}` disebut dengan template tags Django. Baris-baris inilah yang akan berfungsi untuk memuat data secara dinamis dari Django ke HTML.

Pada contoh diatas, tag `{% block %}` di Django digunakan untuk mendefinisikan area dalam template yang dapat diganti oleh template turunan. Template turunan akan me-extend template dasar (pada contoh ini base.html) dan mengganti konten di dalam block ini sesuai kebutuhan.

2. Kemudian, buka `settings.py` yang ada pada direktori proyek (`football_news`) dan carilah baris yang mengandung variabel `TEMPLATES`. Sesuaikan kode yang ada dengan potongan kode berikut agar berkas `base.html` terdeteksi sebagai *template*.

`TEMPLATES = [`  
    `{`  
        `'BACKEND': 'django.template.backends.django.DjangoTemplates',`  
        `'DIRS': [BASE_DIR / 'templates'], # Tambahkan baris ini`  
        `'APP_DIRS': True,`  
        `...`  
    `}`  
`]`

**Info:** Dalam beberapa kasus, APP\_DIRS pada konfigurasi TEMPLATES kamu dapat bernilai False. Apabila nilainya False, ubah menjadi True. APP\_DIRS **harus** bernilai True. Hal ini dilakukan agar templates milik app (contohnya main) diprioritaskan daripada admin/base\_site.html milik **django.contrib.admin**. Untuk informasi lebih lanjut, kamu dapat mengakses halaman [ini](https://docs.djangoproject.com/en/5.1/ref/templates/api/#loading-templates).

3. Pada subdirektori templates yang ada pada direktori main (main/templates/), ubahlah kode berkas main.html yang telah dibuat di tutorial sebelumnya menjadi sebagai berikut.  
   {% extends 'base.html' %}  
   {% block content %}  
   \<h1\>SaccerBall\</h1\>  
   \<h5\>NPM: \</h5\>  
   \<p\>{{ npm }}\<p\>  
   \<h5\>Name:\</h5\>  
   \<p\>{{ name }}\</p\>  
   \<h5\>Class:\</h5\>  
   \<p\>{{ class }}\</p\>  
   {% endblock content %}  
     
   Perhatikan bahwa kode diatas merupakan kode yang sama dengan kode pada main.html pada tutorial sebelumnya. Perbedaannya adalah pada kode diatas, kita menggunakan `base.html` sebagai template utama.

### **Langkah 2: Membuat Form Input Data dan Menampilkan Data Football News Pada HTML**

Buat berkas baru pada direktori main dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data *Product* baru. Tambahkan kode berikut ke dalam berkas `forms.py`.

from django.forms import ModelForm

from main.models import Product

class ProductForm(ModelForm):

    class Meta:

        model \= Product

        fields \= \["name", "price", "description", "category", "thumbnail", "quantity", "brand", "year\_of\_manufacture", "year\_of\_product", "is\_featured"\]

#### **Penjelasan Kode:**

`model = Product` untuk menunjukkan model yang akan digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek News.

`fields = ["name", "price", "description", "category", "thumbnail", "quantity", "brand", "year_of_manufacture", "year_of_product", "is_featured"]` untuk menunjukkan field dari model News yang digunakan untuk form. Field `id` tidak dimasukkan ke list fields karena ditambahkan secara otomatis.

Buka berkas `views.py` yang ada pada direktori `main` dan tambahkan beberapa import berikut pada bagian paling atas, kemudian perbarui dan tambahkan fungsi-fungsi berikut:

`from django.shortcuts import render, redirect, get_object_or_404`

`from main.forms import ProductForm`

`from main.models import Product`

`def show_main(request):`

    `product_list = Product.objects.all()`

    

    `context = {`

        `'npm' : '2406395291',`

        `'name': 'Josh Christmas Rommlynn',`

        `'class': 'PBP A',`

        `'product_list' : product_list`

    `}`

    `return render(request, "main.html", context)`

`def create_product(request):`

    `form = ProductForm(request.POST or None)`

    `if form.is_valid() and request.method == "POST":`

        `form.save()`

        `return redirect('main:show_main')`

    `context = {'form': form}`

    `return render(request, "create_product.html", context)`

`def show_product(request, id):`

    `product = get_object_or_404(Product, pk=id)`

    `context = {`

        `'product': product`

    `}`

    `return render(request, "product_detail.html", context)`

3\. Buka `urls.py` yang ada pada direktori main dan import fungsi-fungsi yang sudah kamu buat tadi, kemudian tambahkan *path* URL ke dalam variabel `urlpatterns`:

`from django.urls import path`

`from main.views import show_main, create_product, show_product`

`app_name = 'main'`

`urlpatterns = [`

    `path('', show_main, name='show_main'),`

    `path('create-product/', create_product, name='create_product'),`

    `path('product/<str:id>/', show_product, name='show_product'),`

`]`

4. Buka `main.html` pada direktori `main/templates` dan update kode di dalam blok content untuk menampilkan data *news* serta tombol "Add News" yang akan *redirect* ke halaman *form*:

`{% extends 'base.html' %}`

`{% block content %}`

`<h1>SaccerBall</h1>`

`<h5>NPM: </h5>`

`<p>{{ npm }}</p>`

`<h5>Name: </h5>`

`<p>{{ name }}<p>`

`<h5>Class: </h5>`

`<p>{{ class }}</p>`

`<a href="{% url 'main:create_product' %}">`

  `<button>+ Add Product</button>`

`</a>`

`<hr>`

`{% if not product_list %}`

`<p>Belum ada data berita pada football news.</p>`

`{% else %}`

`{% for product in product_list %}`

`<div>`

  `<h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>`

  `<p><b>{{ product.category }}</b> | {% if product.is_featured %}` 

    `<b>Featured</b>{% endif %}<i> | Manufacturing year: {{ product.year_of_manufacture}} |` 

      `Product year: {{product.year_of_product}}</i> </p>`

  `{% if product.thumbnail %}`

  `<img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">`

  `<br />`

  `{% endif %}`

`<p>Deskripsi: {{ product.description | truncatewords:25 }}</p>`

  `<p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p>`

`</div>`

`<hr>`

`{% endfor %}`

`{% endif %}`

`{% endblock content %}`

5. Buat dua berkas HTML baru pada direktori `main/templates` untuk halaman form input dan detail berita:

**create\_product.html**

`{% extends 'base.html' %}` 

`{% block content %}`

`<h1>Add Product</h1>`

`<form method="POST">`

  `{% csrf_token %}`

  `<table>`

    `{{ form.as_table }}`

    `<tr>`

      `<td></td>`

      `<td>`

        `<input type="submit" value="Add Product" />`

      `</td>`

    `</tr>`

  `</table>`

`</form>`

`{% endblock %}`

**Penjelasan Kode:**

* `{% csrf_token %}` adalah token yang berfungsi sebagai security. Token ini di-*generate* secara otomatis oleh Django untuk mencegah serangan berbahaya.  
* `{{ form.as_table }}` adalah *template tag* yang digunakan untuk menampilkan fields form yang sudah dibuat pada `forms.py` sebagai table.

**product\_detail.html**

`{% extends 'base.html' %}`

`{% block content %}`

`<p><a href="{% url 'main:show_main' %}"><button>← Back to News List</button></a></p>`

`<h1>{{ product.name }}</h1>`

`<p><b>{{ product.category }}</b>{% if product.is_featured %} |` 

    `<b>Featured</b>{% endif %} | <i>Manufacturing year: {{ product.year_of_manufacture}} |` 

        `Product year: {{product.year_of_product}}</i></p>`

`{% if product.thumbnail %}`

`<img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">`

`<br /><br />`

`{% endif %}`

`<p>{{ product.description }}</p>`

`{% endblock content %}`

6. Buka `settings.py` pada direktori root project dan kemudian tambahkan entri url proyek pws kamu pada `CSRF_TRUSTED_ORIGINS` tepat setelah `ALLOWED_HOSTS`:

`...`

`CSRF_TRUSTED_ORIGINS = [`

    `"https://josh-christmas-footballshop.pbp.cs.ui.ac.id"`

`]`

`...`

Perlu diingat bahwa url deployment untuk `CSRF_TRUSTED_ORIGINS` harus mengandung protokol, sehingga urlnya akan dimulai dengan `https://` contohnya [`https://isa-citra-footballnews.pbp.cs.ui.ac.id`](https://isa-citra-footballnews.pbp.cs.ui.ac.id)`.`

7. Jalankan proyek Django-mu dengan perintah `python manage.py runserver` dan bukalah [http://localhost:8000/](http://localhost:8000/) di browser favoritmu. Coba tambahkan beberapa data news baru dan klik link judul atau tombol "Read More" untuk melihat detail berita. Seharusnya kamu dapat melihat data yang ditambahkan pada halaman utama aplikasi serta dapat mengakses halaman detail untuk setiap berita.

### **Langkah 3: Mengembalikan Data dalam Bentuk XML**

1. Buka `views.py` yang ada pada direktori main dan tambahkan *import* `HttpResponse` dan `Serializer` pada bagian paling atas.  
   `from django.http import HttpResponse`  
   `from django.core import serializers`  
   **Info:** `HttpResponse` merupakan *class* yang digunakan untuk menyusun respon yang ingin dikembalikan oleh server ke *user*. Kamu dapat mengakses materi lebih dalam terkait HttpRequest dan HttpResponse pada halaman berikut [ini](https://docs.djangoproject.com/en/5.2/ref/request-response/).  
2. Buatlah sebuah fungsi baru yang menerima parameter *request* dengan nama `show_xml` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil *query* dari seluruh data yang ada pada `Product`.  
   `def show_xml(request):`  
        `product_list = Product.objects.all()`  
3. Tambahkan *return function* berupa HttpResponse yang berisi parameter data hasil *query* yang sudah diserialisasi menjadi XML dan parameter content\_type="application/xml".  
   `def show_xml(request):`  
        `product_list = Product.objects.all()`  
        `xml_data = serializers.serialize("xml", news_list)`  
        `return HttpResponse(xml_data, content_type="application/xml")`  
4. Buka urls.py yang ada pada direktori main dan *import* fungsi yang sudah kamu buat tadi.  
   `from main.views import show_main, create_product, show_product, show_xml`  
5. Tambahkan *path url* ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.  
   `...`  
   `path('xml/', show_xml, name='show_xml'),`  
   `...`  
6. Jalankan proyek Django-mu dengan perintah `python manage.py runserver` dan bukalah [http://localhost:8000/xml/](http://localhost:8000/xml/) di browser favoritmu untuk melihat hasilnya.

### **Langkah 4: Mengembalikan Data dalam bentuk JSON**

1. ### Buka views.py yang ada pada direktori main dan buatlah sebuah fungsi baru yang menerima parameter *request* dengan nama show\_json dengan sebuah variabel di dalamnya yang menyimpan hasil *query* dari seluruh data yang ada pada Product.

   `def show_json(request):`  
       `product_list = Product.objects.all()`  
     
2. Tambahkan *return function* berupa HttpResponse yang berisi parameter data hasil *query* yang sudah diserialisasi menjadi JSON dan parameter content\_type="application/json".  
   `def show_json(request):`  
       `product_list = Product.objects.all()`  
       `json_data = serializers.serialize("json", news_list)`  
       `return HttpResponse(json_data, content_type="application/json")`  
3. Buka `urls.py` yang ada pada direktori `main` dan *import* fungsi yang sudah kamu buat tadi.  
     
   `from main.views import show_main, create_product, show_product, show_xml, show_json`  
     
4. Tambahkan *path url* ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.  
   `...`  
   `path('json/', show_json, name='show_json'),`  
   `…`  
5. Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah [http://localhost:8000/json/](http://localhost:8000/json/) (sesuaikan dengan *path url* yang dibuat) di browser favoritmu untuk melihat hasilnya.

### **Langkah 5: Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON**

1. ### Buka views.py yang ada pada direktori main dan buatlah dua fungsi baru yang menerima parameter request dan product\_id dengan nama show\_xml\_by\_id dan show\_json\_by\_id.

2. Buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada `News`.  
   `news_item = News.objects.filter(pk=news_id)`  
3. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type` dengan value "`application/xml`" (untuk format XML) atau "`application/json`" (untuk format JSON).  
* XML

  `def show_xml_by_id(request, news_id):`

     `product_item = Product.objects.filter(pk=news_id)`

     `xml_data = serializers.serialize("xml", product_item)`

     `return HttpResponse(xml_data, content_type="application/xml")`

* JSON

  `def show_json_by_id(request, news_id):`

     `product_item = Product.objects.get(pk=news_id)`

     `json_data = serializers.serialize("json", [news_item])`

     `return HttpResponse(json_data, content_type="application/json")`

**Info:** Untuk mendapatkan data berdasarkan ID, kita dapat menggunakan berbagai jenis method milik **Django**, dua di antaranya adalah filter() dan get(). Namun, kedua method ini memiliki perbedaan yang cukup signifikan. filter() dapat digunakan untuk mengambil data satu objek atau berbagai objek yang memenuhi kondisi yang ditetapkan, sedangkan get() dapat digunakan untuk mengambil data satu objek saja. Kamu dapat membaca lebih lanjut terkait hal ini pada halaman berikut [ini](https://docs.djangoproject.com/en/5.2/topics/db/queries/#retrieving-a-single-object-with-get).

4. Tambahkan blok try except pada fungsi untuk mengantisipasi kondisi ketika data dengan product\_id tertentu tidak ditemukan dalam basis data. Jika data tidak ditemukan, kembalikan HttpResponse dengan status 404 sebagai tanda data tidak ada.  
* XML  
  `def show_xml_by_id(request, product_id):`  
     `try:`  
         `product_item = Product.objects.filter(pk=product_id)`  
         `xml_data = serializers.serialize("xml", product_item)`  
         `return HttpResponse(xml_data, content_type="application/xml")`  
     `except Product.DoesNotExist:`  
         `return HttpResponse(status=404)`  
* JSON  
  `def show_json_by_id(request, product_id):`  
     `try:`  
         `product_item = Product.objects.get(pk=product_id)`  
         `json_data = serializers.serialize("json", [product_item])`  
         `return HttpResponse(json_data, content_type="application/json")`  
     `except Product.DoesNotExist:`  
         `return HttpResponse(status=404)`  
5. Buka urls.py yang ada pada direktori main dan *import* fungsi yang sudah kamu buat tadi.  
   `from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id`  
6. Tambahkan *path* URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.  
   `...`  
    `path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),`  
    `path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),`  
   `...`  
7. Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah [http://localhost:8000/xml/\[news\_id\]/](http://localhost:8000/xml/%5Bnews_id%5D/) atau [http://localhost:8000/json/\[news\_id\]/](http://localhost:8000/json/%5Bnews_id%5D/) di browser favoritmu untuk melihat hasilnya.

**Peringatan:** Sesuaikan \[news\_id\] pada URL di atas dengan id objek yang ingin dilihat. Kamu dapat mengambil salah satu ID objek yang ditampilkan ketika mengakses *endpoint* /xml/ dan /json/.

## Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada, karena tutorial 2 udh cukup jelas dan runtut.

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat *screenshot* dari hasil akses URL pada Postman, dan menambahkannya ke dalam [README.md](http://README.md).

Screenshotnya dapat diakses di [https://drive.google.com/drive/folders/1aGJNKYRxaZ1nBNi0BT1KS-NhMz7u04eg?usp=drive\_link](https://drive.google.com/drive/folders/1aGJNKYRxaZ1nBNi0BT1KS-NhMz7u04eg?usp=drive_link) 