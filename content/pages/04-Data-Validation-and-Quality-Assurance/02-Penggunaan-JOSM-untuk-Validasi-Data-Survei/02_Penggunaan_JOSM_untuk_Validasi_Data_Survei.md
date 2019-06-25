---
title: Penggunaan JOSM untuk Validasi Data Survei
weight: 2
---

**Tujuan Pembelajaran:**

*   Menerapkan cara pengecekkan awal data hasil survei lapangan di JOSM
*   Menerapkan cara penjaminan kualitas data hasil survei dengan JOSM
*   Memahami jenis-jenis kesalahan dan peringatan yang harus diperbaiki di JOSM

JOSM merupakan _software_ yang paling sering digunakan untuk melakukan pemetaan dan menambahkan data _OpenStreetMap_. JOSM lebih banyak digunakan karena dapat digunakan secara _offline_ dan memiliki banyak fitur pendukung untuk memudahkan dalam melakukan pemetaan. Salah satu fitur unggulan yang dimiliki oleh JOSM adalah melakukan validasi data. Validasi data merupakan hal yang penting dilakukan untuk menjaga kualitas data _OpenStreetMap_. 

### I. Tahapan yang Dibutuhkan untuk Memeriksa _Raw_ Data Hasil Survei

Dalam survei lapangan, _data entry_ mengumpulkan dua jenis data yaitu data objek infrastruktur dan data batas administrasi. Sebelum dimasukkan ke dalam JOSM, kedua jenis data tersebut harus diperiksa oleh tim _Quality Assurance_. Hal ini dilakukan untuk memeriksa kelengkapan atribut yang dikumpulkan yang telah disesuaikan dengan **Pembuatan Model Data OSM** dan objek-objek yang berada didalam suatu area survei apakah sudah semua di ambil datanya.

1. **Memeriksa Hasil Survei menggunakan Batas Administrasi**
    <br>Hasil survei yang telah dikumpulkan harus dicek menggunakan batas administrasi yang ada. Tujuannya untuk melihat apakah seluruh objek yang ada dalam batas administrasi tersebut telah selesai disurvei atau belum. Anda dapat menggunakan batas administrasi yang diperoleh dari BPS atau dengan menggunakan batas administrasi yang telah digambar oleh _Quality Assurance_. 

   *   Silakan Anda buka hasil survei yang telah dikumpulkan. Sebagai contoh, dalam modul ini akan digunakan data hasil survei di daerah Yogyakarta. 
       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0201_Contoh_data_hasil_survei_di_Desa_Wedomartani.png"></p>
        <p align="center"><i>Contoh data hasil survei di Desa Wedomartani, Sleman, Yogyakarta</i></p>

   *   Setelah itu, silakan Anda buka _file_ batas administrasi yang Anda miliki. Dalam contoh ini akan digunakan data batas desa yang didapatkan dari BPS. Data dari BPS masih dalam format .shp. Untuk dapat dibuka di dalam JOSM, Anda perlu mengubah format data ini menjadi bentuk GeoJSON. Anda dapat membuka materi **Menggunakan GeoJSON** untuk mempelajari bagaimana cara mengubah format data ini. 

        Untuk membuka _file_ batas administrasi, silakan pilih menu **File → Open**, kemudian masukkan batas administrasi yang Anda miliki.

       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0202_Overlay_data_survey_dengan_batas_admin.png"></p>

   *   Anda dapat membandingkan antara sebaran titik yang telah dikumpulkan dengan batas administrasi. Jika menurut Anda titik-titik yang dikumpulkan masih belum memenuhi target pemetaan yang diberikan atau masih ada objek-objek yang belum disurvei, Anda dapat meminta _Data Entry_ untuk melakukan survei ulang untuk memenuhi target yang diinginkan. 
 
2. **Memeriksa Hasil Survei Batas Administrasi**
    <br>_Data entry_ menggunakan peta survei untuk menggambarkan batas administrasi yang didapatkan dari hasil diskusi dengan pihak kelurahan. Anda dapat melakukan pengecekan jumlah RW yang dihasilkan dalam kelurahan tersebut dan batas-batas di dalam peta apakah sudah jelas atau belum.

3. **Menggabungkan hasil survei menjadi satu layer**
    <br>Anda harus menggabungkan _file_ hasil survei _ODK Collect_ menjadi satu _file_ yang sama. Untuk menggabungkannya, langkah-langkah yang harus Anda lakukan adalah:

*   Silakan Anda cari _file_ _ODK Collect_ yang telah Anda pindahkan dari _smartphone_ ke laptop/komputer Anda dengan menggunakan **Windows Explorer**. Jika Anda lupa bagaimana cara memindahkan data ODK Collect dari _smartphone_ ke laptop/komputer Anda, silakan baca kembali modul **Menggunakan Aplikasi ODK Collect**. Sebagai contoh, dalam modul kali ini akan digunakan data hasil survei yang dilakukan di daerah Yogyakarta.

       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0203_Data_ODK_Collect_yang_sudah_dipindahkan_ke_laptop.png"></p>
        <p align="center"><i>Data ODK Collect yang sudah dipindahkan ke laptop/komputer</i></p>

*   Setelah itu, pada kolom pencarian di sebelah kanan atas, silakan Anda ketik **‘.osm’**. Hal ini bertujuan untuk mencari seluruh data hasil survei dengan format .osm. 
       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0204_Pencarian_data_dengan_format_osm.png"></p>
        <p align="center"><i>Pencarian data dengan format .osm</i></p>

*   Jika sudah, silakan Anda pilih semua data tersebut dengan cara klik pada salah satu _file_ dan tekan tombol **Ctrl+A** untuk memilih seluruh file tersebut. 
  <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0205_Seluruh_file_sudah_terpilih.png"></p>
        <p align="center"><i>Seluruh file sudah terpilih</i></p>
        
*   Selanjutnya, silakan Anda klik dan tahan pada salah satu _file_, kemudian Anda geser seluruh _file_ tersebut dan masukkan ke dalam JOSM. Pastikan Anda sudah membuka _software_ JOSM terlebih dahulu. 
       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0206_Geser_dan_buka_file_osm.png"></p>
        <p align="center"><i>Geser dan buka file .osm ke dalam JOSM</i></p>

*   Jika sudah berhasil terbuka akan muncul tampilan seperti berikut
       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0207_Seluruh_file_osm_berhasil_dibuka_dalam_JOSM.png"></p>
        <p align="center"><i>Seluruh file .osm yang berhasil dibuka dalam JOSM</i></p>

*   Jika Anda lihat pada data yang telah dimasukkan, masing-masing titik hasil survei masih berada dalam satu _layer_ yang berbeda. Untuk itu Anda perlu menggabungkan seluruh data tersebut menjadi satu _layer_ baru. Untuk menggabungkannya, silakan Anda klik salah satu _layer_ data pada _layer window_ kemudian tekan tombol **Ctrl + A** untuk memilih seluruh titik, kemudian klik kanan dan pilih **_Merge_**. 
       <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0208_Menggabungkan_seluruh_layer.png"></p>
        <p align="center"><i>Menggabungkan seluruh layer</i></p>

*   Anda akan diminta untuk memilih _layer_ tujuan atau _target layer_. Anda tidak perlu mengubah _target layer_ ini dan langsung pilih **Merge**.
       <p align="center"><img width=40% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0209_Pilih_merge_untuk_menggabungkan_seluruh_data.png"></p>
        <p align="center"><i>Pilih merge untuk menggabungkan seluruh data</i></p>

*   Data yang sudah berhasil digabungkan akan menjadi hanya satu _layer_.
   <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0210_Seluruh_data_yang_sudah_digabungkan.png"></p>
        <p align="center"><i>Seluruh data yang sudah digabungkan</i></p>

*   Silakan Anda simpan layer yang telah disatukan dengan cara klik kanan pada layer tersebut, kemudian pilih **Save as**. Simpan layer ini sesuai dengan nama yang Anda inginkan.
  <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0211_Save_as.png"></p>


4. **Upload Hasil Data Survei ke Google Drive**
    <br>Setelah Anda gabungkan seluruh titik yang telah dikumpulkan, Anda perlu meng-_upload_ data tersebut ke dalam media penyimpanan yang dapat diakses secara bersama-sama, baik _Data Entry_ maupun _Quality Assurance_ secara online. Anda dapat menggunakan media penyimpanan online gratis seperti _Google Drive_. Silakan Anda upload sesuai dengan folder yang telah ditentukan. 
   <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0212_Google_drive.png"></p>

### II. Mengecek Hasil Input Data Survei
Setelah Anda melakukan pengecekan data mentah atau _raw_ data yang telah dikumpulkan, Anda perlu melakukan pengecekan terhadap data yang telah berhasil di-_upload_ ke dalam server _OpenStreetMap_. Pengecekan ini dilakukan dengan menggunakan bantuan _plugin to do list_ dan alat validasi _(validation tool)_ yang telah tersedia di _software_ JOSM.

1. Menggunakan _Plugin To do list_
    <br>Anda dapat menggunakan _plugin_ pada JOSM yang bernama _To do list_ untuk melakukan pengecekan data hasil survei. To do list memungkinkan Anda untuk membuat daftar objek-objek apa saja yang telah dikumpulkan. Dengan adanya daftar ini akan memudahkan Anda untuk melakukan pengecekan data sehingga tidak akan ada data yang terlewat. Anda dapat melihat kembali materi **Menggunakan to-do list** di JOSM untuk memahami lebih lanjut. 

    Sebagai contoh, Anda mempunyai data hasil survei sebagai berikut:
<p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0213_Contoh_data_hasil_survei.png"></p>
    <p align="center"><i>Contoh data hasil survei</i></p>

   Data tersebut dikumpulkan menggunakan ODK Collect dan Open Map Kit (OMK). Data ini harus dilakukan pengecekan apakah data tersebut telah dikumpulkan dengan benar. Terlebih dahulu Anda harus men-_download_ data OSM yang sudah ada untuk mengecek apakah objek yang disurvei sudah dipetakan atau belum. Setelah itu, Anda dapat mengecek data yang telah disurvei, Beberapa pengecekan yang dapat dilakukan antara lain memeriksa adanya kesalahan pengetikan dan peletakan titik. Mengingat banyaknya data yang harus dicek, akan lebih mudah jika Anda menggunakan _to do list_. 
   
   Sebagai contoh, Anda mempunyai data titik survei yaitu kantor kesehatan pelabuhan di daerah Jakarta Utara. Untuk itu, Anda perlu men-_download_ data OSM untuk memeriksa apakah ada kesalahan dalam melakukan input data. Anda dapat melakukan perbandingan mengenai informasi atau atribut yang telah ditambahkan, apakah masih terdapat kesalahan pengetikan atau informasi yang tidak sesuai. Pada contoh, dapat terlihat bahwa pada atribut data mentah atau _raw_ data memiliki penulisan nama objek dengan huruf kecil, namun jika dibandingkan dengan data hasil input, nama yang diketik sudah menggunakan huruf kapital pada awal kata. Hal ini menandakan bahwa _data entry_ sudah memasukan data dengan benar. 

   <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0214_Perbandingan_antara_hasil_input_dan_mentah.png"></p>
    <p align="center"><i>Perbandingan antara hasil input dan hasil data mentah</i></p>
    Selain itu, Anda juga dapat memeriksa apakah titik objek tersebut telah diletakkan sesuai dengan titik yang sebenarnya. Pada gambar terlihat bahwa data mentah (titik survei berwarna abu-abu) belum terletak sesuai dengan lokasi sebenarnya, sedangkan pada data yang sudah dipetakan titiknya telah sesuai dengan lokasi sebenarnya (titik survei berwarna). Anda dapat menggunakan bantuan citra satelit sebagai acuan untuk melihat posisi titik tersebut apakah sudah sesuai dengan objek bangunan yang ada di citra atau belum. 
 <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0215_Perbedaan_posisi_titik_data_hasil_input_dan_data_mentah.png"></p>
    <p align="center"><i>Perbedaan posisi titik data hasil input dan data mentah</i></p>

2. Menggunakan Alat Validasi
    <br>Untuk melakukan pengecekan hasil input data survei, langkah-langkah yang harus dilakukan adalah: 

   *   _Download_ data _OpenStreetMap_ pada lokasi survei yang ingin Anda cek datanya.
  <p align="center"><img width=70% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0216_Contoh_data_OSM_yang_telah_didownload.png"></p>
    <p align="center"><i>Contoh data OpenStreetMap yang telah di-download</i></p>

   *   Lakukan validasi dengan menggunakan _validation tools_ atau alat validasi yang ada di JOSM. Untuk mengaktifkan jendela validasi atau _validation result_ silakan Anda pilih menu **Window** lalu pilih **Validation Result**. Jendela validasi akan muncul di sebelah kanan bawah JOSM Anda. 
  <p align="center"><img width=30% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0217_Mengaktifkan_jendela_validasi_pada_JOSM.png"></p>
    <p align="center"><i>Mengaktifkan jendela validasi pada JOSM</i></p>

   *   Untuk melakukan validasi Anda dapat menggunakan tombol **_Validation_** yang ada pada jendela _validation result_. Satu hal yang perlu Anda perhatikan pada saat melakukan validasi adalah pastikan tidak ada objek yang sedang Anda pilih karena jika Anda sedang memilih salah satu objek, JOSM hanya akan melakukan validasi terhadap objek yang sedang Anda pilih. 
   <p align="center"><img width=40% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0218_Hasil_validasi_menggunakan_JOSM.png"></p>
    <p align="center"><i>Hasil validasi menggunakan JOSM</i></p>

   *   Perbaiki jika ada kesalahan _(error)_ dan peringatan _(warning)_ yang muncul pada data Anda hingga selesai. Setelah itu jangan lupa untuk mengunggah kembali data yang sudah Anda perbaiki ke dalam server _OpenStreetMap_. 

### III. Pengertian Kesalahan _(Error)_ dan Peringatan _(Warning)_ di JOSM

Seperti telah dijelaskan sebelumnya, ketika melakukan validasi menggunakan JOSM, Anda akan menemukan dua jenis hasil validasi: 
1. Kesalahan _(Error)_
    <br>Kesalahan atau _Error_ merupakan jenis peringatan yang bersifat wajib untuk diperbaiki. Kesalahan atau _Error_ berguna untuk memberitahukan adanya objek yang tidak dipetakan sesuai kaidah _OpenStreetMap_. Anda tidak dapat melakukan _upload_ data jika Anda belum menyelesaikan kesalahan atau _error_ pada _changeset_ Anda. 

2. Peringatan _(Warning)_
    <br>Berbeda dengan kesalahan atau _error_, peringatan atau _warning_ tidak bersifat wajib untuk diperbaiki. Sesuai dengan namanya, peringatan atau _warning_ diberikan untuk memberikan informasi bahwa terdapat ketidaksesuaian dalam pemetaan Anda. Peringatan ini dapat Anda abaikan dan Anda tetap dapat melakukan _upload_ data ke dalam server _OpenStreetMap_. Meskipun demikian, ada juga beberapa jenis _warning_ yang sebaiknya diperbaiki seperti _crossing building, building inside building, crossing ways,_ dan sebagainya. Anda akan mempelajari lebih lanjut mengenai jenis-jenis _warning_ yang harus diperbaiki pada bagian selanjutnya. 
   <p align="center"><img width=40% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0219_Contoh_error_warning_yang_muncul.png"></p>
    <p align="center"><i>Contoh kesalahan (errors) dan peringatan (warnings) yang muncul pada saat validasi</i></p>

   Untuk kesalahan atau _Error_, Anda dapat langsung memperbaikinya secara otomatis dengan menekan pada bagian _Error_, kemudian tekan tombol **Fix**. Namun, untuk peringatan atau _warning_, Anda harus menyelesaikannya satu per satu. 
   <p align="center"><img width=40% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0220_Kesalahan_atau_errors_diselesaikan.png"></p>
<p align="center"><i>Kesalahan atau Errors dapat diselesaikan secara otomatis dengan menggunakan tombol Fix</i></p>

### IV. Jenis-jenis Kesalahan _(Error)_ dan Peringatan _(Warning)_ yang Harus Diperbaiki

Terdapat banyak sekali kesalahan dan peringatan yang muncul ketika Anda melakukan validasi data _OpenStreetMap_. Anda dapat menggunakan _tools_ yang terdapat di JOSM (modul **Menggunakan JOSM**) untuk memperbaiki kesalahan dan peringatan yang muncul pada alat validasi. Anda tidak perlu mengingat setiap jenis kesalahan dan peringatan yang muncul, namun Anda perlu mengetahui jenis-jenis kesalahan dan peringatan apa yang seringkali muncul serta mana yang harus Anda perbaiki, seperti:

1. Kesalahan _(Error)_
*   _Duplicated Node_ (Titik Terduplikasi)
        <br>Kesalahan ini biasanya muncul ketika sebuah objek secara tidak sengaja diunggah sebanyak 2 kali atau lebih sehingga menyebabkan adanya objek yang tumpang tindih pada posisi yang sama. Kesalahan ini biasanya terjadi ketika pengguna mengunggah data dengan menggunakan koneksi internet yang kurang stabil, sehingga menyebabkan adanya gangguan pada saat meng-_upload_ data. 
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0221_Error_duplicated_node.png"></p>
        <p align="center"><i>Error: Duplicated Node</i></p>

*   _Duplicated Ways_ (Garis Terduplikasi)
        <br>Kesalahan ini sama seperti kesalahan _duplicated node_, dimana terdapat dua atau lebih garis yang berada pada posisi yang sama. Kesalahan ini biasa terjadi pada objek jalan, namun seringkali juga terjadi pada objek bangunan yang bertumpuk pada satu tempat yang sama. Kesalahan ini juga disebabkan karena adanya objek yang terunggah sebanyak 2 kali dan disebabkan karena koneksi internet yang kurang stabil.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0222_Error_duplicated_ways.png"></p>
        <p align="center"><i>Error: Duplicated ways</i></p>


2. Peringatan _(Warning)_
*   _Crossing Building_ (Bangunan Bersinggungan)
        <br>Peringatan ini merupakan peringatan yang cukup sering muncul ketika melakukan validasi. Seringkali pengguna memetakan dua bangunan yang berbeda tetapi diletakkan secara bertumpuk. Untuk mengatasi _warning_ ini, Anda cukup memindahkan atau menghapus  salah satu bangunan yang bertumpukan.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0223_Warning_Crossing_building.png"></p>
        <p align="center"><i>Warning: Crossing building</i></p>   
        
*   _Crossing Ways_ (Garis Bersinggungan)
        <br>_Warning_ ini muncul ketika terdapat dua buah objek garis atau jalan yang digambar tanpa adanya titik perpotongan antar jalan. Untuk mengatasi _warning_ ini, Anda cukup menambahkan titik perpotongan yang terletak pada percabangan kedua jalan tersebut.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0224_Warning_Crossing_ways.png"></p>
        <p align="center"><i>Warning: Crossing ways</i></p>
    
*   _Overlapping Highways_ (Jalan saling bertumpang tindih)
        <br>_Warning_ ini muncul ketika terdapat bagian jalan yang bertumpukkan dengan bagian jalan lain. Untuk menyelesaikannya, Anda dapat menggeser atau menghapus bagian jalan yang bertumpukkan. 
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0225_Warning_Overlapping_highways.png"></p>
        <p align="center"><i>Warning: Overlapping highways</i></p>
    
*   _Node connect highways and building_ (Titik bangunan dan jalan saling terhubung)
        <br>_Warning_ ini muncul ketika titik objek bangunan dan titik objek jalan secara tidak sengaja saling terhubung satu sama lain. Untuk menyelesaikannya, silakan Anda pisahkan titik tersebut dengan menggunakan _tools **unglue node**_.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0226_Warning_Node_connect_higways_and_building.png"></p>
        <p align="center"><i>Warning: Node connect highways and building</i></p>
    
*   _Untagged ways_ (Objek belum diberi tag) 
        <br>_Untagged ways_ merupakan peringatan atau _warning_ yang  muncul disebabkan adanya objek yang belum diberi identitas atau _tag_. JOSM akan menandai objek tersebut sebagai objek tanpa identitas, mengingat pentingnya pemberian identitas atau atribut pada setiap objek yang dipetakan. Apabila Anda tetap mengabaikan peringatan ini, objek tersebut tetap dapat Anda _upload_ tetapi objek tersebut tidak akan muncul pada situs _OpenStreetMap_. Silakan Anda berikan _presets_ yang sesuai untuk objek yang belum diberikan informasi objek.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0227_Warning_Untagged_ways.png"></>
<p align="center"><i>Warning:Untagged ways</i></p>
    
*   _Way end node near other highways_ (titik tidak terhubung dengan garis terdekat)
        <br>_Warning_ ini muncul ketika ada titik dari objek jalan yang berdekatan dengan jalan lainnya namun tidak terhubung satu sama lain. Jika memang jalan tersebut merupakan jalan yang tidak dapat dilalui (jalan buntu) silakan gunakan tag **highway=block**. Namun jika ternyata jalan tersebut saling berhubungan, silakan Anda gabungkan jalan tersebut dengan menggunakan fungsi **Merge**.
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0228_Warning_Way_end_node_near_other_highways.png"></p>
        <p align="center"><i>Warning: Way end node near other highways</i></p>
    
*   _Building inside building_ (bangunan di dalam bangunan)
        <br>Peringatan atau _warning_ ini juga salah satu jenis _warning_ yang sering muncul ketika melakukan validasi. _Warning_ ini terjadi ketika ada poligon bangunan yang digambar di dalam poligon bangunan lain. Untuk menyelesaikannya, silakan Anda geser atau hapus salah satu bangunan yang ada di dalam poligon bangunan lain. 
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0229_Warning_Building_inside_building.png"></p>
        <p align="center"><i>Warning: Building inside building</i></p>
    
*   _Unnamed ways_ (Jalan belum diberi nama)
        <br>_Unnamed ways_ menandakan adanya jalan yang belum diberi nama. Jenis _warning_ ini dapat diabaikan, karena bisa saja ketika Anda melakukan pemetaan jarak jauh, Anda hanya memetakan objek jalannya saja tanpa mengetahui nama jalan tersebut. 
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0230_Warning_Unnamed_ways.png"></p>
        <p align="center"><i>Warning: Unnamed ways</i></p>
    
*   _Similarly named ways_ (Jalan memiliki nama yang sama)
        <br>_Warning_ ini muncul ketika ada beberapa jalan yang memiliki nama jalan yang hampir mirip. Sebagai contoh, ada jalan dengan nama Jalan Tebet Timur I, Jalan Tebet Timur IA, Jalan Tebet Timur IAA, dan sebagainya. Jenis _warning_ ini dapat Anda abaikan jika memang pada kenyataannya jalan tersebut memiliki nama jalan yang hampir serupa. 
<p align="center"><img width=50% src="/pages/04-Data-Validation-and-Quality-Assurance/02-Penggunaan-JOSM-untuk-Validasi-Data-Survei/images/0231_Warning_Similarly_named_ways.png"></p>
        <p align="center"><i>Warning: Similarly named ways</i></p>


**RINGKASAN**
<br>Data _OpenStreetMap_ yang memiliki sifat data terbuka menyebabkan data _OpenStreetMap_ rawan mengalami kerusakan oleh orang yang kurang bertanggung jawab. Oleh karena itu, setiap relawan pemetaan yang memasukkan data OSM sangat penting untuk menjaga kualitas data OSM yaitu dengan melakukan validasi data. Dengan mempelajari bagian ini, Anda telah dapat melakukan pengecekan kualitas data baik data hasil survei maupun data yang telah dimasukkan ke dalam server _OpenStreetMap_ menggunakan alat validasi yang ada di dalam JOSM. Anda juga telah mengetahui jenis-jenis kesalahan _(error)_ dan peringatan _(warning)_ yang sering muncul ketika melakukan validasi. Setelah mempelajari modul ini, Anda diharapkan dapat memahami pentingnya menjaga kualitas data yang ada di _OpenStreetMap_. 

