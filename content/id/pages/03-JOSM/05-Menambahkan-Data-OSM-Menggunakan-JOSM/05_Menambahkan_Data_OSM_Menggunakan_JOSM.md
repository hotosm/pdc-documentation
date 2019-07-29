---
title: Menambahkan Data Hasil Survei ke OSM Menggunakan JOSM
weight: 5
---

**Tujuan Pembelajaran:**



*   Mampu menerapkan cara menginstal _plugin Utilsplugin2_
*   Mampu menerapkan cara menggabungkan data hasil survei
*   Mampu menerapkan cara menyimpan _file_ di JOSM
*   Mampu menerapkan cara men-_download_ data _OpenStreetMap_
*   Mampu menerapkan cara memunculkan citra satelit di JOSM
*   Mampu menerapkan, menambahkan dan mengubah data OSM menggunakan JOSM
*   Mampu menerapkan cara meng-_upload_ perubahan ke OSM
*   Mampu menerapkan cara melihat perubahan data OSM di situs OSM

Data OSM dapat diperkaya dengan cara menambahkan atau memetakan objek di OSM. Namun, jika Anda menambahkan data OSM menggunakan citra satelit saja sebagai acuannya, maka informasi objek yang Anda tambahkan tentu terbatas sekali. Survei lapangan dapat membantu Anda dalam melengkapi informasi objek yang dipetakan. Anda dapat mempelajari alat pengumpulan data pada modul **Metodologi Pengumpulan Data**. Untuk menambahkan data OSM, Anda memerlukan editor data OSM. Banyak sekali editor data OSM yang tersedia, namun pada modul ini editor data OSM yang digunakan adalah JOSM. JOSM menyediakan banyak alat serta _plugin_ yang memudahkan pengguna dalam menambahkan atau mengedit data OSM.

### **I. Menginstal _plugin Utilsplugin2_**

Sebelum menambahkan atau mengedit data OSM menggunakan JOSM, instal _plugin_ yang akan digunakan terlebih dahulu. JOSM memiliki _plugin_ yang salah satu fungsinya memudahkan Anda untuk menyalin _preset/tag_ yaitu _plugin_ _**utilsplugin2**_. Anda harus menginstal _plugin_ ini terlebih dahulu. Langkah-langkah untuk menginstal _plugin utilsplugin2_ yaitu:

*   Buka **JOSM**
*   Klik menu **_Edit → Preferences_**
*   Pilih menu **_Plugins_** (ikon steker) untuk menginstal _plugin_ baru. Jika daftar _plugins_ belum muncul, Anda dapat mengklik **_Download List_** namun pastikan komputer/laptop Anda terkoneksi internet.
*   Setelah men-_download plugin_, cari _plugin **utlisplugin2**_ dengan menuliskannya pada kolom **_Search_**. Setelah berhasil menemukan _plugin **utilsplugin2**_, silakan **centang** kotak _plugin **utilsplugin2**_ untuk menginstal _plugin_ tersebut.

![installasi_utilsplugin2](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0501_utilsplugin.png)
<p align="center"><i>Melakukan instalasi plugin utilsplugin2</i></p>

*   Setelah itu klik **_OK_** dan tunggu hingga proses instalasi selesai. Jika sudah berhasil diinstal, akan muncul menu **_More tools_**.

![tampilan_menu_more_tools](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0502_menu_more_tools.png)
<p align="center"><i>Tampilan menu More tools pada JOSM</i></p>

>Catatan :
Terkadang JOSM meminta Anda untuk melakukan _Restart_ setelah melakukan instalasi _plugin_ baru untuk mengaplikasikan _plugin_ yang baru saja diinstal. Namun, tidak semua _plugin_ membutuhkan _Restart_ untuk dapat digunakan setelah instalasi.

### **II. Menggabungkan Data Survei**

Jika Anda sudah melakukan survei menggunakan alat pengumpulan data seperti _ODK Collect_ dan _OpenMapKit_, Anda dapat menggunakan data hasil survei tersebut sebagai acuan menambahkan informasi objek di OSM. Data hasil survei yang didapatkan dari _ODK Collect_ dan _OpenMapKit_ formatnya adalah _.osm_. Banyaknya _file .osm_ hasil survei dari _ODK Collect_ dan _OpenMapKit_ sama dengan banyaknya objek yang disurvei karena informasi satu objek disimpan pada satu _file .osm_. Untuk memudahkan Anda menggunakan data hasil survei untuk menambahkan informasi objek, gabungkan seluruh _file .osm_ dengan cara:



*   Arahkan **_File Explorer_** ke direktori tempat penyimpanan _file_ hasil survei dari **_ODK Collect_** dan _**OpenMapKit**_.

![tampilan_direktori_penyimpanan_file](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0503_direktori_file_odk.png)
<p align="center"><i>Tampilan direktori penyimpanan file hasil survei menggunakan ODK Collect</i></p>

*   Cari semua _file .osm_ dengan cara ketikkan **osm** pada kolom _**Search**_. Pilih semua _file .osm_ dari hasil pencarian.

![tampilan_hasil_pencarian](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0504_pencarian_direktori.png)
<p align="center"><i>Tampilan hasil pencarian pada direktori penyimpanan file hasil survei</i></p>

*   Tarik semua _file .osm_ yang sudah dipilih ke **JOSM**.

![tampilan_layer](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0505_layer_josm.png)
<p align="center"><i>Tampilan layer setelah dimasukkan data hasil survei menggunakan ODK dan OMK</i></p>

*   Pilih semua _layer file_ hasil survei dengan cara **pilih _layer_ hasil survei yang paling atas, tekan _Shift_, pilih _layer_ hasil survei yang paling bawah**
*   **Klik kanan pada _layer_ hasil survei**, lalu klik **_Merge_**. Setelah itu muncul jendela **_Select target layer_**, Anda tidak perlu mengubah target _layer_ nya lalu klik **_Merge_**.

![menggabungkan_hasil_survei](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0506_merge_layer.png)
<p align="center"><i>Menggabungkan layer hasil survei</i></p>

*   Simpan dan ubah nama _layer_ hasil gabungan seluruh data survei dengan cara **klik kanan pada _layer_ hasil gabungan**, pilih **_Save As_**, ubah nama _file_ nya dan kemudian klik **_Save_**.

![menyimpan_layer](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0507_menyimpan_layer.png)
<p align="center"><i>Menyimpan layer hasil survei yang sudah digabungkan</i></p>

*   Untuk memudahkan Anda menandai objek-objek yang sudah dipetakan atau belum dari _layer_ hasil survei, JOSM menyediakan _plugin_ _**to-do**_ cara instalasi dan penggunaan secara detailnya dapat dibaca pada modul **Menggunakan to-do list di JOSM**. Jika _plugin_ _**to-do list**_ sudah diinstal dan kotak jendela _**Todo list**_ sudah diaktifkan, pilih semua titik objek yang ada di _layer_ hasil survei yang sudah digabungkan menggunakan ikon _**Select object**_, kemudian pada kotak jendela Todo list klik **_Add_**.

![memasukkan_hasil_objek](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0508_to_do_josm.png)
<p align="center"><i>Memasukkan objek hasil survei ke dalam Todo list</i></p>

### **III. Men-_download_ Data OSM**

Setelah berhasil menggabungkan data hasil survei, Anda perlu men-_download_ data OSM. Hal ini bertujuan agar dapat mengetahui data OSM yang sudah dipetakan oleh pengguna lainnya dan tersedia di dalam server OSM. Untuk men-_download_ data OSM caranya adalah:

*   Klik menu **_File → Download Data_**
*   Akan muncul jendela **_Download_** yang secara _default_ menampilkan tab _**Slippy Map**_

![jendela_download_data](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0509_jendela_download.png)
<p align="center"><i>Tampilan jendela Download Data OSM</i></p>

*   Jika peta belum menampilkan wilayah pemetaan Anda, geser peta dengan cara **klik kanan tahan** _mouse_ Anda dan **geser/arahkan** ke wilayah pemetaan Anda. Kemudian gambar kotak wilayah pemetaan Anda dengan cara **klik kiri tahan dan geserkan** hingga membentuk **kotak warna merah muda** yang meliputi seluruh wilayah pemetaan Anda. Setelah itu klik **_Download_**.
*   Jika wilayah pemetaan Anda cukup sulit mencarinya dengan cara menggeser peta, Anda dapat memilih tab **_Areas around places_** dan ketik nama wilayah pemetaan Anda di kolom **_Enter a place name to search for_** lalu klik **_Search_**. Setelah itu akan muncul nama wilayah yang Anda cari, **klik salah satu namanya** lalu silakan **kembali lagi ke tab _Slippy Map_**. Peta di tab **_Slippy Map_** akan menampilkan wilayah yang tadi sudah Anda pilih. **Buatlah kotak** yang meliputi seluruh wilayah pemetaan Anda, lalu klik **_Download_**.

>Catatan :
Perhatikan banyaknya data OSM yang sudah ada di wilayah pemetaan Anda. Jika sudah cukup banyak sebaiknya Anda tidak langsung men-_download_ seluruh data OSM yang ada di wilayah pemetaan Anda karena JOSM tidak dapat men-_download_ data yang terlalu besar sekaligus. Untuk mengatasinya, Anda dapat men-_download_ data OSM di wilayah pemetaan Anda per bagian. 

![area_around_places](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0510_tab_areas_around_places.png)
<p align="center"><i>Tampilan tab “Areas around places” pada jendela Download</i></p>

*   Setelah berhasil men-_download_ data OSM pada wilayah pemetaan Anda, akan muncul _layer_ baru yang juga akan menjadi _layer_ area kerja Anda untuk menambahkan dan mengubah data OSM. Pastikan Anda hanya menambahkan data pada **kotak yang tidak diarsir** karena kotak yang diarsir sudah bukan wilayah yang Anda _download_. Pastikan seluruh area survei Anda data OSM nya sudah di-_download_. Seperti ini tampilannya:

![tampilan_josm](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0511_download_data_osm.png)
<p align="center"><i>Tampilan JOSM ketika sudah berhasil men-download data OSM</i></p>

*   Jika sudah berhasil men-_download_ data OSM di seluruh area survei Anda, gabungkan _layer_ data OSM hasil _download_ dengan _layer_ hasil survei yang sudah digabung pada subbab sebelumnya. Caranya **pilih kedua _layer_** tersebut kemudian **klik kanan**, pilih **_Merge_**. Simpan pada _layer_ hasil survei yang sudah digabung. Kemudian klik **_Merge_**.

![menggabungkan_layer_osm](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0512_menggabungkan_layer.png)
<p align="center"><i>Menggabungkan layer data OSM dengan data hasil survei</i></p>

### **IV. Menambahkan Citra Satelit**

*   Setelah berhasil men-_download_ data OSM, tambahkan citra satelit untuk acuan dalam memetakan dengan cara mengklik **_Imagery_ → pilih citra yang akan digunakan, misalnya _DigitalGlobe Premium Imagery_**. Setelah berhasil menambahkan citra satelit berarti Anda sudah siap untuk menambahkan data OSM. Tampilannya akan seperti ini:

![data_osm_dengan_citra](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0513_menambahkan_citra.png)
<p align="center"><i>Tampilan data OSM yang sudah ditambahkan citra satelit</i></p>

*   Anda juga dapat mengatur tampilan citra satelit yang Anda gunakan. Caranya, pilih _layer_ citra satelitnya kemudian klik pada ikon **_Change visibility of selected layer_** lalu ubah tampilannya sesuai keinginan Anda.

![mengubah_tampilan_citra](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0514_setting_citra.png)
<p align="center"><i>Mengubah tampilan citra satelit</i></p>

*   Terkadang citra satelit yang digunakan khususnya **_DigitalGlobe Premium Imagery_** memiliki perbedaan tampilan ketika di _zoom in_ dan _zoom out_ dan hanya salah satunya yang sesuai dengan data OSM nya. Agar tampilan citranya tidak berubah-ubah ketika di _zoom in_ atau _zoom out_, nonaktifkan fitur _**Auto zoom**_ dengan cara **klik kanan pada citra di kanvas kerja → klik _Auto zoom_** sehingga tanda centang pada **_Auto zoom_** hilang.

![menonaktifkan_auto_zoom](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0515_auto_zoom.png)
<p align="center"><i>Menonaktifkan Auto zoom pada citra satelit</i></p>

### **V. Mengedit dengan JOSM**

Setelah menginstal _plugin utilsplugin2_, menggabungkan data hasil survei, men-_download_ data OSM, serta memasukkan citra satelit, sekarang Anda sudah siap menambahkan/mengubah data OSM menggunakan JOSM. Anda dapat menggambar objek yang belum dipetakan atau mengubah objek yang sudah dipetakan menggunakan alat-alat yang sudah Anda pelajari pada modul **Menggunakan JOSM**. Berikut ini adalah cara mengedit data OSM menggunakan data hasil survei, data OSM dan citra satelit yang sudah dibuka sebelumnya di JOSM:

*   Setelah berhasil mengikuti langkah-langkah pada empat subbab sebelumnya, pada JOSM Anda akan terdapat dua _layer_ yang terbuka di JOSM yaitu **_layer_ citra satelit** (pada gambar adalah _layer DigitalGlobe Premium Imagery_) dan **_layer_ data hasil survei yang sudah digabungkan dengan data OSM yang di-_download_** (pada gambar adalah *layer hasil_survey_jakut.osm*). Tampilannya akan seperti ini:

![tampilan_josm](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0516_menambahkan_data_survei.png)
<p align="center"><i>Tampilan JOSM setelah dimasukkan data hasil survei dan citra satelit</i></p>

*   Agar Anda tidak mengubah batas administrasi yang sudah dipetakan pada OSM, Anda dapat menggunakan fitur **Filter** pada JOSM. Hal ini dikarenakan batas administrasi merupakan hal yang bersifat khusus dan tidak terkait dengan objek lainnya di dalam OSM. Untuk menggunakan fitur **Filter**, aktifkan kotak jendela Filter dengan cara klik menu **_Windows → Filter_**. Akan muncul kotak jendela Filter di sebelah kanan kanvas kerja Anda. Klik **_Add_** pada kotak jendela Filter, tuliskan _**boundary=administrative**_ pada kolom **Filter _string_** dan kemudian klik **_Submit Filter_**. Akan muncul sebuah filter baru untuk batas administrasi, untuk menonaktifkan filter Anda dapat menghilangkan tanda centang di sebelah filter. Untuk mengetahui lebih lanjut mengenai fitur **Filter** JOSM, Anda dapat mempelajari modul **Menggunakan Alat Filter di JOSM**.

![jendela_filter](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0517_jendela_filter.png)
<p align="center"><i>Tampilan kotak jendela Filter</i></p>

![mengisi_filter_string](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0518_mengisi_filter.png)
<p align="center"><i>Mengisi filter string pada jendela Filter</i></p>

![tampilan_kotak_filter](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0519_filter_sudah_diisi.png)
<p align="center"><i>Tampilan kotak jendela filter yang sudah ditambahkan sebuah filter</i></p>

*   Setelah itu, mulai lakukan pemetaan dengan perbesar ke sebuah objek langsung, pilih salah satu objek yang ada di kotak jendela _todo list_ kemudian klik **_Zoom_**. Setelah titik objek tersebut diperbesar dan terpilih, Anda dapat menyalin _tag_ yang ada di objek tersebut ke objek OSM ter-_download_. Caranya pilih objek OSM ter-_download_ yang bertampalan/berdekatan dengan titik objek hasil survei yang sebelumnya dipilih, kemudian pilih menu **_More tools_ → _Copy tags from previous selection_** atau tekan **Shift + R** di _keyboard_. Pastikan objek yang Anda pilih sebelum menyalin _tag_ adalah objek hasil survei yang bertampalan/berdekatan dengan objek OSM ter-_download_. Pastikan juga _tag_ yang disalin sudah sesuai dengan aturan OSM serta sudah sesuai juga dengan objeknya. Seperti pada contoh objek klinik yang berada di ruko di bawah ini, objek titik hanya berisi _tag_ yang sesuai untuk objek titik, sedangan _tag_ yang berisi informasi bangunan diberikan ke objek bangunan dimana objek titik tersebut berada. Jika sudah selesai menyalin _tag_ dari satu objek, klik **_Mark_** untuk menandakan bahwa objek tersebut sudah dimasukkan ke OSM. Ulangi langkah-langkah tersebut sampai semua objek selesai dimasukkan.

![zoom_mark_di_todo](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0520_fitur_zoom_mark_todo.png)
<p align="center"><i>Menggunakan fitur Zoom dan Mark pada Todo list</i></p>

![menyesuaikan_isi_tag](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0521_tag_objek_titik.png)
<p align="center"><i>Menyesuaikan isi tag dengan objek titik</i></p>

![menyalin_tag](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0522_menyalin_tag.png)
<p align="center"><i>Menyalin tag mengenai bangunan menggunakan Shift + R</i></p>

*   Contoh objek yang dipetakan di atas digambarkan sebagai sebuah titik. Jika Anda menemukan objek yang sebaiknya digambarkan sebagai poligon, seperti misalnya kompleks sekolah yang memiliki lebih dari satu bangunan. Caranya hampir sama dengan memetakan objek titik pada langkah sebelumnya. Pilih titik objek sekolah yang akan dipetakan pada jendela _todo list_ kemudian klik **_Zoom_**. Pilih titik objek sekolah lalu salin _tag_ dari objek titik sekolah yang akan dipetakan dengan memilih objek poligon bangunan yang bertampalan/berdekatan dengan titik objek sekolah tersebut kemudian klik menu **_More tools_ → _Copy tags from previous selection_** atau tekan **Shift + R** di _keyboard_. Setelah _tag_ berhasil disalin, hapus _tag_ yang tidak berhubungan dengan bangunan dan sisakan _tag_ yang berhubungan dengan bangunan. Gambar kawasan sekolah yang meliputi seluruh bangunan menggunakan **_Draw nodes_**, lalu salin _tag_ yang sesuai dengan informasi kawasan sekolah (yang sebelumnya dihapus pada poligon bangunan) seperti _amenity_, _name_ dan _addr_. Setelah selesai memetakan kompleks sekolah, hapus objek titik hasil survei karena sudah dipetakan sebagai poligon kawasan sekolah.

![objek_sekolah](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0523_objek_sekolah_hasil_survei.png)
<p align="center"><i>Objek sekolah hasil survei</i></p>

![menyesuaikan_isi_tag](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0524_tag_bangunan_sekolah.png)
<p align="center"><i>Menyesuaikan isi tag dengan bangunan sekolah</i></p>

![menyesuaikan_isi_tag_dengan_kawasan](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0525_tag_kawasan_sekolah.png)
<p align="center"><i>Menyesuaikan isi tag dengan kawasan sekolah</i></p>

### **VI. Menyimpan Perubahan**

*   Jika Anda sudah selesai menambahkan/mengubah objek menggunakan JOSM, simpan perubahan tersebut ke server OSM karena data yang Anda tambahkan/ubah hanya ada di komputer Anda saja. Untuk menyimpan perubahan ke server OSM, caranya klik menu **_File → Upload Data_**.
*   Apabila terdapat peringatan/kesalahan (_warning/error_) setelah Anda mengklik _Upload Data_, sebaiknya peringatan/kesalahan tersebut diperbaiki terlebih dahulu. Untuk cara-cara memperbaiki peringatan/kesalahan dan jenis-jenis peringatan/kesalahan yang sering ditemui, Anda dapat mempelajari modul **Penggunaan JOSM untuk Validasi Data Survei**. Namun, jika Anda belum memahami bagaimana cara untuk memperbaiki peringatan/kesalahan, maka Anda dapat langsung mengklik **_Continue Upload_** dan akan muncul jendela **_Upload_**.
*   Jika tidak ada peringatan/kesalahan (_warning/error_), akan langsung muncul jendela **_Upload_**. Pada jendela **_Upload_** tersebut, pada kolom komentar isikan penambahan dan perubahan yang dilakukan dan pada kolom sumber tuliskan citra satelit yang digunakan untuk memetakan. Tuliskan juga *‘survey’* pada kolom sumber apabila Anda melakukan survei. Jika Anda merasa pekerjaan Anda perlu diperiksa oleh pengguna lain yang sudah mahir dalam memetakan menggunakan OSM, silakan centang _**I would like someone to review my edits**_. Setelah itu klik **_Upload Changes_**.

![jendela_upload](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0526_upload_josm.png)
<p align="center"><i>Tampilan jendela Upload</i></p>

>Catatan:
Ketika Anda memetakan suatu wilayah, sebaiknya Anda meng-_upload_-nya secara berkala agar tidak terlalu banyak perubahan yang di-_upload_. Semakin banyak perubahan yang di-_upload_ akan semakin lama pula proses _upload_-nya selesai. Apabila hasil pekerjaan Anda sudah terlanjur banyak jumlahnya, sebaiknya Anda meng-_upload_-nya per bagian. Caranya, pada jendela _**Upload**_, pilih tab _**Advanced**_ dan pilih _**Upload data in chunks of objects**_. Kemudian isi _**Chunk size**_ nya dengan jumlah perubahan yang akan di-_upload_ per bagian, misalnya 500. Hal ini bertujuan agar _upload_ tidak terputus di tengah jalan, terutama apabila internet tidak stabil dan juga menghindari terjadinya kesalahan duplikasi objek.

### **VII. Menyimpan _File .osm_**



*   Anda juga dapat menyimpan _layer_ hasil pekerjaan Anda dengan cara **klik kanan** di _layer_ tempat pekerjaan Anda dan pilih **_Save_**. Akan muncul jendela **_Save OSM file_** seperti di bawah ini. Tuliskan nama _file .osm_ nya sesuai yang Anda inginkan, kemudian klik **_Save_**. _File_ hasil pekerjaan Anda akan tersimpan dengan format _.osm_.

![jendela_save_osm_file](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0527_menyimpan_file_osm.png)
<p align="center"><i>Tampilan jendela Save OSM File</i></p>

>Catatan :
Apabila Anda belum selesai memetakan wilayah pemetaan Anda dan ingin melanjutkan memetakan, Anda dapat menyimpan pekerjaan Anda terlebih dahulu dalam format _.osm_ dan melanjutkannya. Caranya, buka _file .osm_ yang sudah disimpan dengan mengklik menu **_File → Open_** kemudian pilih _file_ yang akan dibuka dan klik **_Open_**. Setelah dibuka, perbarui data OSM tersebut dengan mengklik menu **_File → Update Data_** dan setelah itu Anda dapat melanjutkan pemetaan dan meng-_upload_-nya seperti langkah yang telah dibahas sebelumnya.

### **VIII. Melihat Perubahan di Peta**

*   Anda dapat melihat perubahan di peta OSM dengan mengeceknya pada situs web OSM <https://www.openstreetmap.org> dan mengarahkan peta ke wilayah pemetaan yang sudah Anda tambahkan datanya. Perlu diingat, perubahan baru dapat dilihat beberapa saat setelah Anda meng-_upload_ hasil pemetaan ke server OSM.

![perubahan](/pages/03-JOSM/05-Menambahkan-Data-OSM-Menggunakan-JOSM/images/0528_hasil_upload.png)
<p align="center"><i>Tampilan perubahan sebelum (kiri) dan sesudah (kanan) proses pemetaan</i></p>

**RINGKASAN**

Jika Anda dapat mengikuti dan memperhatikan seluruh tahapan dalam bab ini, maka Anda telah berhasil menerapkan proses pemetaan OSM menggunakan JOSM. Anda sudah dapat menerapkan proses menambahkan data hasil lapang ke dalam _OpenStreetMap_ seperti men-_download_ data OSM, menambahkan citra satelit, mengedit dengan JOSM, meng-_upload_ hasil pemetaan, menyimpan hasil pemetaan menjadi format _.osm_ dan melihat perubahan hasil pemetaan. Anda dapat memasukkan hasil survei secara berkala ke dalam OSM, misalnya hasil survei berdasarkan administrasi kelurahan. Jika Anda sudah melakukan survei di satu kelurahan, maka Anda dapat memasukkan data tersebut ke dalam OSM. Hal ini dapat menghindari terjadinya penumpukan data survei dan _Quality Assurance_ dapat melakukan validasi data.

