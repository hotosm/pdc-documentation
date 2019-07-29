---
title: Menggunakan Java OpenStreetMap (JOSM)
weight: 4
---


**Tujuan Pembelajaran:**

*   Memahami cara menggunakan alat dasar di JOSM
*   Mampu mengoperasikan penggambaran tingkat lanjut di JOSM
*   Memahami tips _editing_ di JOSM
*   Memahami cara menggambar objek khusus seperti jembatan, kompleks sekolah, dan jaringan jalan.

_Java OpenStreetMap_ atau biasa yang disebut dengan JOSM adalah perangkat editor _OpenStreetMap_ berbasis desktop. JOSM memungkinkan Anda melakukan proses edit data pemetaan secara _offline_ untuk sementara waktu atau tidak harus selalu terkoneksi dengan internet. Jika pada modul sebelumnya Anda mempelajari pengoperasian JOSM, maka pada modul ini Anda akan mempelajari cara menggunakan JOSM.

### **I. Latihan Menggambar Dasar dengan JOSM**

Silahkan Anda buka _file_ contoh OSM yang akan digunakan untuk mempelajari cara dasar menggambar peta dengan JOSM. Perhatikan bahwa data ini hanya sebuah contoh dengan tempat yang tidak nyata, jadi Anda tidak akan menyimpan dan mengupload data tersebut ke dalam _OpenStreetMap_.



*   _Download file_ latihan tersebut disini: www.bit.ly/osmsampel
*   Buka _file_ contoh peta OSM di dalam JOSM. Klik tombol **_Open a File_** di bagian atas sebelah kiri.

![open_a_file](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0401_Ikon_Open_a_file.png)
<p align="center"><i>Ikon Open a file</i></p>

*   Cari dan pilih _file **sample.osm**_ di komputer Anda yang sebelumnya Anda _download_, kemudian klik **_Open_**. Di komputer Anda akan muncul tampilan seperti berikut ini:

![file_latihan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0402_Tampilan_file_latihan_di_JOSM.png)
<p align="center"><i>Tampilan file latihan di JOSM</i></p>

**a. Operasi Dasar**

Untuk menggeser peta ke kanan atau ke kiri dan ke atas atau ke bawah, Anda dapat melakukannya dengan cara klik kanan _mouse_ Anda, kemudian tahan dan gerakkan _mouse_ Anda sesuai dengan arah yang Anda inginkan. Terdapat dua cara untuk memperbesar dan memperkecil tampilan peta. Cara yang pertama adalah menggunakan roda gulir atau _scroll_ yang ada pada _mouse_ Anda. _Scroll_ ke depan untuk memperbesar peta dan _scroll_ ke belakang untuk memperkecil peta. Cara yang kedua adalah menggunakan skala baris di sebelah kiri di jendela peta Anda. Klik dan tahan kemudian geser ke kanan atau ke kiri dengan _mouse_ Anda.

![skala_baris](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0403_Skala_baris_di_JOSM.png)
<p align="center"><i>Skala baris di JOSM</i></p>

**b. Titik, Garis, dan Area**

Pada _OpenStreetMap_ terdapat tiga jenis objek yang digunakan. Ketiga jenis objek itu adalah titik, garis, dan poligon.

*   Titik adalah suatu lokasi yang digambarkan dengan simbol. Dalam data contoh ini terdapat dua titik, yaitu toko sepatu dan supermarket. Toko sepatu digambarkan dengan simbol sepatu dan supermarket digambarkan dengan simbol keranjang belanja. Jika Anda belum dapat melihatnya dengan jelas, silahkan perbesar tampilan peta Anda.
*   Terdapat beberapa garis yang terdapat dalam peta, objek yang digambarkan dalam bentuk garis seperti jalan, sungai, dan tanggul sungai. Jika Anda melihat dengan lebih teliti, maka Anda akan melihat di dalam garis akan terdapat titik-titik. Titik-titik tersebut tidak memiliki simbol atau informasi apapun, tetapi titik-titik tersebut yang membentuk garis.
*   Terakhir, ada beberapa poligon dalam peta contoh ini yang menunjukkan tempat-tempat yang berbeda seperti hutan, sungai, dan bangunan. Suatu poligon secara umum mewakilkan suatu area seperti lapangan ataupun bangunan. Poligon sama seperti garis, akan tetapi perbedaannya adalah poligon terdiri atas beberapa garis yang membentuk dimana titik akhir bertemu dengan titik awal garis tersebut.

**c. Memilih Objek**

Untuk mengedit suatu objek, Anda perlu untuk memilih objeknya terlebih dahulu. Berikut ini adalah cara untuk memilih objek:

*   Klik _tool **select, move, scale, and rotate object**_ untuk memilih objek.

![ikon](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0404_Ikon_tool_select_move_scale_and_rotate_object.png)
<p align="center"><i>Ikon tool select, move, scale, and rotate object</i></p>

*   Kemudian klik pada objek yang ingin Anda pilih.

Ketika Anda memilih sebuah objek, objek tersebut akan berwarna merah dan muncul beberapa daftar di panel _Tags_ pada sebelah kanan layar JOSM Anda. _Tags_ adalah bagian dari suatu titik, garis, atau poligon yang memberitahukan informasi mengenai objek tersebut. Saat ini yang Anda butuhkan adalah mengetahui informasi ini untuk menjelaskan apakah objek yang ada di peta itu hutan, sungai, bangunan, atau bentuk lain.

![informasi_objek](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0405_Informasi_objek_di_panel_Tags_JOSM.png)
<p align="center"><i>Informasi objek di panel Tags JOSM</i></p>

**d. Cara Mengubah Objek**

Anda dapat mengubah objek yang sudah digambar di JOSM. Berikut ini adalah langkah-langkah untuk mengubah objek:

*   Pilih salah satu objek pada contoh, misalnya objek hutan. Pastikan Anda mengklik garis pada hutan tersebut, bukan klik pada titiknya. Selanjutnya klik dan tahan objek tersebut kemudian geser. Anda baru saja memindahkan hutan ke lokasi yang baru pada peta.
*   Klik salah satu titik pada garis  hutan. Klik dan tahan titik tersebut kemudian geser titiknya. Anda dapat menggerakan titik. Dengan menggerakkan titik ini Anda dapat mengubah bentuk dari sebuah objek.

![contoh_mengubah_objek](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0406_Contoh_mengubah_objek.png)
<p align="center"><i>Contoh mengubah objek</i></p>

**e. Menggambar Objek**

Di sebelah kiri pada layar JOSM terdapat banyak _toolbar_ yang menyediakan lebih banyak informasi mengenai peta. _Tools_ ini dapat mengubah perintah apa yang Anda lakukan dengan _mouse_ Anda, salah satunya adalah untuk menggambar objek. Berikut ini adalah langkah-langkah untuk menggambar objek:

*   Sebelum menggambar objek, Anda perlu memastikan bahwa tidak ada objek yang terpilih. Klik diluar objek peta dimana tidak terdapat objek, untuk memastikan tidak ada objek  yang terpilih.
*   Kemudian klik pada tombol **_Draw Tool_** untuk menggambar objek.

![draw_tool](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0407_Ikon_Draw_Tool.png)
<p align="center"><i>Ikon Draw Tool</i></p>

*   Temukan area kosong pada peta, dan klik dua kali dengan _mouse_ Anda kemudian akan tergambar sebuah titik tunggal.

![menggambar_titik](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0408_Contoh_menggambar_objek_titik.png)
<p align="center"><i>Contoh menggambar objek titik</i></p>

*   Untuk menggambar sebuah garis, klik sekali dengan _mouse_ Anda. Gerakan _mouse_ Anda dan klik kembali. Lanjutkan hingga membentuk sebuah garis. Untuk mengakhiri garis, klik dua kali pada _mouse_ Anda.

![menggambar_garis](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0409_Contoh_menggambar_objek_garis.png)

<p align="center"><i>Contoh menggambar objek garis</i></p>

*   Gambarlah sebuah poligon dengan cara yang sama seperti menggambar garis, tetapi untuk mengakhiri poligon dengan klik dua kali di atas titik yang pertama kali Anda buat.

![menggambar_poligon](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0410_Contoh_menggambar_objek_poligon.png)
<p align="center"><i>Contoh menggambar objek poligon</i></p>

**f. Cara Menambahkan _Presets_**

Sekarang Anda telah memahami bagaimana cara untuk menggambar titik, garis, dan poligon. Akan tetapi Anda masih belum memberikan informasi mengenai objek tersebut. Di _OpenStreetMap_ memberikan informasi mengenai objek yang Anda gambar adalah suatu kewajiban, apakah objek tersebut adalah sekolah, rumah sakit, kantor pemerintahan dan apakah objek yang Anda buat itu bangunan atau sesuatu yang lain. Hal ini diwajibkan agar orang lain dapat mengetahui informasi objek tersebut. Untuk memberikan informasi terhadap objek yang Anda buat atau edit, Anda perlu memasukkan _presets_ di objek tersebut. Berikut ini adalah langkah-langkahnya:

*   Klik tombol **_Select_** pada _toolbar_ sebelah kiri di JOSM.
*   Pilih objek yang ingin ditambahkan _preset_.
*   Pilih menu **_Presets_** pada bagian atas JOSM. Gerakkan mouse Anda ke sub-menu jenis objek yang ingin Anda tentukan.

![memasukkan_presets](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0411_Memasukkan_preset.png)
<p align="center"><i>Memasukkan preset</i></p>

*   Jika Anda kesulitan mencari pada sub-menu, Anda dapat klik di bagian **_Search preset_** atau dengan menekan tombol **F3** pada _keyboard_ Anda.
*   Kemudian akan muncul jendela _search preset_. Anda dapat langsung mengetik jenis objeknya, misalnya **dokter gigi**. Kemudian klik **_Select_**.

![jendela_search](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0412_Jendela_search_preset.png)
<p align="center"><i>Jendela search preset</i></p>

*   Selanjutnya akan muncul jendela mengenai informasi objek yang Anda petakan. Informasi ini tidak wajib diisi semua, hanya yang Anda ketahui saja. Jika Anda mengetahui semua informasinya silahkan diisi. Jika tidak tahu dilewatkan saja, kemudian klik **_Apply Preset_**. Jika semuanya berjalan dengan lancar, titik, garis, atau poligon yang Anda buat akan berubah warna atau memiliki suatu simbol. Perubahan ini tergantung dari informasi yang Anda masukkan ke dalam objek tersebut.

![jendela_informasi](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0413_Jendela_informasi_objek.png)
<p align="center"><i>Jendela informasi objek</i></p>

### **II. Latihan Menggambar Tingkat Lanjut dengan JOSM**
Pada sesi sebelumnya Anda telah menginstal JOSM dan mempelajari bagaimana melakukan operasi dasar di JOSM seperti menggambar titik, garis, dan poligon. Anda juga telah dapat menambahkan preset ke objek yang Anda buat untuk melampirkan informasi mengenai objek tersebut. Pada akhirnya, Anda dapat menggambar peta Anda sendiri di JOSM.  Pada sesi ini Anda akan mempelajari bagaimana tahapan-tahapan yang tepat dalam mengedit peta _OpenStreetMap_ di JOSM dan juga bagaimana Anda bisa memaksimalkan beberapa alat yang ada di JOSM untuk membantu Anda dalam melakukan _editing_.

**a. Alat Menggambar Tingkat Lanjut di JOSM**

Pada materi ini Anda akan mempelajari beberapa _tools_ dasar dan teknik yang ada untuk menggambar fitur peta di JOSM. Anda akan mempelajari lebih detail untuk _tools_ menggambar lanjutan yang akan membantu Anda dalam melakukan pemetaan di JOSM. Silakan Anda _download_ di [http://www.bit.ly/toolsbahasa] (http://www.bity.ly/toolsbahasa) kemudian buka JOSM dan file yang telah di-_download_. Tampilan pada JOSM Anda akan seperti di bawah ini:

![tampilan_file](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0414_Tampilan_file_latihan_mengedit_di_JOSM.png)
<p align="center"><i>Tampilan file latihan mengedit di JOSM</i></p>

JOSM memiliki _tools_ yang akan memudahkan Anda dalam mengedit baik garis atau poligon. _Tools_ ini dapat ditemukan di menu **_Tools_** di bagian atas JOSM. Jika Anda klik pada menu _Tools_ di bagian atas JOSM, Anda akan melihat bahwa terdapat banyak fungsi yang dapat membantu Anda dalam menggambar garis dan poligon, dan juga mengedit objek pada peta.

![pilihan_menu_tool](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0415_Pilihan_yang_ada_di_menu_tools_JOSM.png)
<p align="center"><i>Pilihan yang ada di menu tools JOSM</i></p>

Dalam mengaplikasikan fungsi dalam menu ini, Anda terlebih dahulu harus memilih sebuah titik, garis, atau poligon pada bidang peta. _File_ contoh yang telah Anda _download_ berisi berbagai macam elemen yang berlabelkan nama alat yang berbeda-beda di dalam menu. Anda dapat mencoba masing-masing _tools_ menggunakan _file_ contoh. Penjelasan mengenai beberapa _tools_ lainnya disediakan di bawah ini:

*   **_Split Way_** (Memisahkan Segmen Garis/_Way_).

    _Split Way_ digunakan untuk membagi sebuah segmen garis menjadi dua segmen garis yang terpisah. Ini berguna jika Anda ingin menambahkan atribut ke bagian jalan yang berbeda, seperti jembatan atau jalan yang berbeda nama. Untuk menggunakan fungsi ini, pilih sebuah titik di tengah segmen garis yang Anda ingin potong, kemudian klik **_Split Way_** dari menu _Tools_, dan garis Anda akan terpotong menjadi dua. Tombol pintas untuk melakukan _split way_ adalah tombol **P** pada _keyboard_ setelah anda memilih salah satu titik pada garis.

![split_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0416_Tampilan_split_way.png)
<p align="center"><i>Tampilan split way</i></p>

Setelah Anda melakukan _split way_, Anda dapat menambahkan informasi mengenai masing-masing segmen jalan yang sudah dipisah, misalnya seperti memberikan nama jalan pada kedua jalan.

*   **_Combine Way_** (menggabungkan segmen garis/_way_).

    _Combine way_ ini adalah kebalikan dari _Split Way_, digunakan untuk menggabungkan dua segmen garis menjadi satu segmen garis. Kedua segmen garis ini harus saling terhubung dengan titik yang sama. Untuk menggunakan fungsi ini, pilih kedua garis yang ingin Anda gabungkan. Anda dapat memilih lebih dari satu objek dengan menahan tombol _shift_ pada _keyboard_ Anda dan klik di kedua garisnya. Ketika Anda telah memilih kedua garis tersebut, klik **_Combine Way_** dari menu _Tools_. Kedua segmen garis tersebut akan menyatu jadi satu segmen garis. Tombol pintas untuk melakukan _combine way_ adalah tombol **C** pada _keyboard_ setelah anda mengklik kedua garis.

![combine_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0417_Tampilan_combine_way.png)
<p align="center"><i>Tampilan combine way</i></p>

![menggabungkan_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0418_Hasil_menggabungkan_Garis_Way_JOSM.png)
<p align="center"><i>Hasil menggabungkan Garis/Way JOSM</i></p>

Jika Anda menggabungkan jalan yang memiliki arah yang berbeda, Anda akan mendapatkan peringatan seperti di bawah ini. Peringatan tersebut berarti jika jalan yang terhubung dan memiliki arah yang sama. Jika Anda yakin untuk menggabungkan kedua jalan tersebut, silakan Anda klik **_Reverse and Combine_**.

![peringatan_change_direction](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0419_Peringatan_change_directions.png)
<p align="center"><i>Peringatan change directions</i></p>

*   **_Reverse Way_** (membalikkan garis/_way_). 

    _Reverse way_ digunakan untuk mengubah arah pada garis. Semua garis di dalam OSM memiliki sebuah arah, yang ditunjukkan di dalam JOSM dengan panah pada garis. Pengaturan arah sangat berguna untuk memetakan jalan yang memiliki satu arah dan aliran sungai (hulu ke hilir). Pada kasus ini, Anda mungkin perlu membalikkan arah garis sehingga garis tersebut dalam arah yang benar. Cara untuk menggunakan _reverse way_ ini adalah klik pada garis yang ingin Anda ubah arahnya, kemudian ke menu _tools_ dan klik **_Reverse Ways_**. Tombol pintas untuk melakukan _reverse way_ adalah tombol **R** pada _keyboard_.

![reverse_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0420_Tampilan_reverse_ways.png)
<p align="center"><i>Tampilan reverse way</i></p>

*   **_Simplify Way_** (sederhanakan jalur)

    Jika garis Anda memiliki terlalu banyak titik di dalamnya dan Anda ingin membuatnya lebih sederhana, menu _simplify way_ akan menghapus beberapa titik yang ada pada sebuah garis. _Tool_ ini juga digunakan untuk mempercepat saat _upload_ data karena menghapus beberapa nodes/titik yang berada di satu garis. Cara untuk menggunakan _simplify way_ adalah klik pada garis yang ingin Anda sederhanakan, kemudian ke menu _tools_ dan klik **_Simplify Way_**. Tombol pintas untuk melakukan _simplify way_ adalah tombol **Shift+Y** pada _keyboard._

![simplify_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0421_Tampilan_simplify_way.png)
<p align="center"><i>Tampilan simplify way</i></p>

*   **_Align Nodes in Circle_** (Sejajarkan _Node_ Membentuk Lingkaran).

    Jika Anda mengalami kesulitan dalam menggambar bentuk lingkaran di dalam OSM, maka Anda dapat menggunakan _tools_ ini untuk membuat bentuk lingkaran secara sempurna. Cara untuk menggunakan _align nodes in circle_ ini adalah klik pada garis yang ingin Anda sederhanakan, kemudian ke menu _tools_ dan klik **_Align Nodes in Circle_**. Tombol pintas untuk melakukan _align nodes in circle_ adalah tombol **O** pada _keyboard._

![align_node_in_circle](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0422_Tampilan_Align_Nodes_in_Circle.png)
<p align="center"><i>Tampilan Align Nodes in Circle</i></p>

*   **_Create Circle_** (Buat Lingkaran)

    Sebagai alternatif untuk membuat lingkaran, Anda dapat menggunakan _tool create circle_. _Tool_ ini akan membuat lingkaran dari diameter lingkaran (hanya memerlukan sebuah garis yang terdiri atas dua titik). Cara untuk menggunakan _create circle_ ini adalah gambar sebuah garis yang mewakili diameter dari lingkaran yang Anda inginkan, dan kemudian ke menu tools dan klik **_Create Circle_**. Tombol pintas untuk melakukan _create circle_ adalah tombol **Shift+O** pada _keyboard._

![create_circle](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0423_Tampilan_create_cirle.png)
<p align="center"><i>Tampilan create cirle</i></p>

*   **_Align Nodes in Line_** (Sejajarkan Node dalam Garis/_Way_)

    Fungsi ini digunakan untuk mengubah garis yang tidak beraturan menjadi bentuk yang lurus. Hati-hati karena hal ini memiliki kecenderungan untuk pergeseran garis walaupun sedikit. Perlu diingat, fungsi ini akan meluruskan bentuk garis sesuai letak titik awal dan akhir garis tersebut. Cara untuk menggunakan _align nodes in line_ ini adalah klik garis yang ingin Anda sejajarkan, dan kemudian ke menu tools dan klik **_Align Nodes in Line_**. Tombol pintas untuk melakukan _align nodes in line_ adalah tombol **L** pada _keyboard_.

![align_node_in_line](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0424_Tampilan_align_nodes_in_line.png)
<p align="center"><i>Tampilan align nodes in line</i></p>

![setelah_align_node_in_line](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0425_Contoh_setelah_menggunakan_align_nodes_in_line.png)
<p align="center"><i>Contoh setelah menggunakan align nodes in line</i></p>

*   **_Orthogonalize Shape_** (Ortogonalisasi Bentuk)

    _Orthogonalize shape_ sangat berguna untuk membuat gambar poligon yang memiliki sudut-sudut tidak teratur menjadi bentuk persegi, contohnya adalah bentuk bangunan. Setelah Anda menggambar sebuah bangunan, fungsi ini akan membentuk menjadi bangunan yang memiliki sudut  persegi 90’. Cara untuk menggunakan _orthogonalize shape_ ini adalah klik objek yang ingin Anda ubah bentuknya, dan kemudian ke menu _tools_ dan pilih **_Orthogonalize Shape_**. Tombol pintas untuk melakukan _orthogonalize shape_ adalah tombol **Q** pada _keyboard_.

![orthogonalize_shape](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0426_Tampilan_orthogonalize_shape.png)
<p align="center"><i>Tampilan orthogonalize shape</i></p>

![setelah_ortho_shape](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0427_Contoh_setelah_menggunakan_orthogonalize_shape.png)
<p align="center"><i>Contoh setelah menggunakan orthogonalize shape</i></p>

*   **_Unglue Way_** (Memisahkan Titik/Garis)

    _Unglue way_ berfungsi untuk melepaskan titik-titik yang terhubung. _Unglue way_ berguna ketika dua objek berada di titik yang sama padahal seharusnya mereka tidak menempel. Sebagai contoh, kesalahan yang sering terjadi adalah sebuah jalan memiliki titik yang sama dengan sudut bangunan. Tentu saja di lapangan, jalan tidak mungkin bergabung dengan bangunan, sehingga ini adalah suatu kesalahan. Untuk memperbaikinya Anda dapat melepaskan objek satu dengan yang lain. Cara untuk menggunakan _unglue way_ ini adalah klik titik yang saling menempel antara dua objek, dan kemudian ke menu tools dan pilih **_Unglue Way_**. Tombol pintas untuk melakukan _unglue way_ adalah tombol **G** pada _keyboard_. Perlu Anda perhatikan ketika Anda sudah menggunakan _tool_ ini, antara kedua objek yang sebelumnya saling menempel, tidak langsung otomatis terpisah, tetapi harus Anda menggeser salah satu objeknya.

![unglue_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0428_Tampilan_unglue_way.png)
<p align="center"><i>Tampilan unglue way</i></p>

![setelah_unglue](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0429_Contoh_setelah_menggunakan_unglue_way.png)
<p align="center"><i>Contoh setelah menggunakan unglue way</i></p>

Sering kali terdapat pertanyaan bagaimana cara untuk memutar sebuah garis atau poligon setelah objek tersebut tergambar. Cara untuk memutar objek tersebut adalah sebagai berikut:
*   Untuk memutar sebuah objek, pertama pilih objek yang ingin Anda putar.
*   Tahan **SHIFT+CTRL** pada _keyboard_ Anda.
*   Klik dan geser _mouse_ untuk memutar.

![konsep_memutar_object](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0430_Konsep_memutar_objek_di_JOSM.png)
<p align="center"><i>Konsep memutar objek di JOSM</i></p>

**b. Tombol Pintas di Keyboard**

Setelah melakukan _editing_ di _OpenStreetMap_, Anda akan menyadari bahwa Anda kesulitan untuk mencari letak _tools_ yang terdapat pada menu _Tools_. Untuk mengatasi hal ini, JOSM memiliki tombol pintas _keyboard_ untuk segala hal. Hal ini bertujuan untuk mempermudah Anda tanpa harus mengklik sebuah objek terlebih dahulu dan kemudian melalui proses menu dan sub-menu yang panjang. Anda dapat memilih objek langsung dan menekan sebuah tombol pada keyboard Anda. Berikut ini adalah beberapa tombol pintas yang sering digunakan:

Tabel Beberapa Tombol Pintas di JOSM

|No.| Perintah  | Simbol  |
|---|---|---|
|1|Aktifkan _Select Tool_|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0431_Select_Tool.png)|
|2|Aktifkan _Draw Tool_|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0432_Draw_Tool.png)|
|3|Aktifkan _Zoom Tool_|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0433_Zoom_Tool.png)|
|4|Hapus objek yang terpilih|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0434_Hapus.png)|
|5|_Zoom In_|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0435_Zoom_In.png)|
|6|_Zoom Out_|![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0436_Zoom_Out.png)|

### **III. Tips Editing**
Ada beberapa kesalahan umum yang biasa dilakukan oleh pengguna ketika memulai menggunakan _OpenStreetMap_. Berikut ini beberapa kesalahan yang sering dilakukan dan beberapa tips atau petunjuk singkat untuk memetakan lebih baik.

**1. Objek yang Sebaiknya Tidak Terhubung**

Ketika Anda membuat poligon dan garis yang seharusnya tidak terhubung, pastikan bahwa mereka tidak terhubung oleh satu titik. Contohnya titik jalan raya sebaiknya tidak menempel ke bangunan, walaupun pada kenyataannya terdapat bangunan yang terletak di depan jalan, namun tetap ada sedikit ruang yang memisahkan antara bangunan dan jalan tersebut. Jika Anda ingin memisahkan dua atau lebih objek yang menempel di titik yang sama, pilih titik yang saling terhubung kemudian pilih menu **_Tools →  UnGlue Ways_** atau tombol pintasnya adalah tekan **G** pada keyboard, kemudian geser salah satu objeknya.

![bangunan_jalan_terpisah](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0437_Objek_bangunan_dan_jalan_yang_tersambung_dan_objek_bangunan_dan_jalan_yang_terpisah.png)
<p align="center"><i>(Kiri) Objek bangunan dan jalan yang tersambung dan (Kanan) objek bangunan dan jalan yang terpisah</i></p>

**2. Objek yang Harus Terhubung**

Jika sebelumnya membahas mengenai objek yang tidak boleh terhubung, sekarang Anda akan mempelajari objek apa saja yang harus terhubung, misalnya jalan yang bersinggungan atau persimpangan seharusnya selalu terhubung pada titik. Jika mereka tidak terhubung pada satu titik, maka JOSM tidak mengetahui bahwa jalan tersebut sebenarnya saling terhubung satu sama lain. Oleh karena itu, jika terdapat jalan yang tidak saling terhubung satu sama lain, maka Anda dapat memperbaiki dengan pilih _node_/titik dari jalan yang ingin dihubungkan, kemudian pilih menu **_Tools →  Merge Nodes_** atau tekan **M** pada keyboard.

![jalan_harus_terhubung](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0438_Jalan_harus_terhubung_satu_sama_lain.png)
<p align="center"><i>Jalan harus terhubung satu sama lain</i></p>

**3. Objek yang Saling _Overlap_ atau Tumpang Tindih**

Salah satu kesalahan umum pada saat menggambar di JOSM adalah poligon saling _overlap_, padahal seharusnya objek yang digambarkan tidak saling _overlap_. Sebuah bangunan tidak bisa _overlap_ dengan bangunan yang lain. Sebagai contoh, poligon penggunaan lahan permukiman tidak seharusnya overlap atau tumpang tindih dengan poligon kebun.

![poligon_overlap](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0439_Contoh_poligon_yang_saling_overlap.png)
<p align="center"><i>Contoh poligon yang saling overlap</i></p>

Ada beberapa pengecualian pada aturan ini, contohnya seperti bangunan sekolah. Di dalam halaman sekolah mungkin Anda ingin mengidentifikasi bangunan menggunakan poligon, tapi mungkin Anda juga ingin membuat sebuah poligon yang meliputi seluruh halaman sekolah. Dalam kasus seperti ini, poligon diperbolehkan untuk saling overlap, tetapi aturannya adalah pastikan bahwa bangunan-bangunan secara menyeluruh berada dalam poligon penggunaan lahan.

![poligon_sekolah](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0440_Contoh_sekolah_dengan_poligon_keseluruhan_halaman_sekolah_dan_bangunannya.png)
<p align="center"><i>Contoh sekolah dengan poligon keseluruhan halaman sekolah dan bangunannya</i></p>

**4. Tips lain**

Saat menggambar di JOSM, ada beberapa kesalahan-kesalahan lain yang sering terjadi. Berikut ini adalah contoh-contoh kesalahan lainnya yang sering terjadi dan tips agar menghindari kesalahan tersebut.

Tabel Kesalahan yang Sering Terjadi dan Tipsnya

| Kesalahan  |Tips   |
|---|---|
|Tag diberikan pada node, bukan pada objek (misalnya: bangunan) ![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0441_Contoh_bangunan_yang_diberikan_tag_yang_salah_dan_benar.png) |Satu masalah umum yang sering terjadi yaitu menambahkan tag pada node atau titik yang terdapat pada bagian dari sebuah garis atau poligon. Ini sering terjadi ketika seseorang menggambar sebuah objek, kemudian melakukan _select all)_ pada objek (memilih semua titik/_select node_ pada garis). Kemudian seseorang menambahkan _presets_, sehingga tag terdapat di setiap sudut poligon, ini adalah cara yang tidak tepat. Cara untuk menghindari hal ini, dengan klik objek secara langsung pada garis atau hindari _select all_ pada objek.|
|Persimpangan yang bertemu di sudut jalan atau persimpangan jalan harus dipisah ![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0442_Contoh_pembuatan_simpangan_yang_salah_dan_benar.png) |Ketika jalan bersinggungan atau persimpangan satu sama lain di sudut jalan, Anda tidak boleh membuat garis melengkung di persimpangan. Garis seharusnya berbentuk sudut 90° dan terpisah menjadi dua segmen garis yang berbeda, seperti di kondisi yang sebenarnya di lapangan|
|Tidak ada tag pada node atau garis ![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0443_Contoh_tidak_ada_tag_pada_node_atau_garis.png)|Untuk memperbaiki kesalahan ini, pilih objek dan masukan _presets_ sesuai dengan informasi objek tersebut atau bisa dihapus bila objek itu merupakan kesalahan. Hal ini dikarenakan, server OSM tidak bisa membaca sebuah objek yang tidak dilengkapi dengan presets (informasi objek).|
|Garis berada dekat dengan garis lain tetapi tidak terhubung ![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0444_Contoh_garis_jalan_yang_tidak_saling_terhubung.png)|Untuk memperbaikinya, Anda dapat memilih titik dari garis yang ingin dihubungkan dan kemudian pilih _tool Draw nodes_ untuk menambahkan titik di garis yang mendatar/garis yang berada di depannya. Alternatif lainnya, Anda dapat menggunakan _tool Merge Node_ (jika di depan garis yang belum terhubung tersebut merupakan sebuah titik), caranya: 1. Pilih kedua titik yang berdekatan, yang berada di dalam kedua garis yang ingin dihubungkan. 2. Pilih _Merge Node_ yang berada di  _Menu tools_. Jika didepan garis yang belum terhubung tersebut tidak terdapat sebuah titik, Anda bisa menggunakan _tool Join Node to Way_ dengan cara: 1. Pilih titik terakhir dari garis yang belum terhubung dan juga pilih garis yang berada di depan garis yang belum terhubung. 2. Pilih _Join Node to Way_ yang Berada Di _Menu Tools_|
|Garis tidak boleh melewati bangunan ![](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0445_Contoh_salah_garis_melewati_bangunan.png) |Untuk mengatasinya, Anda perlu melihat menggunakan citra satelit objek mana yang berada pada lokasi yang salah. Kemudian Anda dapat menggeser objek tersebut ke tempat yang sesuai. Contoh garis yang tidak boleh melewati bangunan misalnya sungai.|

### **IV. Menggambar Objek Khusus**
Saat ini Anda telah mempelajari bagaimana cara menggambar sebuah objek di OSM dengan menggunakan JOSM dan apa saja yang harus diperhatikan dalam menggambar sebuah objek di JOSM. Ketika Anda mencoba menggambar sebuah objek menggunakan citra satelit, Anda mungkin akan menemui beberapa objek membutuhkan teknik penggambaran khusus, seperti misalnya jembatan, kompleks perkantoran, atau jalan besar yang mempunyai pembatas jalan.

**1. Menggambar jembatan**

Jembatan pada umumnya dapat dijumpai di atas suatu jaringan sungai. Namun, dalam penggambarannya di OSM, Anda tidak bisa sekedar menggambarkan suatu garis/jalan di atas sungai. Apabila hal tersebut Anda lakukan, secara teknis gambar Anda tetap dapat di-_upload_ di OSM, namun akan dianggap sebagai suatu kesalahan oleh sistem. Lalu, bagaimana cara menggambar objek jembatan yang benar? Berikut ini adalah contoh suatu area yang di dalamnya terdapat objek jembatan.

![contoh_jembatan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0446_Contoh_objek_jembatan.png)
<p align="center"><i>Contoh objek jembatan</i></p>

Langkah digitasinya adalah sebagai berikut:
*   Gambar terlebih dahulu jaringan sungai.

![gambar_jaringan_sungai](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0447_Contoh_gambar_jaringan_sungai.png)
<p align="center"><i>Contoh gambar jaringan sungai</i></p>

*   Gambar jaringan jalan yang melintasi (di atas) sungai tersebut.

![gambar_jaringan_jalan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0448_Contoh_gambar_jaringan_jalan_di_atas_sungai.png)
<p align="center"><i>Contoh gambar jaringan jalan di atas sungai</i></p>

*   Perbesar tampilan pada citra satelit, maka Anda akan melihat ujung kiri dan ujung kanan jembatan.

![gambar_ujung_jembatan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0449_Contoh_gambar_ujung_jembatan.png)
<p align="center"><i>Contoh gambar ujung jembatan</i></p>

*   Pada garis jaringan jalan, buatlah titik/_node_ yang bertepatan dengan ujung kiri dan ujung kanan jembatan.

![gambar_titik_setiap_ujung](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0450_Gambar_titik_di_setiap_ujung_jembatan.png)
<p align="center"><i>Gambar titik di setiap ujung jembatan</i></p>

*   Selanjutnya, Anda akan memisahkan garis yang merupakan jembatan dan garis yang hanya merupakan jaringan jalan. Untuk melakukan pemisahan garis (_split way_), caranya adalah klik kedua _node_ yang baru saja Anda buat, yang merupakan ujung kiri dan kanan jembatan kemudian menuju menu **_Tools →  Split Way_**.

![split_way](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0451_Contoh_split_way.png)
<p align="center"><i>Contoh split way</i></p>

* Maka, garis yang semula merupakan 1 segmen jaringan jalan saja, kini telah terbagi menjadi 3 segmen, yaitu (1) jaringan jalan di sebelah kiri jembatan, (2) jembatan, (3) jaringan jalan di sebelah kanan jembatan.

![jalan_sudah_terbagi](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0452_Jalan_sudah_terbagi_menjadi_tiga_segmen.png)
<p align="center"><i>Jalan sudah terbagi menjadi tiga segmen</i></p>

*   Setelah objek jembatan tergambarkan sebagai objek sendiri, langkah selanjutnya adalah memberi _tag_/keterangan bahwa objek tersebut adalah suatu jembatan. Sekarang, klik pada objek jembatan, kemudian klik menu **_Preset →  Man Made → Bridges → Bridge_**.

![meambahkan_jembatan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0453_Cara_menambahkan_jembatan.png)
<p align="center"><i>Cara menambahkan jembatan</i></p>

*   Akan terbuka kotak dialog _preset_ jembatan (_bridges_). Cukup isikan keterangan **Bridge=yes** dan **Layer=1**. Layer=1 ini berfungsi untuk menambahkan informasi bahwa jembatan tersebut berada di satu tingkat lebih tinggi dibandingkan dengan dasarnya.

![informasi_untuk_jembatan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0453_Cara_menambahkan_jembatan.png)
<p align="center"><i>Informasi yang harus diisi untuk jembatan</i></p>

*   Selesai.

![gambar_jembatan_berhasil_dibuat](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0455_Contoh_gambar_jembatan_yang_sudah_berhasil_dibuat.png)
<p align="center"><i>Contoh gambar jembatan yang sudah berhasil dibuat</i></p>

![contoh_gambar_jembatan_dan_infonya](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0456_Contoh_gambar_jembatan_dan_informasinya_di_bagian_panel_tags.png)
<p align="center"><i>Contoh gambar jembatan dan informasinya di bagian panel tags</i></p>

**2. Menggambar Kompleks Sekolah, Perkantor, atau Gedung**

Suatu sekolah, rumah sakit, atau perkantoran pada umumnya tidak berdiri sendiri, melainkan terdiri dari beberapa bangunan di dalamnya. Dalam sub-bab ini, akan dibahas bagaimana menggambar sebuah kompleks sekolah yang memiliki beberapa bangunan dan objek di dalamnya. Lihat contoh gambar di bawah ini:

![contoh_beberapa_bangunan_sekolah](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0457_Contoh_beberapa_bangunan_sekolah.png)
<p align="center"><i>Contoh beberapa bangunan sekolah</i></p>

Beberapa orang menggambarkannya sebagai suatu kompleks bangunan yang sangat besar, yang dibatasi oleh pagar yang mengitari (lihat gambar a). Sebagian yang lain menggambarkan setiap bangunan di dalam kompleks tersebut secara terpisah, kemudian setiap bangunan  diberi nama/keterangan sesuai dengan nama/keterangan sekolah tersebut (gambar b). Dengan cara yang seperti itu, maka akan terhitung bahwa pada lokasi tersebut terdapat lebih dari 1 sekolah. Hal tersebut bukanlah cara penggambaran yang benar.

![gambar_a_b](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0458_Gambar_a_dan_gambar_b.png)
<p align="center"><i>Gambar a dan gambar b</i></p>

Lalu bagaimana cara penggambaran yang benar untuk suatu objek yang merupakan suatu kompleks, yang terdiri atas bangunan-bangunan lain yang lebih kecil? Berikut ini adalah langkah-langkahnya:
*   Pertama, gambarlah elemen-elemen/bagian-bagian dari sekolah tersebut yang berada di dalam area pagar/batas terluar sekolah, misalnya gedung ruang kelas, gedung parkir, masjid, lapangan, dan taman. Berikan _tag_ sesuai jenis objek.

![gambar_object_di_sekolah](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0459_Contoh_gambar_objek_objek_yang_terdapat_di_dalam_sekolah.png)
<p align="center"><i>Contoh gambar objek-objek yang terdapat di dalam sekolah</i></p>

*   Setelah semua elemen tergambar, gambarlah pagar/batas terluar dari sekolah tersebut, dengan memberikan _tag **amenity=school.**_

![gambar_garis_terluar](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0460_Gambar_garis_terluar_dari_sekolah.png)
<p align="center"><i>Gambar garis terluar dari sekolah</i></p>

Jika sudah tergambar seperti gambar di atas, maka Anda sudah berhasil membuat gambar lingkungan sekolah dengan benar.

**3. Menggambar Jaringan Jalan Dengan Pembatas Jalan**

Suatu jaringan jalan dapat dijumpai dalam wujud yang sederhana (lebar 1-3 meter dan tanpa pembatas) (gambar a), namun dapat pula dijumpai dalam wujud yang kompleks, yang sangat lebar (mencapai 10-20 meter) dan terdapat pembatas jalan (gambar b). 

![gambar_a_b](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0461_Gambar_a_dan_Gambar_b.png)
<p align="center"><i>Gambar a dan Gambar b</i></p>

Untuk menggambar jaringan jalan yang sederhana, tentulah sangat mudah, yaitu cukup menggambarkannya dengan satu garis. Namun, untuk menggambar jaringan jalan yang terdapat pembatas di tengah jaringan jalan tersebut, Anda harus menggambar ruas yang dipisahkan menjadi ruas jalan yang berbeda.  Di bawah ini  adalah sebagian dari ruas jalan Thamrin, Jakarta Pusat. Jalan ini memiliki lebar kurang lebih 40 meter, dan terdapat pembatas di tengah jalan, yang memisahkan arus kendaraan dari arah utara dan kendaraan dari arah selatan. 

![sebagian_jalan_thamrin](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0462_Sebagian_Jalan_Thamrin.png)
<p align="center"><i>Sebagian Jalan Thamrin</i></p>

Untuk menggambarkan Jalan Thamrin tersebut, Anda harus menggambarkannya dengan dua garis,  yang nantinya akan menggambarkan ruas jalan yang dilewati oleh kendaraan dari arah utara dan ruas jalan yang dilewati oleh kendaraan dari arah selatan. Berikut ini adalah langkah-langkah untuk menggambar jalan seperti Jalan Thamrin.

*   Pertama, gambarlah garis dari bawah ke atas (selatan ke utara), kemudian beri _tag **highway=primary**_, **_name=Jalan Thamrin_**, dan **_oneway=yes_**. Selanjutnya, gambarlah garis dari atas ke bawah (utara ke selatan), kemudian beri tag **_highway=primary_** dan **_name=Jalan Thamrin_** dan **_oneway=yes_**. 

![gambar_jalan_dari_bawah_keatas](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0462_Sebagian_Jalan_Thamrin.png)
<p align="center"><i>Gambar jalan dari bawah ke atas (selatan ke utara)</i></p>

![gambar_jalan_utara_selatan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0464_Gambar_jalan_dari_atas_ke_bawah_utara_ke_selatan.png)
<p align="center"><i>Gambar jalan dari atas ke bawah (utara ke selatan)</i></p>

Perhatikan arah panah pada kedua garis berbeda. Pada garis pertama, arah panah ke atas, artinya ruas jalan tersebut adalah ruas jalan yang dilewati oleh kendaraan dari arah selatan ke arah utara. Pada garis kedua arah panah ke bawah, artinya ruas jalan tersebut adalah ruas jalan yang dilewati oleh kendaraan dari arah utara ke arah selatan.

Jika suatu jalan terdiri atas empat ruas yang berbeda (berarti terdapat 3 pembatas jalan), misalnya jalur lambat arah ke utara, jalur cepat arah ke utara, jalur lambat arah ke selatan, dan jalur cepat arah ke selatan; maka Anda harus menggambarkan jalan tersebut dengan 4 garis. Kondisi tersebut misalnya dijumpai di Jalan Sudirman, Jakarta Pusat.

![jalan_sudirman](pages/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0465_Salah_satu_bagian_Jalan_Sudirman_Jakarta_Pusat.png)
<p align="center"><i>Salah satu bagian Jalan Sudirman, Jakarta Pusat, yang terdiri dari empat ruas (tiga pembatas jalan)</i></p>

![tampilan_ruas_jalan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0466_Tampilan_ruas_jalan_di_atas_pada_citra_satelit.png)
<p align="center"><i>Tampilan ruas jalan di atas, pada citra satelit</i></p>

![kondisi_ruas_jalan](/id/images/03-JOSM/04-Menggunakan-Java-OpenStreetMap-JOSM/0467_Ruas_jalan_tersebut_meskipun_merupakan_1_jalan_yang_sama_yaitu_jalan_sudirman.png)
<p align="center"><i>Ruas jalan tersebut, meskipun merupakan satu jalan yang sama, yaitu Jalan Sudirman, namun terdiri dari empat ruas; pada OSM, digambarkan dengan empat garis yang berbeda</i></p>

**RINGKASAN**

Selamat! Jika semua berjalan dengan baik, Anda sudah mempelajari bagaimana menggunakan _tools_ atau alat-alat menggambar pada JOSM yang dapat membantu Anda dapat memetakan objek-objek di OSM. Anda juga sudah mempelajari tips-tips editing yang akan berguna pada saat Anda editing menggunakan JOSM. Pada bab selanjutnya, Anda akan melihat lebih dekat bagaimana proses mengedit peta OSM di JOSM.
