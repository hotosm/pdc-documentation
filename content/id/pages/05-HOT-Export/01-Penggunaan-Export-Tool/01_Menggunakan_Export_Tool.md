---
title: Download Data OSM dengan Menggunakan Export Tool
weight: 1
---

**Tujuan Pembelajaran**

*   Memahami pengertian _Export Tool_
*   Mempraktikkan cara mendapatkan data OSM dengan _Export Tool_

Setelah Anda belajar bagaimana menambahkan dan mengedit data pada _OpenStreetMap_ (OSM), sekarang Anda akan mempelajari tentang bagaimana cara mendapatkan data _OpenStreetMap_ yang telah di-_upload_ ke server OSM. Data tersebut dapat digunakan untuk analisis data, kustomisasi simbologi data, membuat peta, dan lainnya sesuai kebutuhan Anda. 

### **I. Pengertian _Export Tool_**

_Export tool_ adalah sebuah layanan terbuka yang digunakan untuk men-_download_ data OSM terbaru yang memberikan kebebasan bagi pengguna untuk memilih data yang akan mereka _download_ di area tertentu. _Export tool_ juga menyediakan pilihan format data spasial, seperti ESRI shapefiles (_.shapefile_), google KML (_.kml_), GeoPackage (_.gpkg_) dan MBTiles (_.mbtiles_). Anda dapat memilih wilayah yang diinginkan dan kategori data yang akan di-_download_ dengan menggunakan _Export Tool._ Cara men-_download_ data pada situs ini sangat mudah dan tidak ada persyaratan, hanya Anda diwajibkan untuk mendaftar dengan menggunakan akun _OpenStreetMap_ Anda dan mencantumkan sumber data untuk lisensi kredit pada produk yang Anda buat seperti **© OpenStreetMap contributors.**

### **II. Cara Menggunakan _Export Tool_**

*   Buka halaman situs Anda, dan ketikkan link berikut ini https://export.hotosm.org

![halaman export tool](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0101_tampilanexporttool.png)
<p align="center"><i>Halaman muka Export Tool</i><p align="center">

*   Anda harus masuk menggunakan akun OSM dengan klik **_Login_** di sudut kanan atas. Apabila muncul _‘Authorize access to your account’_ klik **_Grant Access_**. Jika belum memiliki akun OSM, Anda dapat membuka pada modul **Memulai Menggunakan OSM**.
*   Sekarang Anda sudah berhasil masuk dengan menggunakan akun OSM, kemudian klik **_Start Exporting_** untuk memulai proses _download_ data OSM.
*   Akan muncul formulir isian dan peta seperti gambar di bawah ini, formulir isian harus  diisi dan Anda dapat memilih area yang diinginkan pada peta di sebelah kanan. 

![lembar kerja export](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0102_lembarkerjaet.png)
<p align="center"><i>Lembar kerja Export Tool</i><p align="center">

*   Ada beberapa cara untuk menggambarkan area yang akan dipilih

  **_Box_** = Menggambar area dengan menggunakan kotak. Jika Anda ingin mengulang untuk pembuatan kotak klik tanda X pada kolom _Box_. 

![penentuan area](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0103_Penentuan_Area_dengan_Kotak.png)
<p align="center"><i>Penentuan area dengan kotak</i><p align="center">


  **_Draw_** = Menggambar area yang dipilih secara manual

![penentuan area manual](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0104_penentuan_manual.png)
<p align="center"><i>Penentuan Area dengan Bentuk Manual</i><p align="center">


  **_Import_** = Menggunakan poligon dalam format *.geojson* untuk memilih area yang akan di-_download_. Cara mendapatkan _file_ _.geojson_ dapat Anda lihat pada modul **Menggunakan GeoJSON**.

![penentuan area](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0105_penentuangeojson.png)
<p align="center"><i>Penentuan area dengan berdasarkan admin</i><p align="center">
  
*   Jika sudah menyelesaikan formulir isian dan menentukan area yang akan di _download_, pilih menu **_Format_**. Pilih data spasial yang Anda inginkan, misalnya _shapefile_

![format data spasial](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0106_menuformat.png)
<p align="center"><i>Format data spasial</i><p align="center">

*   Selanjutnya klik Menu **Data**, pada bagian ini halaman yang akan muncul akan menyesuaikan pemilihan tipe data spasial yang Anda pilih sebelumnya pada **_Menu Format_**. Pada bagian **_Tag Tree_**, menunjukkan informasi objek yang sesuai dengan presets OSM secara global. Anda harus memberikan tanda centang untuk data OSM yang akan di-_download_ sesuai dengan kebutuhan data yang diinginkan. Sebagai contoh, jika kita akan men-_download_ data bangunan dan jalan, berikan tanda centang pada **_Buildings dan Transportation > Roads_**

![pilihan objek di expor tool](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0107_buildingandroads.png)
<p align="center"><i>Pilihan Objek di Export Tool</i><p align="center">

*   Klik Menu **_Summary_**, Anda harus memilih apakah _file_ ekspor ini akan dipublikasikan kepada umum atau hanya ada pada akun Anda. Kemudian klik **_Create Export_** untuk memulai proses _export_ data OSM.

![menu summary](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0108_menusummary.png)
<p align="center"><i>Menu Summary</i><p align="center">

*   Tunggu beberapa saat sampai proses selesai. Jika _file export_ Anda telah selesai, _Export Tool_ akan memberikan pemberitahuan melalui email, atau Anda dapat melihat hasilnya di Menu **_Exports_**

![menu export](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0109_menuexporttool.png)
<p align="center"><i>Menu Exports</i><p align="center">

*   Jika proses sudah selesai akan muncul kotak dialog seperti di bawah ini, klik **nama file.shp.zip** untuk menyimpan hasil ekspor data OSM di direktori laptop/komputer Anda.

![proses export tool selesai](/id/images/05-HOT-Export/01-Penggunaan-Export-Tool/0110_selesaiexport.png)
<p align="center"><i>Proses Export Tool Selesai</i><p align="center">


**RINGKASAN**

Anda telah mengetahui bagaimana cara men-_download_ data OSM dengan menggunakan _Export Tool_. Data yang telah Anda _download_ dapat diolah dengan perangkat lunak sistem informasi geografis yang salah satu contohnya perangkat lunak yang _Open Source_ yaitu QGIS ([www.qgis.org](http://www.qgis.org)). Anda dapat memanfaatkan data tersebut untuk perhitungan kuantitas data OSM hasil dari pemetaan untuk membuat analisis data OSM.
