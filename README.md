# **Tugas Individu 2**

## **Penjelasan Implementasi Langkah demi Langkah**

### **Langkah 1: Membuat Proyek Django**

1. Di direktori yang sama, buat berkas requirements.txt dan tambahkan dependensi berikut:

```

django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
python-dotenv
```

2. Instal dependensi dengan perintah berikut (pastikan Anda sudah mengaktifkan *virtual environment*):

```

pip install -r requirements.txt

```

3. Buat proyek Django bernama football\_shop dengan perintah berikut. Pastikan ada karakter . di akhir perintah.

```

django-admin startproject football_shop .

```

**Peringatan:** Pastikan karakter . tertulis di akhir perintah.

### **Langkah 2: Membuat Aplikasi 'main'**

1. Jalankan perintah berikut untuk membuat aplikasi baru dengan nama main.

```

python manage.py startapp main

```

2. Direktori main akan terbentuk dengan struktur awal aplikasi Django Anda.

**Peringatan:** Jika Anda masih bingung mengenai istilah seperti direktori utama, direktori proyek, dan direktori aplikasi, jangan khawatir\! Anda akan terbiasa seiring waktu. Semangat\!

**Mendaftarkan aplikasi main ke dalam proyek:**

3. Buka berkas settings.py di dalam direktori proyek football\_shop. Tambahkan 'main' ke dalam daftar INSTALLED\_APPS sebagai elemen terakhir.

```

INSTALLED_APPS = [
    ...,
    'main'
]

```

### **Langkah 3: Mengonfigurasi Routing Proyek**

1. Buka berkas urls.py di dalam direktori proyek football\_shop.

Impor fungsi include dari django.urls:

```

from django.urls import path, include

```

2. Tambahkan rute URL berikut ke dalam list urlpatterns untuk mengarahkan ke tampilan main:

```

urlpatterns = [
    ...,
    path('', include('main.urls')),
    ...
]

```

3. Jalankan proyek Django Anda dengan python manage.py runserver, lalu buka http://localhost:8000/ di *browser*.

### **Langkah 4: Membuat Model Product di Aplikasi main**

1. Buka berkas models.py pada direktori aplikasi main dan tambahkan kode berikut untuk mendefinisikan model Product.

```

import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    price = models.IntegerField(default = 0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255)
    year_of_manufacture = models.IntegerField(default=2025)
    year_of_product = models.IntegerField(default=2025)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

```

**Catatan:** Fungsi \_\_str\_\_ pada model Product harusnya mengembalikan self.name bukan self.title. Perubahan ini sudah saya tambahkan.

2. Buat berkas urls.py di dalam direktori main dan isi dengan kode berikut:

```

from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

```

### **Langkah 5: Membuat Fungsi show\_main di views.py**

**Langkah 1: Mengintegrasikan Komponen MVT**

1. Buka berkas views.py di direktori main. Tambahkan *import* dan fungsi show\_main:

```

from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406395291',
        'name': 'Josh Christmas Rommlynn',
        'class': 'PBP A'
    }
    return render(request, "main.html", context)

```

**Penjelasan Kode:**

* from django.shortcuts import render: Mengimpor fungsi render untuk me-render tampilan HTML.  
* context: *Dictionary* berisi data yang akan dikirim ke *template*.  
* return render(...): Merender main.html dengan data dari context.

**Langkah 2: Memodifikasi Template**

2. Buka berkas main.html dan ubah isinya untuk menampilkan data dari context.

```

<h5>NPM: </h5>
<p>{{ npm }}</p>

<h5>Name: </h5>
<p>{{ name }}</p>

<h5>Class: </h5>
<p>{{ class }}</p>

```

Sintaks {{ ... }} adalah *template variables* Django yang digunakan untuk menampilkan nilai dari variabel context.

### **Langkah 6: Routing Tambahan pada urls.py**

1. Buka berkas urls.py di dalam direktori proyek football-shop.  
2. Impor fungsi include dari django.urls:

```

from django.urls import path, include

```

3. Tambahkan rute URL berikut di dalam list urlpatterns:

```

urlpatterns = [
    ...,
    path('', include('main.urls')),
    ...
]

```

### **Langkah 7: Deployment ke PWS**

1. Jalankan perintah berikut untuk membuat dan menerapkan migrasi database:

```

python manage.py makemigrations
python manage.py migrate

```

2. Simpan semua perubahan ke GitHub dan PWS:

```

git add .
git commit -m "Complete assignment 1: Django MVT implementation"
git push origin master
git push pws master

```

## **Bagan Alur Permintaan dan Respon Django**

Link bagan: [https://drive.google.com/file/d/1hoyReMOa3Q3JQk4O3hvuKEK9HosL7BuX/view?usp=sharing](https://drive.google.com/file/d/1hoyReMOa3Q3JQk4O3hvuKEK9HosL7BuX/view?usp=sharing)

Penjelasan bagan:

Permintaan dari klien (browser) ke web aplikasi Django melalui HTTP. Alur permintaan ini dimulai dari urls.py yang memetakan URL ke fungsi di views.py. views.py kemudian berinteraksi dengan models.py untuk mengambil data dari database, dan menggunakan template html untuk merender tampilan yang akan dikembalikan sebagai respons. Dalam alur ini, urls.py berfungsi sebagai direktori rute, views.py sebagai logika pemroses, models.py sebagai skema data, dan berkas .html sebagai tampilan.

## **Peran settings.py dalam Proyek Django**

Berkas **settings.py** adalah jantung dari setiap proyek Django. Fungsinya mencakup:

* **Memuat variabel lingkungan** dari berkas .env.  
* **Mengizinkan host** (ALLOWED\_HOSTS) untuk mencegah serangan *HTTP host header*.  
* **Mendefinisikan aplikasi** yang diinstal dalam proyek (INSTALLED\_APPS).  
* **Mengonfigurasi *middleware***, **root URL**, ***template***, **aplikasi WSGI**, **database**, **validasi kata sandi**, dan banyak lagi.

## **Cara Kerja Migrasi Database di Django**

Migrasi database di Django bekerja dalam dua tahap:

1. **python manage.py makemigrations**: Perintah ini **menciptakan berkas migrasi** yang berisi perubahan pada model Anda. Berkas ini belum diterapkan ke database, hanya mencatat perubahan yang perlu dilakukan.  
2. **python manage.py migrate**: Perintah ini **menerapkan perubahan** yang tercantum dalam berkas migrasi ke dalam database.

## **Mengapa Django Ideal untuk Pembelajaran Awal Pengembangan Perangkat Lunak?**

Django sering dijadikan titik awal karena **struktur proyeknya yang sudah terdefinisi** (kerangka proyek). Dengan kerangka ini, pengguna dapat langsung fokus pada konten dan logika aplikasi, bukan dari nol. Ini mempercepat proses belajar dan memberikan pengalaman yang lebih terstruktur.

## **Umpan Balik untuk Asisten Dosen Tutorial 1**

Tidak ada, karena tutorial 1 sudah mudah dipahami.

## **Asal Nama SaccerBall**

Nama **SaccerBall** adalah plesetan dari kata "Soccer ball". Nama ini dibuat karena tidak ada di Google Play Store dan mudah diingat, menjadikannya unik dan relevan dengan dunia olahraga bola.

# **Tugas 3: Data dan Formulir**

## **Mengapa Data Delivery Penting dalam Implementasi Platform?**

Kita memerlukan data *delivery* dalam bentuk **HTML**, **XML**, dan **JSON** untuk menampilkan konten website secara efektif.

* **HTML** untuk menampilkan teks, gambar, dan tautan di *browser*.  
* **XML** dan **JSON** untuk mengubah data menjadi format yang *self-describing* dan mudah dibaca oleh manusia atau mesin.

## **Perbandingan XML dan JSON**

**JSON** lebih baik dan lebih populer daripada **XML** karena:

* **Sintaksnya lebih ringan** dan tidak memerlukan nama *key* berulang kali.  
* **Lebih mudah dibaca** dan dipahami oleh manusia.

## **Fungsi Method is\_valid() pada Form Django**

Method is\_valid() pada formulir Django berfungsi untuk **memvalidasi data input pengguna**. Kita membutuhkannya untuk:

* **Memastikan data aman** dan sesuai dengan persyaratan yang ditentukan.  
* **Mencegah data tidak valid** masuk ke database.  
* **Menampilkan pesan kesalahan** yang relevan kepada pengguna jika ada data yang tidak sesuai.

## **Pentingnya csrf\_token pada Form Django**

**csrf\_token** melindungi formulir dari serangan **Cross-Site Request Forgery (CSRF)**. Jika token ini tidak ada, penyerang bisa menipu pengguna untuk melakukan tindakan yang tidak diinginkan, seperti mengubah data atau mengirimkan informasi tanpa sepengetahuan pengguna. Django mengelola token ini secara otomatis untuk mengamankan formulir.

## **Penjelasan Implementasi Langkah demi Langkah**

### **Langkah 1: Implementasi Skeleton sebagai Kerangka Views**

1. Buat direktori templates di *root folder*, lalu buat berkas base.html sebagai *template* dasar.

```

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>
<body>
    {% block content %} {% endblock content %}
</body>
</html>

```

Tag {% block %} di Django mendefinisikan area dalam *template* yang dapat diganti oleh *template* turunan.

2. Buka settings.py dan sesuaikan variabel TEMPLATES agar berkas base.html terdeteksi.

```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan baris ini
        'APP_DIRS': True,
        ...
    }
]

```

3.   
   Pada subdirektori main/templates, ubah kode main.html menjadi:

```

{% extends 'base.html' %}
{% block content %}
<h1 style="color: blue;">SaccerBall</h1>
<h5 style="color: blue;">NPM: </h5>
<p style="font-weight: bold;">{{ npm }}</p>
<h5 style="color: blue;">Name:</h5>
<p style="font-weight: bold;">{{ name }}</p>
<h5 style="color: blue;">Class:</h5>
<p style="font-weight: bold;">{{ class }}</p>
{% endblock content %}

```

Perhatikan bahwa main.html sekarang mewarisi dari base.html dan mengisi blok content.

### **Langkah 2: Membuat Form Input dan Menampilkan Data**

1. Buat berkas baru di direktori main bernama forms.py untuk struktur form.

```

from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "quantity", "brand", "year_of_manufacture", "year_of_product", "is_featured"]

```

2.   
   Buka views.py dan tambahkan *import* serta fungsi-fungsi berikut:

```

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_list = Product.objects.all()
    context = {
        'npm': '2406395291',
        'name': 'Josh Christmas Rommlynn',
        'class': 'PBP A',
        'product_list': product_list
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

```

3.   
   Buka urls.py di direktori main dan tambahkan *path* URL:

```

from django.urls import path
from main.views import show_main, create_product, show_product
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
]

```

4.   
   Perbarui main.html untuk menampilkan daftar produk dan tombol "Add Product".

```

{% extends 'base.html' %}
{% block content %}
<h1>SaccerBall</h1>
<h5>NPM: </h5>
<p>{{ npm }}</p>
<h5>Name: </h5>
<p>{{ name }}</p>
<h5>Class: </h5>
<p>{{ class }}</p>
<a href="{% url 'main:create_product' %}">
  <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">+ Add Product</button>
</a>
<hr style="border: 1px solid #ddd;">
{% if not product_list %}
<p>Belum ada data berita pada football news.</p>
{% else %}
{% for product in product_list %}
<div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 15px; border-radius: 8px;">
  <h2 style="color: blue;"><a href="{% url 'main:show_product' product.id %}" style="text-decoration: none; color: blue;">{{ product.name }}</a></h2>
  <p>
    <b>{{ product.category }}</b>
    {% if product.is_featured %} | <b>Featured</b>{% endif %}
    <i> | Manufacturing year: {{ product.year_of_manufacture}} | Product year: {{product.year_of_product}}</i>
  </p>
  {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100" style="border-radius: 5px;">
    <br />
  {% endif %}
  <p>Deskripsi: {{ product.description | truncatewords:25 }}</p>
  <p>
    <a href="{% url 'main:show_product' product.id %}">
      <button style="background-color: #008CBA; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer;">Read More</button>
    </a>
  </p>
</div>
<hr style="border: 1px solid #ddd;">
{% endfor %}
{% endif %}
{% endblock content %}

```

5.   
   Buat dua berkas HTML baru: create\_product.html dan product\_detail.html.

**create\_product.html**

```

{% extends 'base.html' %} 
{% block content %}
<div style="padding: 20px; border: 1px solid #ccc; border-radius: 8px; max-width: 600px; margin: 20px auto;">
  <h1 style="color: blue;">Add Product</h1>
  <form method="POST">
    {% csrf_token %}
    <table style="width: 100%; border-collapse: collapse;">
      {{ form.as_table }}
      <tr>
        <td></td>
        <td>
          <input type="submit" value="Add Product" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;" />
        </td>
      </tr>
    </table>
  </form>
</div>
{% endblock %}

```

**product\_detail.html**

```

{% extends 'base.html' %}
{% block content %}
<div style="padding: 20px; border: 1px solid #ccc; border-radius: 8px; max-width: 800px; margin: 20px auto;">
  <p>
    <a href="{% url 'main:show_main' %}">
      <button style="background-color: #f44336; color: white; padding: 8px 16px; border: none; border-radius: 5px; cursor: pointer;">← Back to Product List</button>
    </a>
  </p>
  <h1 style="color: blue;">{{ product.name }}</h1>
  <p>
    <b>{{ product.category }}</b>
    {% if product.is_featured %} | <b>Featured</b>{% endif %}
    <i> | Manufacturing year: {{ product.year_of_manufacture}} | Product year: {{product.year_of_product}}</i>
  </p>
  {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300" style="border-radius: 5px;">
    <br /><br />
  {% endif %}
  <p>{{ product.description }}</p>
</div>
{% endblock content %}

```

6.   
   Tambahkan URL deployment ke CSRF\_TRUSTED\_ORIGINS di settings.py.

```

CSRF_TRUSTED_ORIGINS = [
    "[https://josh-christmas-footballshop.pbp.cs.ui.ac.id](https://josh-christmas-footballshop.pbp.cs.ui.ac.id)"
]

```

7.   
   Jalankan proyek dan uji coba.

### **Langkah 3: Mengembalikan Data dalam Bentuk XML**

1. Buka views.py dan tambahkan import HttpResponse dan serializers.

```

from django.http import HttpResponse
from django.core import serializers

```

2.   
   Buat fungsi show\_xml.

```

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

```

3.   
   Tambahkan *path* URL di urls.py.

```

path('xml/', show_xml, name='show_xml'),

```

### **Langkah 4: Mengembalikan Data dalam Bentuk JSON**

1. Buka views.py dan buat fungsi show\_json.

```

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

```

2.   
   Tambahkan *path* URL di urls.py.

```

path('json/', show_json, name='show_json'),

```

### **Langkah 5: Mengembalikan Data Berdasarkan ID (XML dan JSON)**

1. Buka views.py dan buat dua fungsi baru, show\_xml\_by\_id dan show\_json\_by\_id.

```

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

```

2.   
   Tambahkan *path* URL di urls.py.

```

path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),

```

## **Umpan Balik untuk Asisten Dosen Tutorial 2**

Tidak ada, karena tutorial 2 sudah cukup jelas dan runtut.

## **Screenshot Postman**

Screenshot dapat diakses di: [https://drive.google.com/drive/folders/1aGJNKYRxaZ1nBNi0BT1KS-NhMz7u04eg?usp=drive\_link](https://drive.google.com/drive/folders/1aGJNKYRxaZ1nBNi0BT1KS-NhMz7u04eg?usp=drive_link)

# **Tugas Individu 4**

## **Django Authentication Form**

**Django Authentication Form** adalah formulir bawaan Django yang menangani proses otentikasi pengguna, seperti *login* dan *password hashing*.

* **Kelebihan**: Mudah dikustomisasi, keamanan bawaan (termasuk *password hashing* dan manajemen sesi), dan fleksibel.  
* **Kekurangan**: Ketergantungan pada sistem sesi berbasis *cookie*, yang bisa menjadi tantangan untuk aplikasi dengan arsitektur *frontend* dan *backend* terpisah.

## **Perbedaan Autentikasi dan Otorisasi**

* **Autentikasi** menjawab "Siapa kamu?".  
* **Otorisasi** menentukan "Apa yang boleh kamu lakukan?".

Django mengimplementasikan **autentikasi** dengan sistem otentikasi bawaan yang menggunakan *cookie* dan ID sesi, serta menyediakan *views* untuk *login* dan *logout*. Untuk **otorisasi**, Django menggunakan model User dan sistem Permissions untuk mengontrol akses.

## **Kelebihan dan Kekurangan Session dan Cookies**

* **Session**:  
  * **Kelebihan**: Data disimpan di server, lebih aman untuk informasi sensitif.  
  * **Kekurangan**: Kapasitas terbatas, data dapat hilang jika sesi berakhir.  
* **Cookies**:  
  * **Kelebihan**: Data disimpan di *browser* pengguna, dapat digunakan untuk data yang persisten.  
  * **Kekurangan**: Kurang aman, rentan terhadap intersepsi, dan kapasitasnya sangat kecil.

## **Keamanan Cookies dan Penanganan Django**

Penggunaan *cookie* secara *default* **tidak aman** karena risiko intersepsi dan penyalahgunaan. Namun, Django menangani ini secara proaktif dengan atribut seperti Secure dan HttpOnly untuk melindungi dari ancaman keamanan seperti serangan XSS dan CSRF. Pengembang tetap harus mengonfigurasi *cookie* dengan benar.

## **Penjelasan Implementasi Langkah demi Langkah**

### **Langkah 1: Membuat Fungsi dan Form Registrasi**

1. Aktifkan *virtual environment*.  
2. Buka views.py dan tambahkan import UserCreationForm dan messages.

```

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

```

3.   
   Tambahkan fungsi register ke dalam views.py.

```

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

```

4.   
   Buat berkas register.html di main/templates.

```

{% extends 'base.html' %}
{% block meta %}
<title>Register</title>
{% endblock meta %}
{% block content %}
<div style="padding: 20px; border: 1px solid #ccc; border-radius: 8px; max-width: 400px; margin: 20px auto; text-align: center;">
  <h1 style="color: blue;">Register</h1>
  <form method="POST">
    {% csrf_token %}
    <table style="margin: 0 auto;">
      {{ form.as_table }}
      <tr>
        <td></td>
        <td>
          <input type="submit" name="submit" value="Daftar" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;" />
        </td>
      </tr>
    </table>
  </form>
  {% if messages %}
  <ul style="list-style-type: none; padding: 0;">
    {% for message in messages %}
    <li style="color: green; font-weight: bold; margin-top: 10px;">{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>
{% endblock content %}

```

5.   
   Buka urls.py di main dan tambahkan *path* untuk register.

```

from main.views import register
urlpatterns = [
    ...,
    path('register/', register, name='register'),
]

```

### **Langkah 2: Membuat Fungsi Login**

1. Buka kembali views.py dan tambahkan *import* authenticate, login, dan AuthenticationForm.

```

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

```

2.   
   Tambahkan fungsi login\_user ke dalam views.py.

```

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Anda berhasil login!')
            return redirect('main:show_main')
        else:
            messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

```

3.   
   Buat berkas login.html di main/templates.

```

{% extends 'base.html' %}
{% block meta %}
<title>Login</title>
{% endblock meta %}
{% block content %}
<div class="login" style="padding: 20px; border: 1px solid #ccc; border-radius: 8px; max-width: 400px; margin: 20px auto; text-align: center;">
  <h1 style="color: blue;">Login</h1>
  <form method="POST" action="">
    {% csrf_token %}
    <table style="margin: 0 auto;">
      {{ form.as_table }}
      <tr>
        <td></td>
        <td>
          <input class="btn login_btn" type="submit" value="Login" style="background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;" />
        </td>
      </tr>
    </table>
  </form>
  {% if messages %}
  <ul style="list-style-type: none; padding: 0;">
    {% for message in messages %}
    <li style="color: red; font-weight: bold; margin-top: 10px;">{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
  <p style="margin-top: 15px;">Belum punya akun? <a href="{% url 'main:register' %}" style="color: #008CBA; text-decoration: none;">Daftar Sekarang</a></p>
</div>
{% endblock content %}

```

4.   
   Buka urls.py di main dan tambahkan *path* untuk login.

```

from main.views import login_user
urlpatterns = [
    ...,
    path('login/', login_user, name='login'),
]

```

5. Tambahkan *path url* ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

```

urlpatterns = [
  ...  path('login/', login_user, name='login'),]
```

Kita sudah menambahkan form *login* akun dan membuat mekanisme login. Selanjutnya, kita akan membuat mekanisme *logout* dan menambahkan tombol *logout* pada halaman *main*.

## **Tutorial: Membuat Fungsi Logout**

1. Buka kembali views.py yang ada pada subdirektori main. Tambahkan *import* logout ini pada bagian paling atas, bersama dengan authenticate dan login.

```

from django.contrib.auth import authenticate, login, logout
```

2.   
   Tambahkan fungsi di bawah ini ke dalam fungsi views.py. Fungsi ini berfungsi untuk melakukan mekanisme *logout*.

```

def logout_user(request):
   logout(request)    return redirect('main:login')
```

**Penjelasan Kode:**

* logout(request) digunakan untuk menghapus sesi pengguna yang saat ini masuk.  
  * return redirect('main:login') mengarahkan pengguna ke halaman login dalam aplikasi Django.  
3. Bukalah berkas main.html yang ada pada direktori main/templates dan tambahkan potongan kode di bawah ini setelah *hyperlink tag* untuk *Add News*.

```

...
<a href="{% url 'main:logout' %}">  <button>Logout</button></a>...
```

**Penjelasan Kode:**

* {% url 'main:logout' %} digunakan untuk mengarah ke URL secara dinamis berdasarkan app\_name dan name yang sudah didefinisikan di urls.py. Secara umum, penulisannya adalah dengan {% url 'app\_name:view\_name' %}:  
  * app\_name merupakan nama *app* yang didefinisikan di dalam berkas urls.py. Jika *app* menggunakan atribut app\_name di urls.py, maka ini akan dipakai untuk merujuk pada *app* tersebut. Jika app\_name tidak didefinisikan maka nama *app* yang digunakan adalah nama dari folder *app* yang dibuat.  
    * view\_name merupakan nama dari URL yang diinginkan, didefinisikan melalui parameter name dalam path() di urls.py.  
4. Buka urls.py yang ada pada subdirektori main dan *import* fungsi yang sudah kamu buat sebelumnya.

```

from main.views import logout_user
```

5.   
   Tambahkan *path url* ke dalam urlpatterns untuk mengakses fungsi yang sudah di-*import* sebelumnya.

```

urlpatterns = [
  ...   path('logout/', logout_user, name='logout'),]
```

Kita sudah membuat mekanisme logout dan menyelesaikan sistem autentikasi dalam proyek ini.

## **Tutorial: Merestriksi Akses Halaman Main dan Product Detail**

**Info**

Merestriksi akses halaman tersebut berarti membatasi siapa saja yang boleh membuka halaman tersebut, misalnya hanya pengguna yang sudah login atau admin.

1. Buka kembali views.py di subdirektori main. Tambahkan import login\_required pada bagian paling atas.

```

from django.contrib.auth.decorators import login_required
```

**Penjelasan Kode:**

* Baris kode ini melakukan import decorator login\_required dari sistem autentikasi milik Django.  
  * Decorators dapat kita gunakan untuk menambahkan fungsionalitas ke suatu fungsi tanpa mengubah isi kode fungsi tersebut.  
    * Penjelasan lebih lanjut tentang decorators dapat dibaca [di sini](https://www.geeksforgeeks.org/python/decorators-in-python/).  
2. Tambahkan potongan kode @login\_required(login\_url='/login') di atas fungsi show\_main dan show\_news untuk mengimplementasikan decorator yang baru saja kita import.

```

...
@login_required(login_url='/login')def show_main(request):...@login_required(login_url='/login')def show_product(request):...
```

**Penjelasan Kode:**

* Baris kode tersebut mengaplikasikan decorator login\_required untuk fungsi show\_main dan show\_news, sehingga halaman utama dan news detail hanya dapat diakses oleh pengguna yang sudah *login* (terautentikasi).  
  * Penjelasan lebih lanjut tentang login\_required dapat dibaca [di dokumentasi Django](https://docs.djangoproject.com/en/5.2/topics/auth/default/#the-login-required-decorator).

Setelah menambahkan pembatasan akses halaman tersebut, jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/ di *web browser* pilihanmu. Seharusnya halaman yang muncul bukanlah halaman *main*, namun halaman *login* apabila pengguna sedang dalam keadaan *logout*.

## **Tutorial: Menggunakan Data Dari *Cookies***

1. Lakukan *logout* terlebih dahulu apabila kamu sedang menjalankan aplikasi Django.  
2. Buka kembali views.py di subdirektori main. Tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas.

```

import datetime
from django.http import HttpResponseRedirectfrom django.urls import reverse
```

3.   
   Ubah bagian kode di fungsi login\_user untuk menyimpan *cookie* baru bernama last\_login yang berisi *timestamp* terakhir kali pengguna melakukan *login*. Kita dapat memperoleh ini dengan mengganti kode yang ada pada blok if form.is\_valid() menjadi seperti berikut.

```

...
if form.is_valid():    user = form.get_user()    login(request, user)    response = HttpResponseRedirect(reverse("main:show_main"))    response.set_cookie('last_login', str(datetime.datetime.now()))    return response...
```

**Peringatan**

Perhatikan indentasi kode kamu yang telah dimodifkasi\!

**Penjelasan Kode:**

* login(request, user) berfungsi untuk melakukan *login* menggunakan sistem autentikasi Django.  
  * response \= HttpResponseRedirect(reverse("main:show\_main")) akan menetapkan *redirect* ke halaman *main* setelah response diterima.  
  * response.set\_cookie('last\_login', str(datetime.datetime.now())) berfungsi untuk mendaftarkan *cookie* last\_login di response dengan isi *timestamp* terkini.  
4. Pada fungsi show\_main, tambahkan potongan kode 'last\_login': request.COOKIES\['last\_login'\] ke dalam variabel context. Berikut contoh kode yang sudah diubah.

```

context = {
   'npm' : '2406395291',    'name': 'Josh Christmas Rommlynn',    'class': 'PBP A',    'news_list': news_list,    'last_login': request.COOKIES.get('last_login', 'Never')}
```

**Penjelasan Kode:**

* Kita mengakses *cookie* yang terdaftar di request dengan request.COOKIES.get('last\_login', 'Never').  
  * Method .get() digunakan untuk mengambil nilai cookie dengan aman \- jika cookie last\_login tidak ada atau sudah dihapus, akan mengembalikan nilai default Never.  
  * Waktu terakhir pengguna *login* sekarang dapat ditampilkan di halaman *web* dengan mengakses *key* last\_login.  
5. Ubah fungsi logout\_user untuk menghapus *cookie* last\_login setelah melakukan *logout*.

```

def logout_user(request):
   logout(request)    response = HttpResponseRedirect(reverse('main:login'))    response.delete_cookie('last_login')    return response
```

**Penjelasan Kode:**

* response.delete\_cookie('last\_login') berfungsi untuk menghapus *cookie* last\_login dari daftar *cookies* di response.  
6. Buka berkas main.html di direktori main/templates dan tambahkan potongan kode berikut di setelah tombol *logout* untuk menampilkan data waktu terakhir pengguna *login*.

```

...
<h5>Sesi terakhir login: {{ last_login }}</h5>...
```

7.   
   Silakan *refresh* halaman *login* (atau jalankan proyek Django-mu dengan perintah python manage.py runserver jika proyek Django belum dijalankan) dan cobalah untuk *login*. Data last\_login kamu akan muncul di halaman main.  
8. Jika kamu menggunakan *browser* Chromium seperti Google Chrome atau Microsoft Edge, kamu dapat melihat data *cookie* last\_login dengan mengakses panel Developer Tools (Ctrl \+ Shift \+ I atau Cmd \+ Option \+ I) dan membuka tab Application.  
   * Klik bagian Cookies di grup Storage dan kamu dapat melihat data *cookies* yang tersedia. Selain last\_login, kamu juga dapat melihat data sessionid dan csrftoken. Berikut contoh tampilannya.

![][image1]

9. Jika kamu melakukan *logout* dan membuka bagian riwayat *cookie*, *cookie* last\_login yang dibuat sebelumnya akan hilang dan dibuat ulang ketika kamu *login* kembali.

**Info**

Sebelum melanjutkan ke tutorial berikutnya, cobalah untuk **membuat setidaknya satu akun** di proyek Django.

## **Tutorial: Menghubungkan Model Product dengan User**

Terakhir, kita akan menghubungkan setiap objek News dengan pengguna yang membuatnya. Dengan begitu, setiap pengguna yang sedang login hanya dapat melihat *news* yang ia buat sendiri.

Untuk melakukan hal tersebut, ikuti langkah-langkah berikut:

1. Buka file models.py pada subdirektori main, kemudian tambahkan baris berikut di bagian import (bersama dengan import lain yang sudah ada):

```

...
from django.contrib.auth.models import User...
```

2.   
   Pada model News yang sudah dibuat, tambahkan potongan kode berikut:

```

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini...
```

**Penjelasan Kode:**

* Potongan kode di atas berfungsi untuk menghubungkan satu *news* dengan satu user melalui sebuah relationship  
* Setiap *news* dapat terasosiasi dengan seorang user (many-to-one relationship)  
* null=True memungkinkan news yang sudah ada sebelumnya tetap valid tanpa harus memiliki user  
* on\_delete=models.CASCADE berarti jika user dihapus, semua news milik user tersebut juga akan ikut terhapus  
3. Buat file migrasi model dengan python manage.py makemigrations. Selanjutnya jalankan migrasi model dengan python manage.py migrate.  
4. Buka kembali views.py yang ada pada subdirektori main, dan ubah potongan kode pada fungsi create\_news menjadi sebagai berikut:  
   

```

def create_news(request):
   form = NewsForm(request.POST or None)

   if form.is_valid() and request.method == 'POST':
       news_entry = form.save(commit = False)
       news_entry.user = request.user
       news_entry.save()
       return redirect('main:show_main')

   context = {
       'form': form
   }

   return render(request, "create_news.html", context)
```

**Penjelasan Kode:**

* Parameter commit=False pada potongan kode di atas digunakan agar Django tidak langsung menyimpan objek hasil form ke database. Dengan begitu, kita memiliki kesempatan untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan.  
* Pada kasus ini, kita memanfaatkan kesempatan tersebut untuk mengisi field user dengan nilai request.user, yaitu pengguna yang sedang login. Dengan cara ini, setiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.  
    
5. Modifikasi fungsi show\_main sehingga bentuk akhirnya menjadi seperti berikut:

```

...
@login_required(login_url='/login')
def show_main(request):
filter_type = request.GET.get("filter", "all")  # default 'all'

if filter_type == "all":
   news_list = News.objects.all()
else:
   news_list = News.objects.filter(user=request.user)

context = {
   'npm': '2406395291',
   'name': request.user.username,
   'class': 'PBP A',
   'news_list': news_list,
   'last_login': request.COOKIES.get('last_login', 'Never')
}
return render(request, "main.html",context)
...

```

**Penjelasan Kode:**

* Fungsi show\_main menampilkan halaman utama setelah user login dan dilengkapi dengan **filter artikel** berdasarkan penulis. Filter ini diambil dari query parameter filter pada URL, dengan dua opsi: "my" untuk menampilkan hanya artikel yang ditulis oleh user yang sedang login, dan "all" untuk menampilkan semua artikel.  
* Selain itu, informasi user seperti name diambil langsung dari **username** user yang sedang login.  
6. Tambahkan tombol filter My dan All pada halaman main.html

```

{% extends 'base.html' %}
{% block content %}
<h1>SaccerBall</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>


<a href="{% url 'main:create_product' %}">
 <button>+ Add Product</button>
</a>
<a href="{% url 'main:logout' %}">
 <button>Logout</button>
</a>
<h5>Sesi terakhir login: {{ last_login }}</h5>
<hr>
<!-- Tambahkan kode ini -->
<a href="?filter=all">
   <button type="button">All Products</button>
</a>
<a href="?filter=my">
   <button type="button">My Products</button>
</a>
...
```

![][image2]

7. Kemudian tampilkan nama author di news\_detail.html

```

{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to News List</button></a></p>

<h1>{{ news.title }}</h1>
<p><b>{{ news.get_category_display }}</b>{% if news.is_featured %} |
   <b>Featured</b>{% endif %}{% if news.is_news_hot %} |
   <b>Hot</b>{% endif %} | <i>{{ news.created_at|date:"d M Y, H:i" }}</i>
   | Views: {{ news.news_views }}</p>

{% if news.thumbnail %}
<img src="{{ news.thumbnail }}" alt="News thumbnail" width="300">
<br /><br />
{% endif %}

<p>{{ news.content }}</p>

<!-- Tambahkan kode ini -->
{% if news.user %}
   <p>Author: {{ news.user.username }}</p>
{% else %}
   <p>Author: Anonymous</p>
{% endif %}

{% endblock content %}
```

   ![][image3]

   Informasi author merefleksikan pembuat artikel, bukan user yang sedang login. Silakan coba menggunakan dua akun berbeda untuk memastikan.

   

8. Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah [http://localhost:8000/](http://localhost:8000/) di browser favoritmu untuk melihat hasilnya. Cobalah untuk membuat akun baru dan login dengan akun yang baru dibuat. Amatilah halaman utama, news yang tadi telah dibuat dengan akun sebelumnya tidak akan ditampilkan di halaman pengguna akun yang baru saja kamu buat. Hal tersebut berarti kamu sudah berhasil menghubungkan objek News dengan User yang membuatnya.

## **Tutorial: Pengenalan Selenium (OPSIONAL)**

Selenium adalah sebuah alat gratis yang digunakan untuk mengotomatisasi web browser. Dengan Selenium, kita bisa menulis program yang mampu **mengendalikan browser seolah-olah sedang digunakan manusia**, misalnya untuk mengklik tombol, mengisi formulir, berpindah halaman, hingga mengambil data dari sebuah website. Kelebihan Selenium adalah dapat digunakan di berbagai browser besar seperti Chrome, Firefox, Edge, dan Safari tanpa harus banyak mengubah kode, karena mengikuti standar resmi W3C WebDriver.

### **Apa itu webdriver?**

WebDriver adalah komponen utama di Selenium yang berfungsi sebagai “**jembatan**” antara kode program yang kita tulis dengan browser yang kita kendalikan. Dengan kata lain, WebDriver memungkinkan kode berkomunikasi dengan browser sehingga proses otomatisasi dapat berjalan secara nyata.

### **Contoh Penggunaan Selenium WebDriver**

Kode berikut adalah cara sederhana menggunakan **Selenium WebDriver** untuk membuka browser Edge, mengunjungi sebuah halaman, lalu menutup browser.

```

from selenium import webdriver

# Membuat instance WebDriver untuk Chrome
driver = webdriver.Edge()

# Membuka halaman web selenium.dev
driver.get("http://selenium.dev")

# Menutup browser setelah selesai
driver.quit()
```

Berbeda dengan unit test yang menguji fungsi secara individual, Selenium digunakan untuk **functional testing** \- yaitu menguji aplikasi web seperti yang dilakukan pengguna sebenarnya.

Selenium dapat melakukan:

* Membuka halaman web  
* Mengklik tombol atau link  
* Mengisi form kemudian submit  
* Berpindah antar halaman  
* Memverifikasi tampilan yang muncul

Dengan demikian, kita dapat menguji **keseluruhan alur aplikasi** dari awal hingga akhir. Frontend, backend, dan database dapat diuji secara bersamaan, bukan hanya satu komponen saja.

### **Membuat Functional Test di Django**

1. Tambahkan selenium ke requirements.txt. Selanjutnya jalankan pip install \-r requirements.txt.  
2. Buka tests.py di direktori main dan tambahkan import sebagai berikut:

```
from django.test import TestCase, Client
from .models import Product
from django.test import TestCase, Client
from .models import Product
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

```

3. Selanjutnya buat kelas test FootballShopFunctionalTest sebagai berikut setelah blok kode MainTest:  
   

```

class FootballShopFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create single browser instance for all tests
        cls.browser = webdriver.Edge()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Close browser after all tests complete
        cls.browser.quit()

    def setUp(self):
        # Create user for testing
        self.test_user = User.objects.create_user(
            username='testadmin',
            password='testpassword'
        )

    def tearDown(self):
        # Clean up browser state between tests
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        # Navigate to blank page to reset state
        self.browser.get("about:blank")

    def login_user(self):
        """Helper method to login user"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        # Test login functionality
        self.login_user()

        # Check if login is successful
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "SaccerBall")

        logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        # Test register functionality
        self.browser.get(f"{self.live_server_url}/register/")

        # Check if register page opens
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        # Fill register form
        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        # Check redirect to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(login_h1.text, "Login")

    def test_create_news(self):
        # Test create news functionality (requires login)
        self.login_user()

        # Go to create news page
        add_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Add Product")
        add_button.click()

        # Fill form
        name_input = self.browser.find_element(By.NAME, "name")
        description_input = self.browser.find_element(By.NAME, "description")
        category_select = self.browser.find_element(By.NAME, "category")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")
        brand_input = self.browser.find_element(By.NAME, "brand")
        is_featured_checkbox = self.browser.find_element(By.NAME, "is_featured")

        name_input.send_keys("Test Product Name")
        description_input.send_keys("Test product description for selenium testing")
        thumbnail_input.send_keys("https://example.com/image.jpg")
        brand_input.send_keys("Test")

        # Set category (select 'jersey' from dropdown)

        select = Select(category_select)
        select.select_by_value("jersey")

        # Check is_featured checkbox
        is_featured_checkbox.click()

        # Submit form
        name_input.submit()

        # Check if returned to main page and product appears
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "SaccerBall"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "SaccerBall")

        # Check if product name appears on page
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Test Product Name")))
        product_name = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Test Product Name")
        self.assertTrue(product_name.is_displayed())

    def test_product_detail(self):
        # Test product detail page

        # Login first because of @login_required decorator
        self.login_user()

        # Create news for testing
        product = Product.objects.create(
            name="Detail Test Product",
            description="Description for detail testing",
            brand="Test",
            user=self.test_user
        )

        # Open news detail page
        self.browser.get(f"{self.live_server_url}/news/{product.id}/")

        # Check if detail page opens correctly
        self.assertIn("Detail Test Product", self.browser.page_source)
        self.assertIn("Description for detail testing", self.browser.page_source)

    def test_logout(self):
        # Test logout functionality
        self.login_user()

        # Click logout button - text is inside button, not link
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        # Check if redirected to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        # Test filter functionality on main page
        #        
        # Create news for testing
        Product.objects.create(
            name="My Test Product",
            description="My product description",
            brand="mine",
            user=self.test_user
        )
        Product.objects.create(
            name="Other User Product",
            description="Other product description",
            brand="others",
            user=self.test_user  # Same user for simplicity
        )

        self.login_user()

        # Test filter "All Articles"
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "All Products")))
        all_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "All Products")
        all_button.click()
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other User Product", self.browser.page_source)

        # Test filter "My Articles"  
        my_button = self.browser.find_element(By.PARTIAL_LINK_TEXT, "My Products")
        my_button.click()
        self.assertIn("My Test Product", self.browser.page_source)

```

4. Selanjutnya, jalankan functional test tersebut python manage.py test main.tests.FootballShopFunctionalTest.  
   ![][image4]

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>