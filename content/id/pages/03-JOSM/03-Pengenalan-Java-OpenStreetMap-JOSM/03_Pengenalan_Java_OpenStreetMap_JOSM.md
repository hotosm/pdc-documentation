---
title: Pengenalan Java OpenStreetMap (JOSM)
weight: 3
---


**Tujuan Pembelajaran:**

*   Mengerti cara _download file_ instalasi JOSM
*   Mampu melakukan instalasi JOSM
*   Mampu mengubah pengaturan JOSM
*   Memahami tampilan antarmuka JOSM

JOSM adalah singkatan dari _Java OpenStreetMap_ yang merupakan perangkat editor _OpenStreetMap_ berbasis desktop. JOSM memungkinkan Anda melakukan proses edit data pemetaan secara _offline_ untuk sementara waktu atau tidak harus selalu terkoneksi dengan internet. Hal ini tentunya akan memudahkan Anda yang bekerja dalam keterbatasan koneksi internet. Anda hanya membutuhkan koneksi internet ketika akan men-_download_ data dari _OpenStreetMap_ dan ketika akan men-_upload_ data ke server _OpenStreetMap_. Selain itu pada modul ini juga akan mempelajari cara untuk mengubah beberapa pengaturan pada JOSM agar nantinya memudahkan Anda dalam menggunakannya. Anda juga akan mempelajari dan memahami apa saja bagian-bagian yang ada pada tampilan antarmuka di JOSM. Dengan memahami setiap bagian dari JOSM, di akhir modul ini Anda akan mendapatkan pemahaman secara menyeluruh mengenai perangkat JOSM beserta beberapa pengaturan dasar di dalamnya.  

### **I. _Download_ JOSM**
Jika Anda memiliki salinan _file_ instalasi JOSM pada sebuah CD atau _flashdisk_, Anda dapat langsung melanjutkan ke sub-bab selanjutnya yaitu Menginstal _JOSM_. Tetapi jika Anda tidak memiliki JOSM, atau ingin memiliki JOSM versi terbaru, silakan buka **_web browser_** Anda (dapat menggunakan _Firefox_, _Chrome_, _Opera,_ atau _Internet Explorer_). Pada kolom alamat di bagian atas jendela, kemudian ketik **josm.openstreetmap.de** kemudian tekan **_enter_**. Anda juga dapat menemukan situs JOSM dengan mengetik kata pencarian “JOSM” pada mesin pencarian _google_. Situs JOSM akan tampak seperti di bawah ini.

![tampilan_situs_JOSM](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0301_Tampilan_situs_JOSM.png)
<p align="center"><i>Tampilan situs JOSM</i></p>

Silakan pilih _file_ instalasi sesuai dengan sistem operasi komputer Anda. Jika Anda menggunakan komputer dengan sistem operasi _Windows_, klik **_Windows JOSM Installer_** untuk men-_download_ JOSM. Jika Anda memiliki sistem operasi lainnya, klik pada _link_ yang sesuai dengan sistem operasi komputer Anda. Kemudian Anda dapat men-_download_-nya. Pada modul ini kami akan mengasumsikan Anda menggunakan _Windows_, tetapi petunjuknya hampir sama dengan sistem operasi lainnya.  

### **II. Menginstal JOSM**
Setelah Anda berhasil men-_download_ JOSM, sekarang Anda akan menginstal JOSM ke komputer atau laptop Anda. Berikut ini adalah cara-cara untuk melakukan instalasi JOSM:
*   Temukan _file_ instalasi JOSM di dalam komputer Anda. Klik dua kali pada _file_ tersebut untuk memulai instalasi. Kemudian akan muncul jendela _“Do you want to allow this app from an unknown publisher to make changes to your device?”_, lalu klik **_Yes_**.
*   Selanjutnya akan muncul jendela untuk memilih bahasa. Di modul ini hanya akan membahas JOSM yang berbahasa Inggris. Jika bahasa sudah dipilih, silakan klik **_OK_**.

![tampilan_jendela_installer](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0302_Tampilan_jendela_installer_language.png)
<p align="center"><i>Tampilan jendela installer language</i></p>

*   Kemudian akan muncul jendela selanjutnya mengenai JOSM _Setup Wizard_. Klik **_Next_**.

![tampilan_JOSM_setup](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0303_Tampilan_JOSM_Setup_Wizard.png)
<p align="center"><i>Tampilan JOSM Setup Wizard</i></p>

*   Selanjutnya akan muncul jendela _License Agreement_. Klik **_I Agree_**.

![license_agreement](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0304_Tampilan_jendela_License_Agreement.png)
<p align="center"><i>Tampilan jendela License Agreement</i></p>

*   Berikutnya akan muncul jendela _Choose Components_. Disini Anda dapat memilih apa saja dari bagian JOSM yang ingin Anda _install_. Kemudian klik **_Next_**.

![tampilan_choose_components](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0305_Tampilan_jendela_choose_components.png)
<p align="center"><i>Tampilan jendela choose components</i></p>

*   Selanjutnya akan muncul jendela _Choose Install Location_. Disini Anda dapat memilih folder dimana Anda ingin menginstal JOSM. Kemudian klik **_Install_**.

![install_location](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0306_Tampilan_jendela_choose_install_location.png)
<p align="center"><i>Tampilan jendela choose install location</i></p>
 
*   Ketika instalasi selesai, klik **_Finish_** untuk membuka JOSM pertama kalinya. Kemudian, ketika  ingin memulai JOSM, Anda dapat melakukannya dengan mengklik pada _Start Menu_ di pojok kiri bawah pada komputer Anda, dan klik program JOSM.  
*   Ketika JOSM terbuka, maka akan terlihat tampilan seperti di bawah ini:

![JOSM](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0307_Tampilan_awal_JOSM.png)
<p align="center"><i>Tampilan awal JOSM</i></p>

> **Catatan:**
 Anda mungkin memiliki masalah ketika melakukan instalasi JOSM apabila Java belum terinstal di komputer Anda. Jika Anda memiliki masalah ketika melakukan instalasi pada bagian ini, cobalah mendownload dan menginstal Java. Anda dapat mendownloadnya disini: http://www.java.com/en/download/
 Anda mungkin akan melihat sebuah jendela muncul saat pertama kali membuka JOSM yang menanyakan untuk memperbarui perangkat lunak tersebut. Anda tidak perlu memperbaharuinya karena yang baru saja Anda download perangkat lunak baru. Tekan tombol _"Cancel"_. Jika Anda tidak ingin melihat pesan ini lagi, centang kotak di bawah sebelum menekan _"Cancel"_.
JOSM yang digunakan dalam modul ini versi 14760. Tampilan mungkin berbeda jika Anda menggunakan JOSM versi yang lain.

### **III. Mengubah Pengaturan Pada JOSM**
**a. Mengubah Bahasa**

Banyak pengaturan yang dapat Anda sesuaikan di JOSM. Salah satu pengaturan yang Anda mungkin ingin sesuaikan adalah bahasa. JOSM telah diterjemahkan ke dalam berbagai macam bahasa, dan Anda dapat memilih bahasa yang Anda inginkan.  Berikut ini adalah langkah-langkah untuk mengubah bahasa di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![preferences](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0308_Menu_preferences_di_JOSM.png)
<p align="center"><i>Menu preferences di JOSM</i></p>

*   Pada sisi sebelah kiri, klik ikon **_Display Setting_** yang terlihat seperti kaleng dan kuas cat.

![ikon_display_setting](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0309_Ikon_display_setting.png)
<p align="center"><i>Ikon display setting</i></p>

*   Di atas jendela, klik tab yang bertuliskan **_Look and Feel_**.
*   Pilihlah bahasa yang Anda inginkan pada kotak daftar pilihan yang bertuliskan **_Language_**. Klik **_OK_** dan kemudian **_restart_** untuk mengganti bahasa JOSM anda ke dalam bahasa yang Anda inginkan. 

![ganti_bahasa](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0310_Tampilan_display_setting_untuk_mengganti_bahasa.png)
<p align="center"><i>Tampilan display setting untuk mengganti bahasa</i></p>

**b. Mengatur Akun**

Setelah mengubah bahasa yang diinginkan untuk digunakan di JOSM, Anda juga harus memasukkan nama akun OSM Anda serta kata sandinya di dalam JOSM. Tujuannya adalah agar ketika Anda melakukan edit atau menambahkan data di peta OSM, server akan mengenali bahwa hasil edit tersebut dibuat oleh Anda. Jika Anda tidak memasukkan nama akun, maka Anda tidak dapat memasukkan data yang sudah Anda edit atau tambahkan ke dalam peta OSM.  Berikut ini adalah langkah-langkah untuk memasukkan akun OSM Anda di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![ikon_preference](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0311_Ikon_preferences_di_JOSM.png)
<p align="center"><i>Ikon preferences di JOSM</i></p>

*   Pada sisi sebelah kiri, klik ikon **_Connection Setting_** yang terlihat seperti gambar globe atau bola dunia.

![connection_setting](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0312_Ikon_connection_setting.png)
<p align="center"><i>Ikon connection setting</i></p>

*   Pilih **_Authentication → Use Basic Autentication_**.
*   Masukkan nama akun dan kata sandi Anda.

![memasukkan_akun](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0313_Tampilan_connection_setting_untuk_memasukkan_nama_akun_dan_kata_sandi.png)
<p align="center"><i>Tampilan connection setting untuk memasukkan nama akun dan kata sandi</i></p>

*   Klik **_OK_** dan kemudian **_restart_** JOSM Anda.

**c. Menambahkan _Preset_**

Sekarang Anda telah memasukkan nama akun Anda. Selanjutnya adalah pengaturan untuk memasukkan _presets_ di JOSM. _Presets_ adalah sebuah _file_ yang dapat memberikan informasi terkait objek-objek yang Anda petakan di _OpenStreetMap_.  Untuk penjelasan lebih detail tentang presets dan pembuatan _presets_, Anda dapat melihatnya di Panduan Pembuatan _Presets_ di modul **Membuat Preset**. Berikut ini adalah langkah-langkah untuk menambahkan _presets_ di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![preferences](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0314_Menu_preferences_di_JOSM.png)
<p align="center"><i>Menu preferences di JOSM</i></p>

*   Pada sisi sebelah kiri, klik ikon **_Map Setting_** yang terlihat seperti _grid_ atau kotak-kotak.

![map_setting](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0315_Ikon_Map_Setting.png)
<p align="center"><i>Ikon Map Setting</i></p>

*   Dibawah kotak _Available Preset_ cari dan pilih preset yang bernama **_HOT PDC InAWARE Indonesian Project_**. Lalu klik tanda panah biru yang berada di sebelah kanan kotak.  

![presets_JOSM](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0316_Menambahkan_preset_di_JOSM.png)
<p align="center"><i>Menambahkan preset di JOSM</i></p>

Jika Anda sudah memiliki _file presets_ Anda sendiri di komputer Anda, Anda juga dapat langsung memasukkannya dengan cara:

*   Silahkan klik tanda **+** di samping kotak _active presets_. 

![menambahkan_presets](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0317_Tanda_+_untuk_menambahkan_preset_dari_komputer.png)
<p align="center"><i>Tanda + untuk menambahkan preset dari komputer</i></p>

*   Kemudian ikon **_Open a File_** untuk mencari _file presets_ Anda.

![open_a_file](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0318_Ikon_Open_a_File.png)
<p align="center"><i>Ikon Open a File</i></p>

*   Jika sudah ditemukan klik **_Open_** kemudian **_OK_**.

**d. Memasukkan Citra Satelit**

Anda akan menggunakan citra satelit pada saat mengedit peta OSM. Jika koneksi internet Anda stabil pada saat membuka pengaturan JOSM, maka di bagian _**Edit** → **Preferences** → **Imagery Preferences**_, akan otomatis terpilih citra-citra satelit yang sering digunakan. Jika koneksi internet bermasalah dan saat dilihat bagian _Imagery Preferences_ tidak ada citra satelit yang terpilih, coba _restart_ JOSM dan lihat kembali di bagian _Imagery Preferences_ apakah citra satelitnya  sudah terpilih atau belum. Jika masih belum terpilih juga, maka berikut ini adalah langkah-langkah untuk menambahkan _presets_ di JOSM:

*   Akses jendela _Preferences_, klik _**Edit** → **Preferences**._

![preferences](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0319_Ikon_preferences_di_JOSM.png)
<p align="center"><i>Ikon preferences di JOSM</i></p>

*   Pada sisi sebelah kiri, klik ikon **_Imagery Preferences_** atau yang bertuliskan **WMS TMS**.

![imagery](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0320_Ikon_imagery_preferences.png)
<p align="center"><i>Ikon imagery preferences</i></p>

*   Kemudian klik citra satelit yang ingin Anda pilih (misalnya _Bing, Digital Globe, Mapbox, dan Esri_) pada kotak **_Available default entries_**.
*   Selanjutnya klik tombol **_Activate_** di bawah kotak _Available default entries_.

![activate](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0321_Tombol_Activate.png)
<p align="center"><i>Tombol Activate</i></p>

*   Kemudian Anda akan melihat citra satelit yang sebelumnya Anda pilih sudah masuk ke dalam kotak **_Selected Entries_** seperti gambar di bawah ini. Kemudian klik **_OK_** dan JOSM akan meminta untuk _restart_.

![tampilan_citra](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0322_Tampilan_citra_yang_sudah_dipilih.png)
<p align="center"><i>Tampilan citra yang sudah dipilih</i></p>

**e. Mengatur Tampilan Gambar Objek**

Pada pengaturan awal di JOSM, setiap objek _OpenStreetMap_ yang ada di JOSM tidak memperlihatkan titik, label, dan ikon dari setiap objek _OpenStreetMap_.

![tampilan_awal_josm](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0323_Contoh_tampilan_awal_JOSM_yang_pengaturannya_belum_diubah.png)
<p align="center"><i>Contoh tampilan awal JOSM yang pengaturannya belum diubah</i></p>

Untuk memunculkannya Anda harus mengubah tampilan _style_ peta pada JOSM Anda. Berikut ini adalah langkah-langkah untuk mengubahnya:

*   Klik pada menu **_File → New Layer_** untuk memunculkan panel pada JOSM.
*   Pada bagian kanan di panel JOSM, lihat pada bagian **_Map Paint Styles_**.
*   Jika pada panel JOSM Anda belum ada jendela _Map Paint Styles_, silahkan Anda klik menu **_Windows_** pada sisi atas JOSM Anda, kemudian klik _Map Paint Styles_ untuk mengaktifkan jendela _Map Paint Styles_ di sisi kanan JOSM Anda.

![map_paint_styles](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0324_Tampilan_untuk_mengaktifkan_Map_Paint_Styles.png)
<p align="center"><i>Tampilan untuk mengaktifkan Map Paint Styles</i></p>

*   Setelah Anda klik, akan muncul jendela _Map Paint Styles_ di sebelah kanan bawah JOSM Anda.
*   Klik kanan pada **_JOSM default (Map CSS)_** dan pilih _Style Settings._  
*   Samakan dengan tampilan di bawah ini.

![pengaturan_map_paint_styles](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0325_Pengaturan_Map_Paint_Styles_di_JOSM.png)
<p align="center"><i>Pengaturan Map Paint Styles di JOSM</i></p>

Apabila semua pengaturan sudah disamakan dengan apa yang terlihat seperti di atas, tampilan gambar JOSM Anda nantinya akan memunculkan titik, label, dan ikon untuk setiap objek di _OpenStreetMap_ seperti contoh di bawah ini:

![tampilan_awal_josm](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0326_Contoh_tampilan_awal_JOSM_yang_pengaturannya_sudah_diubah.png)
<p align="center"><i>Contoh tampilan awal JOSM yang pengaturannya sudah diubah</i></p>

### **IV. Tampilan Antarmuka JOSM**
Sekarang Anda sudah melakukan beberapa pengaturan di JOSM. Agar lebih memudahkan Anda untuk melakukan _editing_, Anda perlu untuk melihat beberapa bagian penting di JOSM. Untuk melihat tampilan antarmuka JOSM, klik pada menu **_File → New Layer_**. Berikut adalah beberapa bagian di antar muka di JOSM.

![bagian_josm](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0327_Bagian_bagian_pada_tampilan_JOSM.png)
<p align="center"><i>Bagian-bagian pada tampilan JOSM</i></p>

Pada JOSM terdapat bidang peta, _toolbar_, dan panel. Bidang peta adalah bidang untuk melihat, mengedit, dan menambahkan data _OpenStreetMap_. Pada bagian kanan JOSM terdapat serangkaian panel yang memiliki fungsi tertentu. Biasanya ketika Anda pertama kali menginstal JOSM, beberapa panel yang akan ditampilkan dengan pengaturan standar, seperti _Layer, Selections, Tags/Memberships_, dan _Author_. 

*   Panel **_layers_** akan menampilkan _layer_ apa saja yang ditambahkan ke dalam JOSM, seperti citra satelit, hasil _download_ data OSM, dan sebagainya. 
*   Ketika Anda memilih sebuah objek, baik berupa titik, garis, atau poligon di dalam bidang peta, akan ditampilkan di panel **_selections_**. 
*   Informasi mengenai objek yang akan ditampilkan pada panel **_Tags/Memberships._**
*   Nama pembuat objek akan ditampilkan di panel **_author_**. 

Jika ingin menghilangkan panel-panel tertentu, Anda dapat mengklik tanda **x** pada pojok kanan panel yang ingin hilangkan. Jika ingin menambahkan panel lainnya, Anda dapat mengaktifkannya di menu **_Windows_** dan setelah diaktifkan akan muncul pada panel di sebelah kanan JOSM.

_Toolbar_ samping kiri pada JOSM adalah jendela alat yang berisi beberapa tombol untuk _editing_ seperti tombol **_Select object_** dan _**Draw nodes**_. Di bawahnya adalah alat-alat yang untuk **_zoom and move map, delete nodes or way,_** dan **_create areas_**. Untuk pilihan _toolbar_ lainnya, Anda dapat mengklik tombol dua panah ke kanan warna hitam. Kemudian klik _toolbar_ yang Anda inginkan dan akan muncul di _toolbar_.

![tombol_untuk_mengatur_toolbar](/pages/03-JOSM/03-Pengenalan-Java-OpenStreetMap-JOSM/images/0328_Tombol_untuk_mengatur_toolbar_pada_JOSM.png)
<p align="center"><i>Tombol untuk mengatur toolbar pada JOSM</i></p>

**RINGKASAN**

Jika Anda dapat mengikuti dan mempraktikkan seluruh tahapan dalam modul ini, maka Anda telah berhasil menginstal JOSM di dalam laptop atau komputer Anda. Selain itu, Anda juga telah berhasil mempelajari dan mempraktekkan bagaimana cara melakukan pengaturan standar di JOSM untuk memudahkan pekerjaan Anda. Pada modul selanjutnya Anda akan mempelajari bagaimana cara menambahkan data di JOSM mulai dari tingkat dasar hingga tingkat lanjut. 
