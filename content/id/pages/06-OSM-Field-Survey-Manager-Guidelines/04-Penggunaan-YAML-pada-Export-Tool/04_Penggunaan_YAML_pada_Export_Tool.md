﻿---
title: Penggunaan YAML pada Export Tool
weight: 4
---

**Tujuan Pembelajaran:**

*   Mampu memahami konsep YAML
*   Mampu membuat YAML untuk struktur data OSM 
*   Mampu mengoperasikan YAML untuk men-_download_ data OSM pada _Export Tool_

Pada bab sebelumnya, Anda telah mempelajari bagaimana mengenal _tag_ informasi objek di dalam _OpenStreetMap_. Anda juga telah menentukan objek-objek yang akan dikumpulkan pada saat survei lapang. Pada saat proses pengambilan data OSM yang telah di _upload_ ke server menggunakan _Export Tool_, Anda menemukan kendala karena beberapa data atribut yang berasal dari _tag_ info tidak dapat di _download_ melalui _tag_ yang disediakan  _Export Tool_. Oleh karena itu, Anda dapat menggunakan YAML untuk men-_download_ data dengan atribut yang sama seperti atribut yang dimasukkan saat pemetaan.

### **I. Pengertian YAML**

YAML (_YAML Ain't Markup Language)_ adalah sebuah struktur data sederhana yang dapat digunakan pada semua bahasa pemrograman. YAML dapat digunakan untuk membuat struktur data yang disesuaikan dengan _tag_ (_key_ dan _value_) data OSM, yang nantinya dapat berfungsi untuk menyaring data OSM berdasarkan _presets_ yang digunakan saat proses memasukkan data OSM.  

### **II. Pembuatan YAML untuk Filter Data di _Export Tool_**

**a. Struktur Data YAML**
Cara membuat YAML untuk struktur data OSM dapat dibagi menjadi empat bagian, yaitu :

*   Judul _file_ = menunjukkan nama _file_
*   _Types_	    = menunjukkan tipe data pemetaan, terdiri dari _points, lines_, dan _polygons_
*   _Select_	    = menunjukkan _key_ yang berasal dari objek OSM 
*   _Where_ = menunjukkan letak objek pada data OSM, terdiri dari _key_ dan _value_ dari objek tersebut

![struktur yaml](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0401_Struktur_format_YAML.png)
<p align="center"><i>Struktur format YAML untuk data OSM</i><p align="center">

**b. Syarat Format Penulisan Struktur Data YAML**

Ada beberapa syarat yang harus diperhatikan dalam pembuatan struktur data YAML, yaitu :
* Penulisan terdiri dari huruf kecil, tidak boleh kapital
* Nama file/judul file diletakkan di awal dokumen dan tidak boleh ada spasi pada format penulisan judul file. Jika judul lebih dari dua kata, gunakan tanda _ sebagai pemisah kata
* Antar elemen struktur data harus sejajar seperti pada contoh di atas.

**c. Proses Pembuatan YAML**

Anda dapat membuka modul Pembuatan Model Data OSM untuk melihat daftar model data objek OSM yang akan dipetakan. Kemudian dari daftar tabel-tabel tersebut akan dibuat ke dalam struktur data YAML. Langkah-langkah untuk membuat YAML, yaitu:

* Buat daftar objek yang dipetakan yang sudah dibuat sebelumnya pada model data OSM

Tabel Model Data OSM untuk Objek Bank

| *key* | *possible values* |
|---|---|
|*amenity*|bank|
|*building*|bank|
|*amenity*|bank|
|*name*|isian nama|
|*addr:full*|isian alamat|
|*capacity*|<50, 50-100, 100-250, 250-500, >500|
|*building:levels*|isian dalam bentuk angka|
|*building:structure*|*confined_masonry* (Rangka beton bertulang), *steel_frame* (Rangka baja), *wood_frame* (Rangka kayu), *bamboo_frame* (Rangka bambu)|
|*building:walls*|*brick* (Bata), *concrete* (Beton), *wood* (Papan kayu), *bamboo* (Bambu), *glass* (Kaca)|
|*building:floor*|*ground* (Tanah), *wood* (Papan kayu), *cement* (Plester / Semen), *tekhel* (Tegel), *ceramics* (Keramik)|
|*building:roof*|*tile* (Genteng), *tin* (Seng), *asbestos* (Asbes), *concrete* (Beton)|
|*access:roof*|*yes* (Ada), *no* (Tidak ada)|
|*building:condition*|*poor* (Buruk), *good* (Baik)|
|*backup_generator*|*yes* (Ada), *no* (Tidak ada)|

*   Buka **Notepad** yang tersedia pada laptop/komputer Anda.
*   Pada baris pertama ketikkan **nama _file_ yang akan dijadikan judul _file_**, misalnya bank

		  bank:

*   Pada baris kedua **tekan enter + spasi empat kali** dan ketikkan **types:**, kemudian **tekan enter + spasi delapan kali + ketikkan - points/polygons/lines**  dan isi tipe data tersebut berdasarkan model data OSM dengan mengetikkan ke bawah baris 

		 types:
            - points
            - polygons

*   Tekan enter dan sesuaikan dengan baris types:, kemudian ketikkan **select: → tekan enter + spasi delapan kali** ketikkan daftar **key** yang terdapat pada objek “bank”.

		select:
            - amenity
            - name
            - addr:full
            - addr:city
            - capacity:persons
            - building
            - building:levels
            - building:structure
            - building:walls
            - building:floor
            - building:roof
            - access:roof
            - building:condition
            - backup_generator
            - source


*   Tahap terakhir, tekan enter dan sesuaikan dengan posisi types dan select **→ ketikkan where: key dan value**.         

             where: amenity='bank'

*   Anda dapat meneruskan pembuatan YAML sampai seluruh objek pemetaan dimasukkan, yang disamakan dengan format seperti sebelumnya. 
*   Simpan struktur YAML tersebut dalam format _.txt_ di dalam direktori komputer/laptop Anda.

		   bank:
            types:
                - points
                - polygons
            select:
                - amenity
                - name
                - addr:full
                - addr:city
                - capacity:persons
                - building
                - building:levels
                - building:structure
                - building:walls
                - building:floor
                - building:roof
                - access:roof
                - building:condition
                - backup_generator
                - source
                                                                                                                                                                                                                                                             
### **III. Penggunaan YAML pada _Export Tool_**

*   Buka halaman situs Anda, dan ketikkan link berikut ini https://export.hotosm.org

![halaman depan export tool](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0402_Halaman_Situs_Export.png)
<p align="center"><i>Halaman muka situs Export Tool</i><p align="center">

*   Anda harus masuk menggunakan akun OSM dengan klik **_Login_** di sudut kanan atas. Apabila muncul _‘Authorize access to your account’_ klik **_Grant Access_**. Periksa alamat email Anda untuk mengkonfirmasi pembuatan akun pada email yang masih aktif. Klik tautan pada email tersebut untuk konfirmasi pembuatan akun.

![izin akses akun](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0403_Izin_akses_akun_OSM.png)
<p align="center"><i>Izin akses akun OSM</i><p align="center">


*   Sekarang Anda sudah masuk dengan menggunakan akun OSM, kemudian klik **_Start Exporting_** untuk memulai proses _download_ data OSM
*   Pada **_Menu Describe_** akan muncul formulir isian dan gambar peta seperti gambar di bawah ini, formulir isian yang wajib diisi dan Anda dapat memilih area yang diinginkan pada gambar peta di sebelah kanan. 

![lembar kerja export tool](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0404_Lembar_kerja_Export_Tool.png)
<p align="center"><i>Lembar kerja Export Tool</i><p align="center">


*   Ada beberapa cara untuk menggambarkan area yang akan dipilih :

  **_Box_** = Menggambar area dengan menggunakan kotak. Jika Anda ingin mengulang untuk pembuatan kotak klik tanda X pada kolom _Box_. 

![penentuan area](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0405_Penentuan_area_box.png)
<p align="center"><i>Penentuan area dengan bentuk kotak</i><p align="center">

  **_Draw_** = Menggambar area yang dipilih secara manual, Anda dapat klik pada area yang ingin digambar dan diakhiri dengan klik dua kali.

![penentuan area manual](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0406_Penentuan_area_dengan_bentuk_manual.png)
<p align="center"><i>Penentuan area dengan bentuk manual</i><p align="center">

  **_Import_** = Menggunakan poligon dalam format _.geojson_ untuk memilih area yang akan di _download_. Syarat format data _.geojson_ yang dapat ditambahkan ke dalam _Export Tool_ adalah harus satu fitur (satu baris) pada data atribut. Anda dapat membuka modul **Menggunakan GeoJSON** untuk mengetahui cara mendapatkan data _.geojson._

![penentuan area batas admin](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0407_Penentuan_area_dengan_import.png)
<p align="center"><i>Penentuan area dengan berdasarkan batas administrasi</i><p align="center">
 
*   Jika sudah menyelesaikan formulir isian dan menentukan area yang akan di _download_, pilih menu **_Format_**. Pilih data spasial yang Anda inginkan, misalnya _.shapefile_

![format data spasial](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0408_Format_data_spasial.png)
<p align="center"><i>Format data spasial</i><p align="center">

*   Selanjutnya klik Menu **Data → YAML**. Salin struktur data YAML yang telah dibuat, tempelkan/_paste_ ke kotak YAML

![menu yaml](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0409_Menu_YAML.png)
<p align="center"><i>Menu YAML</i><p align="center">

*   Klik Menu **_Summary_**, Anda harus memilih apakah _file_ ekspor ini akan dipublikasikan kepada umum atau hanya ada pada akun Anda. Kemudian klik **_Create Export_** untuk memulai proses ekspor data OSM.

![menu summary](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0410_Menu_summary.png)
<p align="center"><i>Menu summary</i><p align="center">

*   Tunggu beberapa saat sampai proses selesai. Jika _file export_ Anda sudah selesai, _Export Tool_ akan memberikan pemberitahuan melalui _email_, atau Anda dapat melihat hasilnya di Menu **_Export._** Jika Anda ingin melihat hasil _export_ yang dilakukan oleh pengguna lainnya, maka beri tanda centang **_Show all Export_**. 

![menu export](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0411_Menu_export.png)
<p align="center"><i>Menu Export</i><p align="center">

*   Jika proses sudah selesai akan muncul kotak dialog seperti di bawah ini dengan status **_COMPLETED_**, klik tulisan berwarna biru seperti **nama file.shp.zip** untuk menyimpan hasil ekspor data OSM.

![proses export selesai](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0412_Done.png)
<p align="center"><i>Proses export tool telah selesai</i><p align="center">


**Latihan!**

Buatlah 2 (dua) proyek baru di _Export Tool_ dan _download_ data OSM dengan menggunakan tautan YAML berikut [https://tinyurl.com/group-stats](https://tinyurl.com/group-stats). Data OSM tersebut akan digunakan pada bab selanjutnya mengenai perhitungan jumlah objek menggunakan _plugin Group Stats_. Jika Anda telah berhasil, maka akan ada 2 (dua) _shapefile_ yaitu fasum dan jalan.

**RINGKASAN**

Anda telah menyelesaikan proses men-_download_ data spasial dengan menggunakan _Export Tool_. Dengan menggunakan YAML, data yang dihasilkan akan sesuai dengan data yang dimasukkan pada proyek pemetaan. Sehingga _file_ tersebut sudah tertata rapi dan teratur, Anda dapat membuka _file_ tersebut, untuk melihat data-data yang sudah dihasilkan dari pemetaan. _File_ yang sudah di-_download_ dapat dibuka di _software_ pemetaan seperti QGIS.
