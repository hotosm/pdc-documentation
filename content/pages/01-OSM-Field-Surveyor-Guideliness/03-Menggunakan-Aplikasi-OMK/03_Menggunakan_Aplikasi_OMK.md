---
title: Menggunakan Aplikasi OpenMapKit
weight: 3
---

**Tujuan Pembelajaran:**



*   Mampu menjelaskan _OpenMapkit_ sebagai salah satu alat mengambil data infrastruktur
*   Mampu mengoperasikan cara pengaturan awal untuk aplikasi _OpenMapKit_
*   Mampu mengoperasikan cara memasukkan _offline basemap_ untuk _OpenMapKit_
*   Mampu menerapkan cara penggunaan _OpenMapKit_

Sebelumnya Anda sudah mempelajari aplikasi _ODK (OpenDataKit) Collect_, sebuah aplikasi berbasis android pengganti formulir kertas untuk survei. _ODK Collect_ memiliki ekstensi tambahan yang dinamakan _OpenMapKit (OMK)_. Ekstensi tambahan ini digunakan untuk menambahkan informasi posisi atau letak objek yang disurvei.

### **I. Apa itu _OpenMapKit_**

_OpenMapKit (OMK)_ adalah sebuah aplikasi tambahan yang digunakan untuk melengkapi aplikasi _ODK Collect_ dalam menentukan posisi objek yang ditemukan saat survei lapangan secara tepat dan presisi. _OpenMapKit_ dapat dijalankan melalui aplikasi _ODK Collect_, setelah Anda membuka dan memilih salah satu formulir yang tersedia. Dalam menentukan lokasi objek, aplikasi _OpenMapKit_ membutuhkan latar belakang peta berupa citra satelit atau peta OSM. Jika Anda menggunakan peta OSM, maka hal yang harus diperhatikan adalah data tersebut harus tersedia di dalam server OSM. Saat ini _OpenMapKit_ hanya tersedia di _smartphone_ android. Anda dapat men-_download_ _OpenMapKit_ secara gratis melalui _Play Store_.

<p align="center">
<img width=50% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0301_app_omk.png" alt="Aplikasi OpenMapKit di Play Store" title="Aplikasi OpenMapKit di Play Store">
</p>

<p align="center"><i>Aplikasi OpenMapKit di Play Store</i></p>

> Catatan :
Untuk dapat menggunakan _OpenMapKit_ Anda harus menginstal juga _ODK (OpenDataKit) Collect_ versi terbaru, karena formulir yang diisi di dalam _OpenMapKit_ bersumber dari _ODK Collect_.

### **II. Pengaturan awal _OpenMapKit_**

Sebelum _OpenMapKit_ digunakan, pertama-tama Anda harus melakukan pengaturan awal terlebih dahulu. Berikut ini adalah langkah-langkah pengaturan awal _OpenMapKit_:

*   Pada halaman awal _OpenMapKit_, tekan **tombol pengaturan** yang terletak di pojok kanan atas.
*   Pilih **OSM _User Name_** lalu masukkan OSM _User Name_ Anda

<p align="center">
<img width=50% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0302_setting_omk.png" alt="Tampilan menu pengaturan OpenMapKit" title="Tampilan menu pengaturan OpenMapKit">
</p>

<p align="center"><i>Tampilan menu pengaturan OpenMapKit</i></p>

*   Untuk _basemap_ atau peta dasar yang menjadi latar belakang, _OpenMapKit_ secara _default_ akan menampilkan _Online Humanitarian OpenStreetMap_.

### **III. Memasukkan _offline basemap_ untuk _OpenMapKit_**

_OpenMapKit_ menyediakan peta OSM sebagai _basemap_ yang harus diakses menggunakan koneksi internet. Namun jangan khawatir, Anda juga dapat memasukkan _offline basemap_ ke dalam _OpenMapKit_ yang merupakan peta dasar yang dapat dibuka tanpa koneksi internet. _Offline basemap_ dapat memudahkan Anda dalam menambahkan informasi tepat di lokasi yang Anda survei. Berikut ini adalah cara menambahkan _offline basemap_:

*   Format data yang digunakan sebagai _offline basemap_ dalam aplikasi _OpenMapKit_ harus berformat _.mbtiles_. Cara pembuatan _.mbtiles_ dapat dilihat pada modul **Membuat Mbtiles untuk OMK (OpenMapKit)**. Setelah Anda memiliki _file .mbtiles_, sambungkan _smartphone_ Anda ke komputer/laptop. Buka folder yang berisi _file .mbtiles_ yang akan dimasukkan. Pilih _file .mbtiles_ nya kemudian salin ke folder **openmapkit →** **mbtiles** yang ada di internal _storage smartphone_ Anda.

<p align="center">
<img width=70% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0303_omk_mbtiles.png" alt="Proses menambahkan file .mbtiles ke dalam OpenMapKit" title="Proses menambahkan file .mbtiles ke dalam OpenMapKit">
</p>

<p align="center"><i>Proses menambahkan file .mbtiles ke dalam OpenMapKit</i></p>

*   Jika sudah berhasil memasukkan _.mbtiles_, Anda dapat mengubah _basemap OpenMapKit_ dengan cara tekan **tombol pengaturan** yang terletak di pojok kanan atas dan tekan **_Basemap_** kemudian pilih _.mbtiles_ yang baru saja Anda masukkan. Lalu tekan **_OK_**.

<p align="center">
<img width=80% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0304_omk_basemap.png" alt="Tampilan pengaturan basemap di OpenMapKit" title="Tampilan pengaturan basemap di OpenMapKit">
</p>

<p align="center"><i>Tampilan pengaturan basemap di OpenMapKit</i></p>

### **IV. Pengoperasian Dasar _OpenMapKit_**


**a. Men-_download_ Data OSM di _OpenMapKit_**

Data OSM yang sudah ada dapat memudahkan Anda untuk menambahkan informasi bangunan karena Anda dapat memilih langsung bangunan yang akan Anda tambahkan informasinya. Oleh karena itu, sebaiknya Anda men-_download_ data OSM terlebih dahulu sebelum menambahkan informasi. Langkah-langkah untuk men-_download_ data OSM di dalam aplikasi _OpenMapKit_, yaitu:

*   Arahkan peta ke lokasi Anda berada saat ini (misalnya Anda sudah berada di lokasi survei) dengan cara tekan **tombol bulat** yang ada di pojok kanan bawah layar hingga tombol bulat berwarna biru. Sebuah titik hitam akan muncul di lokasi Anda berada saat ini.

<p align="center">
<img width=25% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0305_omk_location.png" alt="Mengarahkan ke lokasi saat ini pada OpenMapKit" title="Mengarahkan ke lokasi saat ini pada OpenMapKit">
</p>

<p align="center"><i>Mengarahkan ke lokasi saat ini pada OpenMapKit</i></p>

*   Tekan **tombol pengaturan** yang ada di pojok kanan atas
*   Pilih **_OSM XML Downloader_** untuk men-_download_ data OSM sesuai dengan tampilan di layar _smartphone_ Anda (lama tidaknya waktu _download_ bergantung pada besar kecilnya area). Pastikan Anda tersambung dengan koneksi internet saat men-_download_ data OSM. Perhatikan warna bangunan, bangunan pada _basemap_ OSM berwarna cokelat dan bangunan hasil _download_ berwarna ungu.

<p align="center">
<img width=60% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0306_warna_bangunan.png" alt="Perbedaan Warna Bangunan" title="Perbedaan Warna Bangunan">
</p>

<p align="center"><i>Warna bangunan pada basemap OSM (kiri) dan Warna bangunan hasil download (kanan)</i></p>

*   Data OSM yang baru saja di-_download_ akan tersimpan dalam format _.osm_ yang dapat diaktifkan atau dinonaktifkan melalui **tombol pengaturan** **→ _OSM XML Layer_**.

<p align="center">
<img width=50% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0307_xml_layer.png" alt="Pengaturan OSM XML Downloader dan OSM XML Layers" title="Pengaturan OSM XML Downloader dan OSM XML Layers">
</p>

<p align="center"><i>Pengaturan OSM XML Downloader dan OSM XML Layers</i></p>

**b. Menambahkan informasi bangunan di _OpenMapKit_**

Jika sudah berhasil men-_download_ data bangunan dari OSM, Anda dapat menambahkan informasi bangunan tersebut dengan cara:

*   Pilih pada bangunan yang akan ditambahkan informasinya. Pastikan bangunannya berwarna ungu yang menandakan bangunan tersebut sudah di-_download_ dari OSM. Jika bangunan terpilih, warnanya akan berubah menjadi oranye.
*   Anda dapat mengisi informasi bangunan tersebut sesuai dengan formulir yang sudah Anda pilih sebelumnya di aplikasi _ODK Collect_, dengan cara tekan pada informasi _tag_ pada baris pertama yang terletak di bawah.

<p align="center">
<img width=50% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0308_mengisi_form_omk.png" alt="Mengisi informasi bangunan menggunakan formulir dari ODK Collect" title="Mengisi informasi bangunan menggunakan formulir dari ODK Collect">
</p>

<p align="center"><i>Mengisi informasi bangunan menggunakan formulir dari ODK Collect</i></p>

*   Setelah selesai, di akhir halaman pilih **_Save_** untuk menyimpan isian formulir ke dalam _ODK Collect_. Jika sudah selesai mengisikan formulir, bangunan yang Anda isikan informasinya akan terlihat seperti ini:

<p align="center">
<img width=25% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0309_tag_bangunan_omk.png" alt="Tampilan bangunan yang sudah diisikan informasinya" title="Tampilan bangunan yang sudah diisikan informasinya">
</p>

<p align="center"><i>Tampilan bangunan yang sudah diisikan informasinya</i></p>

Jika lokasi survei Anda masih belum tersedia data bangunannya di dalam OSM, Anda dapat memetakan bangunan terlebih dahulu sebelum melakukan survei. Jika tidak ada waktu untuk melakukan pemetaan bangunan, Anda dapat menggunakan titik untuk menandakan objek di aplikasi _OpenMapKit_ dengan cara:

*   Gunakan _.mbtiles_ yang sudah Anda masukkan sebelumnya untuk membantu menandai objek secara akurat dengan cara tekan **tombol pengaturan** **→ _Basemap_**
*   Tekan **ikon plus (+)** yang ada di pojok kanan bawah layar Anda hingga berubah warna menjadi hijau. Akan muncul _marker_ atau penanda warna hijau dengan tulisan _Add Node_ di atasnya. Geser peta hingga lokasi penanda akurat dengan objek yang disurvei.

<p align="center">
<img width=25% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0310_add_node_omk.png" alt="Menambahkan penanda menggunakan ikon plus (+)" title="Menambahkan penanda menggunakan ikon plus (+)">
</p>

<p align="center"><i>Menambahkan penanda menggunakan ikon plus (+)</i></p>

*   Tekan **_Add Node_** jika titik sudah akurat

<p align="center">
<img width=25% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0311_tombol_add_node.png" alt="Tombol add node saat menambahkan titik" title="Tombol add node saat menambahkan titik">
</p>

<p align="center"><i>Tombol add node saat menambahkan titik</i></p>

*   Jika titik yang Anda tambahkan ternyata posisinya kurang sesuai dengan objek yang ada di lapangan, Anda dapat menggeser titik yang sudah tambahkan dengan cara klik titik yang akan digeser kemudian tekan ikon dua panah di pojok kanan atas. Warna titik akan berubah menjadi oranye dan di atasnya terdapat tulisan _Place Node_.

<p align="center">
<img width=30% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0312_menggeser_node.png" alt="Menggeser titik yang sudah ditambahkan" title="Menggeser titik yang sudah ditambahkan">
</p>

<p align="center"><i>Menggeser titik yang sudah ditambahkan</i></p>

*   Geser peta hingga posisi titik akurat, kemudian tekan **_Place Node_**.

<p align="center">
<img width=30% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0313_place_node.png" alt="Tombol place node saat menggeser titik" title="Tombol place node saat menggeser titik">
</p>

<p align="center"><i>Tombol place node saat menggeser titik</i></p>

*   Setelah posisi titik sudah akurat dan sama dengan objek yang ada di lapangan, Anda dapat melakukan pengisian formulir sama seperti langkah sebelumnya.
*   Masukkan informasi yang sesuai dengan kondisi di lapangan. Geser layar ke kanan atau ke kiri untuk mengganti halaman pertanyaan pada formulir.
*   Di akhir halaman, pilih **_Save_** untuk menyimpan isian formulir ke dalam _ODK Collect_. Jika sudah selesai mengisikan formulir, titik objek yang Anda isikan informasinya akan terlihat seperti ini:

<p align="center">
<img width=25% src="/pages/01-OSM-Field-Surveyor-Guideliness/03-Menggunakan-Aplikasi-OMK/images/0314_finished_tag.png" alt="Tampilan titik objek yang sudah diisikan informasinya" title="Tampilan titik objek yang sudah diisikan informasinya">
</p>

<p align="center"><i>Tampilan titik objek yang sudah diisikan informasinya</i></p>

*   Anda dapat melihat formulir yang sudah berhasil disimpan pada _ODK Collect_, yang dapat Anda pelajari di modul **Menggunakan Aplikasi ODK Collect**.

**RINGKASAN**

Jika Anda dapat mengikuti dan memperhatikan seluruh tahapan dalam bab ini, maka Anda telah berhasil memahami _OpenMapKit_ sebagai salah satu alat survei lapang untuk mengambil data infrastruktur. Selain itu, Anda juga telah berhasil menerapkan pengoperasian cara pengaturan awal _OpenMapKit_, cara memasukkan _offline basemap_ untuk _OpenMapKit_ dan cara penggunaan _OpenMapKit_ untuk mengambil data infrastruktur. Formulir yang sudah Anda tambahkan di dalam aplikasi _OpenMapKit_ dapat dilihat dan dikirimkan ke server melalui aplikasi _ODK Collect_.


