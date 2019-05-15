---
title: Mengatasi Konflik pada Data OpenStreetMap (OSM)
weight: 10
---

**Tujuan Pembelajaran:**

*   Mampu menjelaskan pengertian konflik data OSM pada JOSM
*   Mampu menjelaskan jenis-jenis konflik data di JOSM
*   Mampu melakukan cara memperbaiki konflik data di JOSM
*   Mampu memahami cara menghindari konflik data di JOSM

Saat Anda meng-_upload_ objek dengan menggunakan JOSM, beberapa kontributor OSM mungkin saja sedang mengedit wilayah yang sama dengan Anda. Hal ini dapat menimbulkan konflik pada saat Anda meng-_upload_ objek OSM. Untuk itu, pada modul ini Anda akan mempelajari apa itu konflik pada JOSM, jenis konflik, dan cara menyelesaikan konflik pada JOSM.

### **I. Pengertian konflik data OSM pada JOSM**

Ketika Anda sedang bekerja di JOSM dan ketika Anda meng-_upload_ peta yang telah diedit (pelajari selengkapnya pada modul **Menggunakan JOSM**), mungkin Anda pernah mendapatkan pesan seperti ini:

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1001_conflict.png" alt="konflik" title="Jendela konflik terdeteksi"></p>
<p align="center"><i>Contoh jendela apabila konflik terdeteksi</i></p>

Gambar diatas menunjukkan konflik yang terjadi pada data OSM. Mengapa konflik data pada OSM dapat terjadi? Hal ini dikarenakan, pada saat Anda mengedit di JOSM, Anda mengedit data OSM yang sama dengan pengguna lainnya pada waktu yang bersamaan. Kemudian pengguna lain lebih dahulu meng-_upload_ perubahan data ke server OSM, sehingga ketika Anda ingin meng-_upload_ hasil kerja Anda, server sudah memiliki versi yang baru. 

Anda akan berhadapan dengan konflik ketika Anda melakukan perubahan data OSM dengan mengedit, menambahkan, atau menghapus dari server utama, dimana data tersebut juga sedang diedit oleh orang lain. Karena Anda hanya bekerja pada sebuah salinan di JOSM yang tersimpan pada komputer Anda, pengguna lain masih dapat menerima, mengedit dan meng-_upload_ objek-objek OSM di area yang sama dan di waktu yang bersamaan dengan Anda. Kemudian, ketika objek tersebut telah Anda edit dan di-_upload_ pada saat yang bersamaan, server OSM tidak mengetahui versi mana yang benar dan hasil perubahan mana yang akan disimpan. Jika terjadi hal demikian, maka konflik perlu diperbaiki dan diselesaikan sebelum Anda meng-_upload_ data ke server OSM.

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1002_ilustrasi_konflik.png" alt="ilustrasi_konflik" title="Ilustrasi konflik"></p>
<p align="center"><i>Contoh ilustrasi penyebab konflik</i></p>

Gambar diatas merupakan contoh konflik yang mungkin terjadi diakibatkan oleh perbedaan antara lokasi objek versi Anda (versi saya) dan versi yang ada di server OSM (versi mereka). Untuk menyelesaikan konflik tersebut, Anda harus memilih salah satu versi diantara kedua versi tersebut (lihat **III. Cara memperbaiki konflik data di JOSM**).

### **II. Jenis-jenis konflik data di JOSM**

**a. Konflik properti**

Konflik properti merupakan konflik yang disebabkan perbedaan titik koordinat yang terjadi pada sebuah objek yang telah dipindahkan atau dihapus posisinya pada dua versi yang berbeda. Hal ini dapat disebabkan objek tersebut telah diedit, dipindahkan posisinya atau dihapus oleh pengguna lain.

<p align="center">
<img width=80% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1003_konflik_properti.png" alt="konflik_properti" title="Jenis konflik properti"></p>
<p align="center"><i>Tampilan jendela konflik properti</i></p>

Gambar diatas merupakan contoh jenis konflik yang disebabkan oleh perbedaan versi posisi salah satu _node_/titik pada suatu objek. Untuk menyelesaikannya Anda perlu memilih versi posisi titik mana yang ingin Anda gunakan.

**b. Konflik _tag_**

Konflik _tag_ terjadi akibat adanya perbedaan _tag_ atau informasi yang terjadi pada sebuah objek yang telah diubah atau dihapus posisinya pada dua versi yang berbeda.

<p align="center">
<img src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1004_konflik_tag.png" alt="konflik_tag" title="Jenis konflik tag"></p>
<p align="center"><i>Tampilan jendela konflik tag</i></p>

Gambar diatas menunjukkan perbedaan versi _tag_ pada objek yang sama. **_My version_** menunjukkan objek yang mempunyai _tag_ Rumah Sakit (_amenity = hospital_) dengan nama Rumah Sakit Tebet Raya. Sedangkan objek pada **_Their version_** menggunakan tag klinik (_amenity = clinic_) dengan nama RS Tebet Timur. Untuk menyelesaikannya, Anda perlu memilih salah satu versi _tag_ yang menurut Anda paling benar.

**c. Konflik _node_/titik**

Konflik pada titik/_node_ terdapat  perbedaan pada daftar titik/_node_ yang terjadi pada sebuah objek yang berbentuk garis, dimana titik pada garis tersebut telah dipindahkan atau dihapus posisinya pada dua versi yang berbeda. 

<p align="center">
<img src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1005_konflik_node.png" alt="konflik_node" title="Jenis konflik node"></p>
<p align="center"><i>Tampilan jendela konflik node/titik</i></p>


### **III. Cara memperbaiki konflik data di JOSM**
Proses dalam menyelesaikan konflik cukup sederhana di dalam JOSM, walaupun sebagian besar pengguna OSM mengalami kebingungan untuk menyelesaikan permasalahan konflik pada data OSM. Pada dasarnya, semua konflik yang terjadi JOSM akan menyediakan dua pilihan - objek versi Anda dan satu lagi versi orang lain yang berada di server. Anda harus memilih apakah ingin tetap menggunakan **versi Anda** atau **versi server**. Langkah untuk menyelesaikan konflik adalah sebagai berikut:



*   Ketika jendela konflik muncul, Anda mungkin akan memilih tombol **Synchronize node 5,960,126 only**, tetapi pilihan ini hanya akan memperbaiki konflik yang terjadi pada satu _node_/titik tertentu. Oleh karena itu, sebaiknya Anda memilih tombol **Synchronize entire dataset** agar anda dapat menyelesaikan seluruh konflik sekaligus.

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1006_kotak_konflik.png" alt="kotak_konflik" title="Kotak konflik"></p>
<p align="center"><i>Tampilan kotak dialog ketika konflik terdeteksi</i></p>

*   Setelah itu akan muncul jendela berisi jumlah konflik yang terdeteksi, klik **_OK_**.

<p align="center">
<img src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1007_conflict_detected.png" alt="jumlah_konflik" title="Jumlah konflik"></p>
<p align="center"><i>Jumlah konflik yang terdeteksi</i></p>

*   Akan muncul daftar konflik pada panel **Conflict** di sebelah kanan peta Anda. Untuk menyelesaikan konflik yang muncul, Anda dapat memilih konflik pada panel tersebut dengan cara klik pada konflik kemudian klik **_Resolve_**.

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1008_panel_conflict.png" alt="panel_conflict" title="Panel konflik"></p>
<p align="center"><i>Panel Conflict untuk menyelesaikan konflik yang terdeteksi</i></p>

*   Ketika Anda klik tombol **_Resolve_**, akan muncul jendela baru yang yang berisikan detail konflik Anda. Pesan konflik tersebut mungkin terlihat rumit, namun sebenarnya sederhana. Anda akan mengetahui jenis konflik apa yang Anda dapatkan yang ditunjukkan oleh simbol ![simbol_merah](/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1009_simbol.png "simbol_merah"). Konflik dalam contoh ini terjadi karena perbedaan titik koordinat dan perubahan posisi objek. Anda dapat melihat daftar koordinat yang mengalami perubahan pada contoh gambar di bawah. Konflik yang terjadi merupakan konflik properti yang disebabkan oleh satu titik. 

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1010_penyelesaian_konflik.png" alt="penyelesaian_konflik" title="Tahap penyelesaian konflik"></p>
<p align="center"><i>Contoh tampilan jendela untuk menyelesaikan konflik</i></p>

*   Anda hanya dapat menyelesaikan dua konflik pada saat yang sama. Anda dapat memilih salah satu antara versi Anda atau versi yang lain pada _server_. Jika Anda yakin bahwa hasil editing yang Anda lakukan benar dan tepat (misalnya Anda sudah survei lapangan atau mengetahui wilayah tersebut), maka Anda dapat memilih **Versi Saya/My Version (local dataset)**. Namun, jika Anda tidak mengetahui wilayah tersebut dan melihat pengguna tersebut lebih mahir maka Anda dapat memilih **Versi mereka/Their version (server dataset)**. Klik ![tanda_panah](/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1011_tanda_panah.png "tanda_panah") tanda panah biru  pada kolom versi yang telah Anda pilih. Konflik yang sudah berhasil diselesaikan akan berubah warna menjadi hijau serta tanda centang hijau 
![konflik_selesai](/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1012_ikon_konflik_selesai.png "konflik_selesai").

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1013_tahap_penyelesaian.png" alt="tahap_penyelesaian" title="Tahap penyelesaian konflik"></p>
<p align="center"><i>Tahap memilih salah satu versi yang benar untuk penyelesaian konflik</i></p>

*   Setelah Anda memilih versi mana yang menurut Anda paling benar, Anda harus memastikan warna kolom sudah berubah dari warna merah muda menjadi warna hijau. Hal ini menandakan bahwa Anda telah berhasil memilih salah satu versi untuk menyelesaikan konflik.

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1014_perbedaan_warna.png" alt="perbedaan_warna" title="Perbedaan warna konflik"></p>
<p align="center"><i>Perbedaan warna antara konflik yang terjadi dan yang sudah diselesaikan</i></p>


*   Kemudian klik **_Apply Resolution_** seperti ditunjukkan gambar di bawah. Setelah Anda selesai menyelesaikan semua konflik, Anda dapat memulai untuk _upload_ hasil perubahan data OSM Anda.

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1015_apply_resolution.png " alt="apply_resolution" title="Menyelesaikan konflik"></p>
<p align="center"><i>Tampilan jendela konflik yang berhasil diselesaikan</i></p>

*   Pada jendela menu, Anda memiliki kotak jendela **Conflicts** ![ikon_konflik](/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1016_ikon_konflik.png "ikon_konflik"). Jendela ini menampilkan jumlah dari daftar konflik yang terjadi pada cara klik pada salah satu konflik lalu klik tombol **_Resolve_**. Anda juga dapat menggunakan cara lain yaitu dengan klik kanan pada salah satu konflik, lalu pilih **_Resolve to my versions_** atau **_Resolve to their versions._** Untuk menemukan objek yang terkena konflik, klik kanan lalu klik **_Zoom to Conflict_**. Ini sangat berguna apabila Anda berhadapan dengan banyak konflik dan Anda perlu memeriksa dan menyelesaikannya satu per satu.  

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1017_zoom_conflict.png" alt="zoom_conflict" title="Zoom pada konflik"></p>
<p align="center"><i>Tampilan jendela dari daftar konflik pada JOSM</i></p>

> Catatan :
Anda tidak dapat meng-upload perubahan sampai panel _Conflicts_ kosong dan semua konflik telah diselesaikan. Perlu diperhatikan bahwa Anda perlu berhati-hati dalam menyelesaikan konflik yang terjadi dan sebaiknya konflik diperiksa dan diselesaikan satu persatu agar hasilnya lebih maksimal.

### **IV. Cara menghindari konflik data di JOSM**
Anda dapat melakukan beberapa hal, agar terhindar dari konflik saat meng-_upload_ objek ke dalam server OSM.

**a. Meng-_upload_ hasil perubahan secara berkala**
*   Untuk meminimalkan konflik yang dapat terjadi, Anda dapat mengupload secara berkala untuk hasil pengeditan data OSM. Misalnya, jika Anda akan melakukan pemetaan 100 bangunan dan koneksi internet Anda tidak bagus, maka Anda dapat mengupload secara berkala setiap Anda mendijitasi 20 bangunan atau setiap 15 menit sekali. Kemungkinan konflik akan muncul lebih banyak apabila Anda mengedit seluruh wilayah terlebih dahulu dan menunda untuk meng-_upload_ nya. Semakin lama selang waktu antara men-_download_ data dengan meng-_upload_ editan Anda, maka semakin besar kemungkinan seseorang telah mengedit data tersebut pada saat itu.
*   Jika Anda menyimpan data OSM dan ingin meng-_upload_ di waktu yang tidak bersamaan, maka Anda dapat membarui data OSM untuk mendapatkan data OSM terbaru yang ada di server OSM. Sebelum meng-_upload_ pekerjaan Anda ke OSM, klik pada menu **_File → Update data_** atau pilih **_Update Modified_** lalu tunggu sampai proses pembaharuan data selesai. Setelah itu Anda dapat meng-_upload_ data dengan menggunakan opsi **_Upload data_** pada menu **_File_** atau klik ikon  ![ikon_upload](/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1018_ikon_upload.png "ikon_upload") pada _bar menu_.

<p align="center">
<img width=30% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1019_update_data.png" alt="update data" title="update data"></p>
<p align="center"><i>Pilihan update data pada menu File</i></p>


**b. Lakukan perubahan hanya di area yang di-_download_**

Anda dapat melakukan pemetaan di wilayah yang spesifik untuk mengurangi risiko konflik dengan tidak mengedit objek yang berada di area yang diarsir pada data layer JOSM. Langkah ini dapat menghindari banyak pengguna mengedit di wilayah yang sama. Anda dapat dengan mudah melihat mana daerah luar dari daerah yang Anda _download_ di JOSM, karena latar belakang daerah luar tersebut terdapat garis-garis diagonal (arsiran), bukan hanya warna hitam.

<p align="center">
<img width=30% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1020_perbedaan_area_download.png" alt="area_download" title="Perbedaan area download"></p>
<p align="center"><i>Perbedaan area hasil download (hitam polos) dan area di luar hasil download (garis arsiran)</i></p>

 Setelah Anda melakukan _download_ data, area untuk Anda melakukan perubahan ialah area kotak yang tidak mempunyai garis arsiran. Area diluar kotak yang merupakan area arsiran adalah area yang mungkin saja sedang dikerjakan oleh pengguna lain. Sebaiknya Anda menghindari area tersebut untuk menghindari terjadinya konflik.

**c. Menggunakan _Tasking Manager_**

Jika Anda ingin memetakan wilayah yang sama secara kolaboratif, maka Anda dapat menggunakan _Tasking Manager_. Dengan menggunakan _Tasking Manager_, Anda lebih mudah memilih wilayah yang spesifik dan wilayah tersebut tidak bisa diambil oleh pengguna lainnya.
Para relawan pemetaan di area tersebut dapat memilih sebuah kotak yang ingin dipetakan, dan ketika mereka selesai melakukan pemetaan, mereka dapat menandai kotak tersebut sebagai komplit atau sudah selesai dipetakan. Dengan cara ini, sebuah tim yang berisi banyak orang yang tersebar di berbagai daerah dapat berkoordinasi bersama untuk menyelesaikan pemetaan pada grid tersebut. Penggunaan _grid_/kotak untuk membagi area kerja masing-masing tiap pengguna dapat meminimalisasi terjadinya konflik di JOSM. Cara penggunaan _Tasking Manager_ selengkapnya dapat dilihat pada modul **[Penggunaan Tasking Manager].**

<p align="center">
<img width=70% src="/pages/03-JOSM/10-Mengatasi-konflik-data-pada-OpenStreetMap/images/1021_tasking_manager.png" alt="tasking_manager" title="Tampilan Tasking Manager"></p>
<p align="center"><i>Tampilan situs Tasking Manager (tasks.openstreetmap.id)</i></p>


**RINGKASAN**

Jika Anda dapat mengikuti dan mempraktikkan seluruh tahapan dalam bab ini, maka Anda telah berhasil mengetahui pengertian konflik dan menyelesaikan konflik pada data OSM dengan menggunakan JOSM. Selain itu, Anda juga telah berhasil mempelajari jenis-jenis konflik yang dapat terjadi dan mengetahui cara-cara untuk menghindari konflik pada JOSM.

