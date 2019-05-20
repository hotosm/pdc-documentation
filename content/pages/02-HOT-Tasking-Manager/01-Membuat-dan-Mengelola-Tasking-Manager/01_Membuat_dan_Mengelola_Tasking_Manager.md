---
title: Membuat dan Mengelola Tasking Manager
weight: 1
---


**Tujuan Pembelajaran:**

*   Menjelaskan fungsi dari _Tasking Manager_ dalam Konteks Pemetaan Partisipatif
*   Mengoperasikan cara membuat _Tasking Manager_
*   Mengoperasikan cara mengatur _Tasking manager_ yang sudah ada

Anda tentunya sudah mengetahui bagaimana cara menggunakan _tasking manager_ untuk melakukan kegiatan pemetaan secara bersama-sama. Ketika Anda menggunakan *tasking manager* yang tidak sesuai dengan wilayah yang Anda inginkan, maka Anda ingin membuat *tasking manager* untuk wilayah Anda sendiri. Pada modul ini, Anda akan mempelajari bagaimana cara membuat *tasking manager*. Pembuatan *tasking manager* membutuhkan orang yang bertanggung jawab atas *tasking* tersebut, agar data OSM yang dihasilkan memiliki kualitas data yang baik. Juga hal ini dikarenakan awal dibuatnya *tasking manager* untuk keperluan pemetaan sebagai respon kebencanaan di suatu wilayah.


## I. Apa itu Tasking Manager

### a. Definisi _Tasking Manager_

_Tasking Manager_ merupakan sebuah alat yang dibuat secara khusus untuk melakukan pemetaan secara kolaboratif dan partisipatif. _Tasking Manager_ memungkinkan Anda untuk melakukan pemetaan di suatu wilayah secara bersama-sama dengan pengguna OSM yang lain dengan  membagi-bagi  area pemetaan di wilayah tersebut. Tujuan _Tasking Manager_ adalah untuk membagi pekerjaan pemetaan ke dalam beberapa _grid_ /kotak yang berbeda sehingga setiap orang dapat memilih _grid_/kotak untuk dikerjakan. Selain itu, _Tasking Manager_ juga dapat memudahkan Anda dalam memantau progres pemetaan sehingga Anda dapat mengetahui wilayah mana yang masih butuh dipetakan dan wilayah mana yang sudah selesai dipetakan.

Bayangkan jika Anda ingin melakukan pemetaan pada suatu wilayah tertentu dimana Anda harus memetakan secara bersama-sama dengan 20 orang lainnya. Jika tidak ada pembagian tugas dan wilayah, maka akan ada kemungkinan beberapa orang memetakan di wilayah yang sama. Dengan adanya _Tasking Manager_, hal seperti ini dapat dihindari dan pekerjaan pemetaan akan dapat diselesaikan secara lebih cepat dan efektif. 

### b. Contoh Penggunaan _Tasking Manager_

_Tasking Manager_ pernah digunakan sebagai bentuk respon ketika bencana Topan Haiyan terjadi di Filipina pada 8 November 2013. Pemetaan menggunakan _Tasking Manager_ dilakukan di Kota Tacloban, salah satu kota yang terdampak sangat parah ketika bencana terjadi. Dalam kurun waktu 24 jam setelah dibuatnya proyek _Tasking Manager_, sebanyak 10.000 bangunan telah terpetakan atau sekitar 25% dari total jumlah bangunan yang ada di Kota Tacloban. Seluruh pemetaan ini dilakukan oleh 33 orang relawan. 

![Kondisi bangunan sebelum dan setelah dipetakan dengan Tasking Manager](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0101_tasking_manager.png "Kondisi bangunan sebelum dan setelah dipetakan dengan Tasking Manager")
<p align="center"><i>Kondisi bangunan sebelum dan setelah dipetakan dengan Tasking Manager</i></p>


Di Indonesia, penggunaan *Tasking Manager* juga digunakan untuk respon ketika bencana terjadi. Salah satu contohnya adalah ketika bencana gempa dan tsunami terjadi di Selat Sunda pada Desember 2018. Dalam kurun waktu 1 bulan, seluruh daerah terdampak sudah selesai dipetakan oleh sekitar 60 orang. 

![Tasking Manager yang dibuat sebagai respon bencana di Selat Sunda](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0102_respon_bencana_di_selat_sunda.png "Tasking Manager yang dibuat sebagai respon bencana di Selat Sunda")
<p align="center"><i>Tasking Manager yang dibuat sebagai respon bencana di Selat Sunda</i></p>


## II. Membuat Proyek *Tasking* Baru


Untuk dapat membuat _tasking_ baru di _tasking manager,_ Anda harus terlebih dahulu mempunyai  akses sebagai _project manager_. Apabila Anda belum memiliki akses maka anda harus diatur sebagai manager proyek agar dapat membuat tasking, Anda bisa mengajukan akses tersebut dengan mengirim _e-mail_ ke [team.id@hotosm.org](mailto:team.id@hotosm.org) untuk _tasking manager_ khusus di Indonesia. Setelah Anda berhasil mendapatkan akses untuk membuat tasking, Anda dapat melihat pada bagian kanan atas dari halaman depan tasking dan mengklik tombol **_Create New Project_.** 

![Memulai membuat proyek baru di tasking manager](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0103_membuat_proyek_baru_di_tasking_manager.png"Memulai membuat proyek baru di tasking manager")
<p align="center"><i>Memulai membuat proyek baru di tasking manager</i></p>

Ada beberapa tahapan yang harus dilakukan dalam membuat tasking:


### a.  Penentuan Wilayah Kerja

*   **Step 1: _Define Area_** = mengatur area kerja

    Setelah Anda menekan tombol **_Create New Project_**, Anda akan diarahkan pada halaman pengaturan pertama, yaitu mengatur area proyek pemetaan Anda. Terdapat dua cara dalam mengatur area proyek pemetaan:

    *   **_Draw_**= dengan menggambar secara bebas area yang Anda inginkan 
    *   **_Import_**= dengan menggunakan data spasial yang berformat _GeoJSON, KML, OSM_ atau _SHP_ yang terkompresi dalam bentuk _zip_.

    Klik **_Next_** apabila Anda sudah selesai mengatur area kerja Anda.

![Pilihan mengatur area kerja](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0104_pilihan_mengatur_area_kerja.png"Pilihan mengatur area kerja")
<p align="center"><i>Pilihan mengatur area kerja</i></p>
 

*   **Step 2: _Choose Tasks Step_** = mengatur tipe pembagian area kerja

    Setelah Anda sudah mengatur area kerja, tahapan berikutnya adalah Anda diminta untuk mengatur bentuk pembagian area kerja. Terdapat dua tipe pembagian area kerja: kotak (**_Square Grid_**) dan bebas (**_Arbitary Tasks_**). Jika memilih bentuk kotak, area kerja Anda akan dibagi menjadi beberapa kotak persegi dengan ukuran yang sama. Sementara itu apabila Anda memilih bentuk bebas. Area kerja Anda akan dibagi menjadi beberapa ukuran acak. Klik **Next** untuk menuju tahapan berikutnya.

![Pilihan mengatur tipe pembagian area kerja](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0105_pilihan_mengatur_tipe_pembagian_area_kerja.png"Pilihan mengatur tipe pembagian area kerja")
<p align="center"><i>Pilihan mengatur tipe pembagian area kerja</i></p>

*   **Step 3: _Set Task Sizes_** = Mengatur besar luasan kotak kerja

    Pada tahapan ini, Anda akan mengatur besar luasan kotak kerja. Diasumsikan bahwa pada tahapan sebelumnya Anda memilih pembagian area kerja dalam bentuk kotak dan pada tahapan ini Anda akan menentukan jumlah kotak yang ada di dalam area yang Anda tentukan. Semakin besar ukuran kotak kerja, maka jumlah pembagi kotak kerja akan lebih sedikit. Namun hal tersebut juga berarti para relawan pemetaan yang ikut memetakan area Anda bisa jadi mendapatkan pembagian luas wilayah yang sangat besar dan begitu juga sebaliknya.

![Deskripsi alat-alat pada tahapan pengaturan kotak kerja](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0106_alat_pada_tahapan_pengaturan_kotak_kerja.png"Deskripsi alat-alat pada tahapan pengaturan kotak kerja")
<p align="center"><i>Deskripsi alat-alat pada tahapan pengaturan kotak kerja</i></p>
   
>Catatan:
>Sedikit tips dalam menentukan luasan kotak kerja, Anda tentunya menginginkan membuat kotak kerja yang tidak terlalu besar dan tidak terlalu kecil. Untuk menentukannya Anda bisa melihatnya melalui kepadatan jaringan jalan yang terlihat pada area pemetaan Anda, dengan menggunakan citra satelit Bing atau Mapbox. Apabila Anda melihat kotak yang berisikan daerah padat, Anda bisa membagi kotak tersebut ke dalam beberapa kotak kecil dengan menggunakan tombol Split (Polygon) atau Split (Point).


*   **Step 4: _Trim Project_**= Memotong kotak kerja yang tidak dibutuhkan

    Setelah Anda mengatur besaran kotak kerja, pada tahapan selanjutnya Anda akan diarahkan untuk memotong kotak kerja hanya spesifik ke area proyek Anda saja. Dengan menggunakan fitur ini, Anda bisa menghapus kotak kerja yang berada di luar area kotak kerja dan menyisakan kotak kerja yang sesuai dengan area batas proyek kerja Anda. Lama tidaknya proses memotong kotak ini tergantung dari besar luasan proyek kerja Anda.

![Menggunakan trim untuk memotong area kerja](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0107_menggunakan_trim_untuk_memotong_area_kerja.png"Menggunakan trim untuk memotong area kerja")
<p align="center"><i>Menggunakan trim untuk memotong area kerja</i></p>


*   **Step 5: _Review_**=Memberikan nama proyek

    Tahapan selanjutnya adalah Anda memberikan nama untuk proyek  pemetaan Anda. Pada tahapan ini sebaiknya Anda memberikan nama yang mudah untuk dicari oleh para pengguna lainnya. Pada bagian ini juga terdapat keterangan jumlah _grid_/kotak yang akan Anda kerjakan, seperti gambar di bawah ini ada 56 _grid_/kotak. Klik **_Create_** untuk membuat proyek _tasking manager_ Anda.

![Tahapan akhir sebelum proyek dibuat](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0108_tahapan_akhir_sebelum_proyek_dibuat.png"Tahapan akhir sebelum proyek dibuat")
<p align="center"><i>Tahapan akhir sebelum proyek dibuat</i></p>


### b. Pengaturan Deskripsi Proyek 
Setelah selesai membuat proyek, Anda akan diarahkan ke pengaturan tambahan dimana Anda akan memasukkan deskripsi proyek, instruksi, area prioritas, dsb. Anda harus memasukkan deskripsi proyek dan instruksi data yang dipetakan, sementara yang lainnya adalah opsional.

*   **Description**= Memberikan deskripsi proyek

    Ada beberapa hal yang Anda lakukan pada bagian ini. 
    1. Anda akan mengatur status proyek _tasking_ Anda (**_Draft, Published, Archived_**). Status **_Draft_** merupakan pengaturan bawaan saat pertama kali proyek berhasil dibuat. Apabila sebuah proyek _tasking_ masih berstatus _draft_, para relawan pemetaan tidak akan dapat ikut membantu memetakan proyek _tasking_ Anda. Status **_Published_** berarti proyek _tasking_ Anda sudah dipublikasikan sehingga orang lain dapat melihat dan ikut membantu memetakan _tasking_ Anda. Status **_Archived_** berarti proyek tasking Anda sudah diarsipkan karena sudah selesai atau ada proyek _tasking_ baru dengan area yang sama. Pilih **_Published_** agar para sukarelawan dan tim Anda bisa melihat _tasking_ Anda.
    2. Anda akan mengatur prioritas _tasking_ Anda. Pada _tasking manager_, Anda akan diberikan tiga pilihan prioritas yaitu mendesak, tinggi, sedang, dan rendah dimana masing-masing tingkat memiliki arti yang berbeda-beda. Anda bisa mengatur _tasking_ Anda ke dalam tingkat mendesak/**_urgent_** apabila proyek _tasking_ yang dibuat oleh Anda bertujuan untuk segera dipetakan seperti pemetaan respon saat bencana terjadi sehingga proyek _tasking_ Anda akan ditampilkan pada urutan teratas di daftar _tasking_. Atur prioritas ke tingkat tinggi/**_high_** apabila kegiatan pemetaan Anda merupakan kegiatan pemetaan untuk respon kebencanaan namun bencana tersebut telah melewati fase tanggap darurat. Atur prioritas ke sedang/**_medium_** apabila proyek pemetaan Anda tidak terlalu mendesak untuk dipetakan namun termasuk kedalam lingkup pemetaan untuk kebencanaan. Atur prioritas ke rendah/**_low_** apabila kegiatan proyek _tasking_ Anda tidak mendesak dan bukan merupakan kegiatan untuk pemetaan kebencanaan.
    3. Anda akan mengatur ringkasan (**_Short description_**) dan deskripsi dari _tasking manager_ Anda. Dalam memberikan ringkasan (_short description)_ dan deskripsi untuk tasking Anda, terdapat pilihan bahasa dari bahasa Inggris (**EN**) dan Indonesia (**ID**). Pilihan bahasa tersebut akan muncul saat pengguna mengubah bahasa situs _tasking manager_ ke bahasa yang mereka inginkan. Apabila Anda ingin memasukkan bahasa Indonesia saja, pilih **ID** sebagai pilihan bahasa dan kemudian isi deskripsi singkat dan deskripsinya dalam format _markdown_. _Markdown_ merupakan format yang sama dengan format _html _dengan penulisan yang lebih sederhana. Untuk panduan penulisan dengan format _markdown_, Anda bisa melihatnya di situs _Markdown Guide_[^1]_._

![Penjelasan untuk Bagian Deskripsi Proyek Pemetaan Anda](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0109_penjelasan_deskripsi_proyek_pemetaan_anda.png"Penjelasan untuk Bagian Deskripsi Proyek Pemetaan Anda")
<p align="center"><i>Penjelasan untuk Bagian Deskripsi Proyek Pemetaan Anda</i></p>

*   **_Instructions_**= Memberikan instruksi pemetaan

    Pada bagian ini Anda akan memberikan informasi mengenai objek apa saja yang harus dipetakan pada _Tasking Manager_ yang telah Anda buat. 

    1. Pada bagian **_Entitles to map_** Anda bisa menjabarkan obyek apa saja yang Anda butuhkan dari proyek _tasking_ ini. Misalnya Anda membutuhkan data jaringan jalan, bangunan dan sungai. Maka pada bagian ini, Anda bisa menjabarkan tentang obyek-obyek tersebut. 
    2. Pada bagian **_Changeset comment_** Anda bisa mengatur komen _changeset_ bawaan yang akan muncul otomatis pada saat pengguna  akan mengunggah penambahan data mereka ke _OpenStreetMap_.
    3. Pada bagian **_Detailed Instruction_** Anda bisa memasukkan instruksi pemetaan secara detail. Penjelasan ini sangat membantu relawan yang ingin berkontribusi dalam proyek _tasking_ Anda tetapi belum memiliki pengalaman pemetaan baik di _Tasking Manager_ maupun di OpenStreetMap. Anda bisa memberikan instruksi yang sedetail mungkin pada bagian ini. 

![Tampilan pada bagian instruksi](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0110_tampilan_pada_bagian_instruksi.png"Tampilan pada bagian instruksi")
<p align="center"><i>Tampilan pada bagian instruksi</i></p>

*   **_Metadata_**= Mengeset metadata proyek (opsional)
    1. **Mapper Level.**
    Pada bagian ini, Anda bisa mengatur tingkat kesulitan proyek pemetaan dan mengaturnya berdasarkan persepsi Anda sendiri. Sebagai contoh apabila daerah yang dipetakan merupakan daerah pemukiman padat penduduk dengan kondisi citra satelit yang tidak terlalu baik dan kebutuhan data yang dipetakan adalah data bangunan umum, Anda bisa mengatur tingkat kesulitan untuk memetakan daerah tersebut  termasuk tinggi atau sedang.

    1. **Type(s) of Mapping.**
    Anda bisa mengidentifikasi obyek yang akan dipetakan pada proyek tasking Anda dengan memberikan centang pada daftar obyek yang ada di bagian **_Type(s) of Mapping_**. 

    1. **Organization Tag.**
     Pada bagian ini Anda bisa memberikan _tag_ organisasi Anda untuk memudahkan pencarian proyek _tasking_ pada kolom pencarian.

    2. **Campaign Tag.**
    Sama seperti _organization tag_ pada bagian ini Anda bisa menambahkan _tag_ yang sesuai dengan proyek pemetaan Anda agar memudahkan pencarian.

![Tampilan halaman metadata](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0111_tampilan_halaman_metadata.png"Tampilan halaman metadata")
<p align="center"><i>Tampilan halaman metadata</i></p>


*   **Priority Areas** = Mengatur area prioritas (opsional)
    Pada menu ini Anda bisa menggambar area prioritas untuk proyek _tasking _Anda dengan beberapa cara:
    1. Menggambar area dengan menggunakan tombol _**DRAW POLYGON**_
    2. Menggambar area berbentuk kotak dengan menggunakan tombol **_DRAW RECTANGLE_**
    3. Menggambar lingkaran dengan menggunakan tombol **_DRAW CIRCLE_**
    4. Mengubah area prioritas yang sudah digambar dengan menggunakan tombol **_EDIT_**
    5. Menghapus area prioritas dengan menggunakan tombol **_DELETE_,** dan
    6. Menghapus semua area prioritas dengan menggunakan tombol **_CLEAR ALL_**

![Tampilan halaman Priority Areas](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0112_tampilan_halaman_priority_areas.png"Tampilan halaman Priority Areas")
<p align="center"><i>Tampilan halaman Priority Areas</i></p>

*   **_Imagery_** = Memberikan citra satelit tambahan (opsional)
    Apabila Anda mempunyai citra satelit tambahan dalam format TMS (_Tile Map Service_). Anda bisa memasukkan _url_ nya di bagian ini. Selain itu Anda juga perlu mengatur lisensi dari citra satelit yang anda gunakan. Anda harus memastikan citra satelit yang Anda gunakan mempunyai lisensi yang dapat digunakan untuk pemetaan di OpenStreetMap.

![Tampilan halaman Imagery](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0113_tampilan_halaman_imagery.png"Tampilan halaman Imagery")
<p align="center"><i>Tampilan halaman Imagery</i></p>

*   **_Permissions_** = Mengatur tingkat izin proyek (opsional)
    Pada bagian ini Anda bisa mengatur tasking proyek Anda hanya dapat diakses oleh pengguna dengan tingkat skill mulai dari tingkat pemula sampai mahir. Dengan mengaktifkan fitur **_Mapper Level_**, proyek tasking Anda hanya bisa dikerjakan oleh pengguna dengan tingkat yang telah Anda tentukan.

    Apabila Anda mengaktifkan **_Validator Level_** maka pengguna yang bisa mengakses tasking Anda untuk melakukan validasi data adalah pengguna dengan tingkat level _validator_.

    Apabila Anda mengaktifkan **_Private Project_** maka tasking Anda hanya akan bisa diakses oleh pengguna yang namanya (_user_ OSM) sudah Anda tentukan sebelumnya. Orang lain diluar nama yang telah diatur tidak dapat melihat tasking yang dibuat oleh Anda.

![Tampilan halaman Permissions](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0114_tampilan_halaman_permissions.png"Tampilan halaman Permissions")
<p align="center"><i>Tampilan halaman Permissions</i></p>

Setelah selesai dengan pengaturan tambahan. Anda bisa menyimpan proyek _tasking_ Anda dengan mengklik tombol **SAVE CHANGES** yang ada pada bagian bawah.

![Klik tombol untuk menyimpan proyek tasking yang sudah diubah](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0115_menyimpan_proyek_tasking_yang_sudah_diubah.png "Klik tombol untuk menyimpan proyek tasking yang sudah diubah")
<p align="center"><i>Klik tombol untuk menyimpan proyek tasking yang sudah diubah</i></p>

## III. Pengelolaan Proyek *Tasking*

### a. Mengubah Instruksi dan Deskripsi

  Jika Anda ingin menambahkan beberapa kalimat instruksi baru atau ingin mengubah deskripsi proyek Anda seiring dengan berjalannya waktu pemetaan di _tasking_ Anda, Anda bisa memilih tombol **_Edit Project_** pada halaman _tasking_ tersebut . Setelah itu Anda bisa langsung merubah deskripsi dan instruksi untuk tasking Anda.

![Klik tombol EDIT PROJECT untuk mengubah deskripsi proyek tasking Anda](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0116_edit_project_mengubah_deskripsi_proyek_tasking_anda.png "Klik tombol EDIT PROJECT untuk mengubah deskripsi proyek tasking Anda")
<p align="center"><i>Klik tombol EDIT PROJECT untuk mengubah deskripsi proyek tasking Anda</i></p>

### b. Validasi Hasil Kerja

  Seiring dengan berjalannya proyek tasking Anda dan bertambahnya data di daerah yang sedang Anda kerjakan, beberapa relawan mungkin ada yang belum mahir melakukan digitasi dengan OSM sehingga Anda membutuhkan kegiatan validasi untuk memperbaiki data. Untuk lebih jelasnya, Anda bisa membaca modul **Penjaminan Kualitas Data dengan _Tasking Manager_**. Silahkan klik tombol **_Validate_** untuk beralih ke halaman validasi untuk proyek tasking Anda.

![Halaman validasi pada tasking manager](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0117_halaman_validasi_pada_tasking_manager.png"Halaman validasi pada tasking manager")
<p align="center"><i>Halaman validasi pada tasking manager</i></p>


Terdapat 5 opsi pada halaman validasi hasil di _tasking manager_:

* Memilih sendiri kotak pada peta. Dengan cara ini Anda tinggal memilih kotak yang tersedia pada peta untuk memulai validasi.
* Memilih kotak secara acak. Dengan cara ini Anda akan dibantu untuk memilih kotak oleh _tasking manager_.
* Memilih kotak dengan menggambar _polygon_. Dengan menggunakan fitur ini. Anda bisa memilih beberapa kotak untuk divalidasi dengan menggambar sebuah _polygon_ atau area.
* Memilih kotak yang sudah terkunci sebelumnya. Apabila Anda sudah mendapatkan kotak untuk divalidasi tetapi tidak ingat telah memilih kotak tersebut, Anda bisa menggunakan fitur ini. Dengan mengklik tombol ini, Anda akan diarahkan ke kotak yang telah dipilih sebelumnya.
* Memilih sesuai dengan nama pengguna. Anda juga dapat melakukan validasi pada sebuah kotak dengan memilih berdasarkan nama pengguna yang ikut serta untuk memetakan di proyek tasking Anda.
    
### c. Mengubah Area Prioritas

  Anda bisa menentukan area prioritas untuk dipetakan terlebih dahulu. Caranya adalah dengan mengklik **_Edit Project_** terlebih dahulu dan setelah itu Anda menuju ke menu **_Priority areas._** Silahkan ubah dan tambahkan area prioritas Anda dengan menggunakan cara yang sudah dijelaskan pada bagian sebelumnya.

### d. Beberapa Fitur Aksi di _Tasking Manager_

Pada menu pengelolaan _tasking manager_ Anda, terdapat beberapa tombol aksi:

*   Mengirim pesan ke para kontributor proyek tasking Anda. Dengan menggunakan tombol _**Message All Contributors**_ Anda bisa mengirim pesan yang akan terbaca oleh semua kontributor proyek tasking Anda. Hal ini tentunya sangat berguna apabila terdapat perubahan pada obyek yang dipetakan atau perubahan area prioritas.
*   Mengatur semua tasking secara serentak. Terdapat alat yang bisa Anda gunakan untuk mengatur semua tasking secara serentak. 
    *   **_Map All Tasks_** digunakan untuk menandakan bahwa semua kotak pada tasking Anda sudah terpetakan semua.
    *   **_Invalidate All Tasks_** digunakan untuk membatalkan semua kotak yang sudah tervalidasi
    *   **_Validate All Tasks_** digunakan untuk mengesahkan semua kotak yang sudah terpetakan
    *   **_Reset All Bad Imagery Tasks_** digunakan untuk mengatur ulang semua kotak yang memiliki keterangan bahwa citra satelit pada kotak tersebut tidak bisa digunakan.
*   Menghapus proyek tasking. Dengan menggunakan tombol **_Delete Project_** Anda bisa langsung menghapus proyek tasking Anda dengan catatan bahwa belum ada kontributor yang berpartisipasi dalam tasking Anda
*   Mengatur ulang proyek tasking. Dengan tombol **_Reset Tasks_** Anda akan mengatur ulang tasking Anda tetapi masih dapat menyimpan histori kontributor yang ikut turut serta memetakan proyek tasking Anda.
*   Menduplikasi tasking. Dengan tombol **_Clone Project_** Anda bisa menduplikasi tasking Anda dan membuat tasking baru dengan deskripsi dan area kerja yang sama seperti tasking sebelumnya. Hal yang berbeda adalah proyek _tasking_ hasil duplikasi Anda akan dalam status _Draft_ dan untuk bagian area yang ingin dipetakan, jumlah kotak dan area prioritas tidak akan terduplikasi sehingga Anda harus melakukan pengaturan lebih lanjut.

![Tampilan fitur-fitur yang terdapat pada halaman Action](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0118_tampilan_fitur-fitur_yang_terdapat_pada_halaman_action.png"Tampilan fitur-fitur yang terdapat pada halaman Action")
<p align="center"><i>Tampilan fitur-fitur yang terdapat pada halaman Action</i></p>

### e. Mengarsip Proyek Tasking

  Apabila proyek tasking sudah selesai, Anda disarankan untuk mengarsipkan proyek tasking yang telah Anda buat. Hal ini bertujuan untuk menghindari kontributor untuk melakukan pemetaan pada proyek _tasking_ tersebut. Untuk mengarsip proyek tasking , klik **_Edit Project_** dan pilih menu **_Description_.** Pada menu status, ubah dari **_Published_** ke **_Archived_**. Klik **_Save Changes_** untuk menyimpan perubahannya.

![Mengubah status proyek dari Published ke Archived](/pages/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/images/0119_mengubah_status_proyek_dari_published_ke_archived.png"Mengubah status proyek dari Published ke Archived")
<p align="center"><i>Mengubah status proyek dari Published ke Archived</i></p>

## RINGKASAN

Selamat! Saat ini Anda telah berhasil mempelajari cara membuat dan mengelola proyek pada _tasking manager_. Dengan menggunakan _tasking manager_, proyek pemetaan Anda akan menjadi lebih teratur. Hal yang harus diperhatikan, ketika Anda membuat _tasking manager_, proyek tersebut harus diselesaikan dan diperhatikan tidak hanya kuantitas data tetapi juga kualitas data. 





[^1]:

    https://www.markdownguide.org/basic-syntax




