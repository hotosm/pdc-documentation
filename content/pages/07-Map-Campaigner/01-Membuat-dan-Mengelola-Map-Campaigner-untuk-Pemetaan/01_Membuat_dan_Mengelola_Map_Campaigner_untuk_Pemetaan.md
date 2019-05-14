---
title: Membuat dan Mengelola Map Campaigner untuk Pemetaan
---

**Tujuan pembelajaran:**

* Mengetahui dan memahami cara kerja _Map Campaigner_
* Mengoperasikan _Map Campaigner_ untuk membuat kegiatan pemetaan
* Mengoperasikan _Map Campaigner_ untuk memantau kegiatan pemetaan

Dalam melaksanakan proyek pemetaan seringkali  Anda membutuhkan sebuah laporan terkait progres kegiatan tersebut dalam sebuah data statistik mengenai seberapa banyak objek yang telah terpetakan dalam kegiatan tersebut. Terdapat beberapa alat yang bisa digunakan untuk mendapatkan data statistik tersebut. Salah satu alat yang akan kita pelajari saat ini adalah _Map Campaigner._


## I. Apa itu _Map Campaigner_?

_Map Campaigner_ merupakan sebuah alat yang ditujukan untuk mengumpulkan semua manajer proyek dan juga _surveyor_ ke dalam satu platform. Manajer proyek bisa mengatur kegiatan dengan tipe yang spesifik sesuai dengan kebutuhan mereka. Setiap kegiatan pemetaan yang dibuat oleh manajer proyek bisa diatur secara spesifik  terkait data dan objek yang dikumpulkan kemudian akan disajikan dalam setiap proyek pemetaan.


## II. Manfaat dan contoh penggunaan _Map Campaigner_

_Map Campaigner_ bertujuan memudahkan para manajer proyek dalam memantau proyek pemetaan mereka. Sebagai contoh disini adalah kegiatan pemetaan yang dilakukan oleh tim HOT untuk memetakan semua tempat ibadah, sekolah, universitas dan sekolah tinggi yang ada di Jakarta Pusat. Dengan menggunakan _Map Campaigner_, Anda bisa melihat berapa banyak total objek yang sudah terpetakan dalam kegiatan proyek ini, kemudian berapa banyak pengguna _OpenStreetMap_ yang membantu untuk turut serta dalam proyek pemetaan ini, baik secara sukarela maupun yang tergabung ke dalam tim proyek pemetaan.

<p align="center">
  <img width=80% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0101_contoh_penggunaan_map_campaigner_untuk__jakarta_pusat.png">
</p>
<p align="center"><i>Contoh penggunaan Map Campaigner untuk  Jakarta Pusat</i><p align="center">


Dengan menggunakan _Map Campaigner,_ Anda juga bisa mengetahui berapa banyak objek yang sudah lengkap secara definisi _tags_ atau atribut yang dibutuhkan. Misalkan pada gambar di atas, terlihat bahwa dari kegiatan proyek pemetaan ini berhasil memperoleh 1.705 objek dengan menjangkau pengguna sebanyak 157 pengguna (baik yang secara sukarela maupun termasuk tim _surveyor_). _Map Campaigner_ juga memberikan informasi mengenai kelengkapan semua data yang dikumpulkan, misalnya dari 486 objek sekolah yang terpetakan, hanya 36,2% dari objek sekolah tersebut yang lengkap terpetakan dari segi atribut informasi  yang dibutuhkan untuk proyek pemetaan ini. 

_Map Campaigner_ juga menyajikan fitur penjaminan kualitas dari segi kelengkapan atribut suatu objek di OSM. Dengan _Map Campaigner_ Anda  bisa melihat berapa banyak objek yang masih belum lengkap dari segi atribut data yang sudah ditentukan sebelumnya. Anda  bisa mengunduh semua objek tersebut dan kita perbaiki dengan menggunakan JOSM.


<p align="center">
  <img width=80% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0102_contoh_pengecekan_atribut_oleh_map_campaigner.png">
</p>
<p align="center"><i>Contoh pengecekan atribut oleh Map Campaigner</i><p align="center">



## III. Membuat Proyek Pemetaan Baru di _Map Campaigner_

Sampai saat ini Anda telah mengetahui apa itu _Map Campaigner_ dan apa saja manfaat dan contoh _Map Campaigner_. Anda mungkin akan menggunakan _Map Campaigner_ untuk proyek pemetaan Anda sendiri. Agar dapat membuat _project_ baru, Anda harus _login_ terlebih dahulu dengan akun _OpenStreetMap_ Anda. Setelah Anda berhasil _login_ dengan akun Anda, selanjutnya Anda perlu mengklik tombol **_Create Campaign_**. Berikutnya terdapat beberapa tahapan setelah Anda berhasil _login_ dengan akun _OpenStreetMap_ Anda. Setelah mengklik tombol **_Create Campaign_**, Anda akan diarahkan ke halaman pembuatan proyek _campaign_ baru. Pada halaman ini terdapat dua tahapan: **mengatur informasi dasar** dan **mengatur area kerja**.


### a. Mengatur Informasi Dasar untuk Proyek _Campaign_ Anda
Pada bagian ini, Anda akan mengisi informasi dasar untuk proyek Anda. Anda harus mengisi beberapa informasi pada halaman ini:

*   **Nama proyek.** Pada bagian ini, Anda cukup mengisikan nama proyek yang sedang Anda lakukan.
*   **Durasi proyek berlangsung.** Pada bagian ini, Anda akan mengatur durasi proyek berlangsung. Anda bisa memberikan tanggal yang telah lampau apabila proyek pemetaan yang Anda lakukan adalah proyek pemetaan yang sudah selesai.
*   **Deskripsi proyek.** Pada bagian ini, Anda akan mengisikan mengenai deskripsi kegiatan proyek.
*   **Atribut/_tags_ yang dibutuhkan.** Pada bagian ini Anda akan memberikan atribut _OpenStreetMap_ yang dibutuhkan selama proyek pemetaan berlangsung. Untuk atribut _OpenStreetMap_ yang dibutuhkan, Anda bisa mengacu pada halaman Wikipedia[^1] atau pada modul **Model Data _OpenStreetMap_**. Format pengisian pada halaman ini Anda bisa memilih menggunakan struktur data **_YAML_** (yang sudah Anda pelajari pada modul _**Penggunaan YAML pada HOT Export**_) atau dengan versi mudah yang sudah disediakan pada situs ini.


<p align="center">
  <img width=80% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0103_tampilan_saat_memasukkan_atribut_osm_untuk_map_campaigner.png">
</p>
<p align="center"><i>Tampilan saat memasukkan atribut OSM untuk Map Campaigner</i><p align="center">


>Catatan:
>
>       Saat memasukkan tag/atribut dalam format YAML. Ada beberapa hal yang harus diperhatikan:
>       
>       - Penggunaan spasi sangat sensitif disini. 
> 
>       - Satu elemen terdiri dari elemen utama dan elemen pendukung
>       
>       - Semua elemen dibawah elemen utama (elemen pendukung) harus berada beberapa spasi dibandingkan elemen utama
>       
>       - Isi elemen pendukung = feature, tags, & element_type
>       
>       - feature merupakan kategori yang ada di OSM. Untuk lebih jelasnya bisa melihat wikipedia OSM
>       
>       - Agar lebih spesifik, Anda bisa menggunakan set key & value seperti misalnya building=school atau amenity=hospital
>       
>       - tags merupakan kumpulan atribut (key & value) OSM yang akan diperiksa oleh sistem. Harap cek wikipedia atau modul Model Data OpenStreetMap
>       
>       - element_type merupakan jenis objek OSM yang akan diperiksa. Apakah titik (point), garis (line), atau area (polygon) 





*   **Menambahkan manajer proyek lainnya (opsional).** Pada bagian ini Anda bisa menambahkan akun _OSM_ lainnya sebagai manajer proyek _campaign_ apabila proyek yang Anda kerjakan terdapat lebih dari satu orang manajer proyek. Peran dari manajer proyek ini adalah mereka bisa menambahkan atribut baru untuk dihitung atau mengubah informasi yang ada pada proyek _campaign_ mereka.

    
<p align="center">
  <img width=90% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0104_tampilan_pada_halaman_informasi_dasar.png">
</p>
<p align="center"><i>Tampilan pada halaman informasi dasar</i><p align="center">


### b. Mengatur Area Kerja untuk _Project Campaign_ Anda
Setelah Anda berhasil mengatur informasi dasar, langkah berikutnya adalah Anda harus mengatur area kerja proyek Anda. Pada bagian ini, terdapat dua cara untuk mengatur area kerja proyek Anda.

Cara pertama adalah dengan menggunakan alat yang ada pada bagian sebelah kiri peta. Anda bisa menggambar kotak ataupun menggambar secara bebas dengan menggunakan alat tersebut. Hal yang perlu diingat adalah **luas area proyek _campaign_ tidak boleh lebih dari 315 km2.** Apabila proyek pemetaan Anda memiliki luas lebih dari yang telah disebutkan, disarankan untuk membagi wilayah proyek pemetaan tersebut kedalam beberapa bagian agar dapat dibuat di _Map Campaigner_.

Cara kedua adalah dengan menggunakan data batas administrasi dalam format _GeoJSON_. Dengan menggunakan data tersebut, Anda dapat langsung melihat area kerja proyek Anda yang sudah terbagi menjadi beberapa bagian.

Setelah mengatur area kerja proyek, Anda dapat menetapkan tim mana saja yang bertugas untuk area proyek yang sudah ditentukan sebelumnya. Pengaturan tim ini sifatnya opsional dan bertujuan untuk memudahkan memantau perkembangan tim Anda.


<p align="center">
  <img width=90% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0105_tampilan_pada_halaman_pengaturan_area_kerja.png">
</p>
<p align="center"><i>Tampilan pada halaman pengaturan area kerja</i><p align="center">


## IV. Tampilan Halaman Proyek _Map Campaigner_ Anda

Setelah berhasil membuat proyek _campaign_, Anda bisa langsung menuju halaman utama untuk melihat proyek. Ketika membuka proyek pemetaan, Anda akan disajikan beberapa informasi mulai dari data statistik, daftar kesalahan/_error_, dan grafik pengguna yang turut serta dalam pemetaan.



<p align="center">
  <img width=90% src="/pages/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/images/0106_tampilan_halaman_map_campaigner.png">
</p>
<p align="center"><i>Tampilan halaman Map Campaigner</i><p align="center">




1. **_Feature collected._** Bagian ini menjelaskan tentang berapa banyak total objek yang dikumpulkan pada area kerja.
2. **_User engaged_.** Menjelaskan tentang berapa banyak pengguna OSM yang turut serta membantu memetakan baik secara sukarela maupun tidak.
3. **_Area covered._** Menjelaskan tentang berapa persen area yang telah lengkap terpetakan.
4. **_Feature selection_.** Untuk memilih fitur OSM yang telah ditentukan sebelumnya.
5. **_Selected attribute_.** Menjelaskan beberapa atribut OSM yang harus dicek oleh sistem untuk mengetahui kelengkapan atributnya.
6. **_Attribute completeness_.** Menjelaskan tentang berapa persen objek OSM yang telah lengkap memiliki atribut seperti yang sudah ditentukan pada bagian **_selected attribute_**.
7. **_Feature checked._** Menjelaskan tentang jumlah objek OSM yang telah dikumpulkan, spesifik hanya pada satu fitur saja sesuai dengan bagian **_feature selection_**. 
8. **_Graph_.** Menjelaskan tentang grafik jumlah objek secara rinci

Selain beberapa tampilan di atas, terdapat pula bagian **_Errors_** yang menjelaskan tentang daftar objek yang belum dilengkapi dari segi atribut OSM. Selain itu Anda juga bisa melihat pada bagian **_User Enggagement_** mengenai daftar pengguna OSM yang turut serta membantu memetakan daerah tersebut beserta jumlah kontribusi dari masing-masing pengguna OSM.


## V. Memperbaiki Objek OSM yang Belum Lengkap

Dengan menggunakan _Map Campaigner_, Anda bisa langsung memperbaiki objek OSM yang belum lengkap dari segi atribut datanya. Untuk memperbaikinya terdapat dua cara.

*   Cara yang pertama adalah dengan memperbaiki satu-persatu objek OSM tersebut dengan memilih id objek pada kolom **_Name_**. Dengan cara ini Anda akan diarahkan ke halaman situs _OpenStreetMap_ dan kemudian Anda bisa langsung mengubahnya dengan menggunakan **JOSM** ataupun **iD**.

*   Cara kedua adalah dengan mengklik tombol **_Download_** yang ada pada bagian bawah dari daftar _errors_. Dengan menggunakan ini, Anda akan mengunduh _file_ .osm untuk dapat dibuka dengan menggunakan JOSM. Setelah berkas berhasil anda unduh, Anda dapat langsung membukanya di JOSM untuk langsung melengkapi atributnya.


**RINGKASAN**

Selamat! Saat ini Anda telah berhasil mempelajari cara menggunakan _Map Campaigner_ untuk keperluan proyek pemetaan Anda. Dengan menggunakan _Map Campaigner_ Anda akan lebih mudah mengetahui berapa banyak objek yang berhasil terpetakan secara mudah dan melihat mana saja objek OSM yang belum memiliki kelengkapan atribut yang sesuai dengan proyek Anda.


[^1]:

    https://wiki.openstreetmap.org/wiki/Map_Features
    https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines



