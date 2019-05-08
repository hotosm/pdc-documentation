# **Pengenalan _Java OpenStreetMap_ (JOSM)**

**Tujuan Pembelajaran:**
*   Mengerti cara _download file _instalasi JOSM
*   Mampu melakukan instalasi JOSM
*   Mampu mengubah pengaturan JOSM
*   Memahami tampilan antarmuka JOSM

JOSM adalah singkatan dari _Java OpenStreetMap_ yang merupakan perangkat editor _OpenStreetMap_ berbasis desktop. JOSM memungkinkan Anda melakukan proses edit data pemetaan secara _offline_ untuk sementara waktu atau tidak harus selalu terkoneksi dengan internet. Hal ini tentunya akan memudahkan Anda yang bekerja dalam keterbatasan koneksi internet. Anda hanya membutuhkan koneksi internet ketika akan men-_download_ data dari _OpenStreetMap_ dan ketika akan men-_upload_ data ke server _OpenStreetMap_. Selain itu pada modul ini juga akan mempelajari cara untuk mengubah beberapa pengaturan pada JOSM agar nantinya memudahkan Anda dalam menggunakannya. Anda juga akan mempelajari dan memahami apa saja bagian-bagian yang ada pada tampilan antarmuka di JOSM. Dengan memahami setiap bagian dari JOSM, di akhir modul ini Anda akan mendapatkan pemahaman secara menyeluruh mengenai perangkat JOSM beserta beberapa pengaturan dasar di dalamnya.  

### **I. _Download_ JOSM**
Jika Anda memiliki salinan _file_ instalasi JOSM pada sebuah CD atau _flashdisk_, Anda dapat langsung melanjutkan ke sub-bab selanjutnya yaitu Menginstal _JOSM_. Tetapi jika Anda tidak memiliki JOSM, atau ingin memiliki JOSM versi terbaru, silakan buka **_web browser_** Anda (dapat menggunakan _Firefox_, _Chrome_, _Opera,_ atau _Internet Explorer_). Pada kolom alamat di bagian atas jendela, kemudian ketik **josm.openstreetmap.de** kemudian tekan **_enter_**. Anda juga dapat menemukan situs JOSM dengan mengetik kata pencarian “JOSM” pada mesin pencarian _google_. Situs JOSM akan tampak seperti di bawah ini.

![0301_Tampilan_situs_JOSM](images/0301_Tampilan_situs_JOSM.png "Tampilan situs JOSM")
_Tampilan situs JOSM_

Silakan pilih _file_ instalasi sesuai dengan sistem operasi komputer Anda. Jika Anda menggunakan komputer dengan sistem operasi _Windows_, klik **_Windows JOSM Installer_** untuk men-_download_ JOSM. Jika Anda memiliki sistem operasi lainnya, klik pada _link_ yang sesuai dengan sistem operasi komputer Anda. Kemudian Anda dapat men-_download-_nya. Pada modul ini kami akan mengasumsikan Anda menggunakan _Windows_, tetapi petunjuknya hampir sama dengan sistem operasi lainnya.  

### **II. Menginstal JOSM**
Setelah Anda berhasil men-_download_ JOSM, sekarang Anda akan menginstal JOSM ke komputer atau laptop Anda. Berikut ini adalah cara-cara untuk melakukan instalasi JOSM:
*   Temukan _file_ instalasi JOSM di dalam komputer Anda. Klik dua kali pada _file_ tersebut untuk memulai instalasi. Kemudian akan muncul jendela _“Do you want to allow this app from an unknown publisher to make changes to your device?_”, lalu klik **_Yes_**.
*   Selanjutnya akan muncul jendela untuk memilih bahasa. Di modul ini hanya akan membahas JOSM yang berbahasa Inggris. Jika bahasa sudah dipilih, silakan klik **_OK_**.

![Tampilan_jendela_installer_language](images/0302_Tampilan_jendela_installer_language.png "Tampilan jendela installer language")
_Tampilan jendela installer language_

*   Kemudian akan muncul jendela selanjutnya mengenai JOSM _Setup Wizard_. Klik **_Next_**.

![Tampilan_JOSM_Setup_Wizard](images/0303_Tampilan_JOSM_Setup_Wizard.png "Tampilan JOSM Setup Wizard")
_Tampilan JOSM Setup Wizard_

*   Selanjutnya akan muncul jendela _License Agreement_. Klik **_I Agree_**.

![Tampilan_jendela_License_Agreement](images/0304_Tampilan_jendela_License_Agreement.png "Tampilan jendela License Agreement")
_Tampilan jendela License Agreement_

*   Berikutnya akan muncul jendela _Choose Components_. Disini Anda dapat memilih apa saja dari bagian JOSM yang ingin Anda _install_. Kemudian klik **_Next_**.

![Tampilan_jendela_choose_components](images/0305_Tampilan_jendela_choose_components.png "Tampilan jendela choose components")
_Tampilan jendela choose components_

*   Selanjutnya akan muncul jendela _Choose Install Location_. Disini Anda dapat memilih folder dimana Anda ingin menginstal JOSM. Kemudian klik **_Install_**.

![Tampilan_jendela_choose_install_location](images/0306_Tampilan_jendela_choose_install_location.png "Tampilan jendela choose install location")
_Tampilan jendela choose install location_

*   Ketika instalasi selesai, klik **_Finish_** untuk membuka JOSM pertama kalinya. Kemudian, ketika  ingin memulai JOSM, Anda dapat melakukannya dengan mengklik pada _Start Menu_ di pojok kiri bawah pada komputer Anda, dan klik program JOSM.  
*   Ketika JOSM terbuka, maka akan terlihat tampilan seperti di bawah ini:

![Tampilan_awal_JOSM](images/0307_Tampilan_awal_JOSM.png "Tampilan awal JOSM")
_Tampilan awal JOSM_

> **Catatan:**
 Anda mungkin memiliki masalah ketika melakukan instalasi JOSM apabila Java belum terinstal di komputer Anda. Jika Anda memiliki masalah ketika melakukan instalasi pada bagian ini, cobalah mendownload dan menginstal Java. Anda dapat mendownloadnya disini: http://www.java.com/en/download/
 Anda mungkin akan melihat sebuah jendela muncul saat pertama kali membuka JOSM yang menanyakan untuk memperbarui perangkat lunak tersebut. Anda tidak perlu memperbaharuinya karena yang baru saja Anda download perangkat lunak baru. Tekan tombol "Cancel". Jika Anda tidak ingin melihat pesan ini lagi, centang kotak di bawah sebelum menekan "Cancel".
JOSM yang digunakan dalam modul ini versi 14760. Tampilan mungkin berbeda jika Anda menggunakan JOSM versi yang lain.

### **III. Mengubah Pengaturan Pada JOSM**
**a. Mengubah Bahasa**
    Banyak pengaturan yang dapat Anda sesuaikan di JOSM. Salah satu pengaturan yang Anda mungkin ingin sesuaikan adalah bahasa. JOSM telah diterjemahkan ke dalam berbagai macam bahasa, dan Anda dapat memilih bahasa yang Anda inginkan.  Berikut ini adalah langkah-langkah untuk mengubah bahasa di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![Menu_preferences_di_JOSM](images/0308_Menu_preferences_di_JOSM.png "Menu preferences di JOSM")
_Menu preferences di JOSM_

*   Pada sisi sebelah kiri, klik ikon **_Display Setting_** yang terlihat seperti kaleng dan kuas cat.

![Ikon_display_setting](images/0309_Ikon_display_setting.png "Ikon display setting")
_Ikon display setting_

*   Di atas jendela, klik tab yang bertuliskan **_Look and Feel_**.
*   Pilihlah bahasa yang Anda inginkan pada kotak daftar pilihan yang bertuliskan **_Language_**. Klik **_OK_** dan kemudian **_restart_** untuk mengganti bahasa JOSM anda ke dalam bahasa yang Anda inginkan. 

![Tampilan_display_setting_untuk_mengganti_bahasa](images/0310_Tampilan_display_setting_untuk_mengganti_bahasa.png "Tampilan display setting untuk mengganti bahasa")
_Tampilan display setting untuk mengganti bahasa_

**b. Mengatur Akun**
Setelah mengubah bahasa yang diinginkan untuk digunakan di JOSM, Anda juga harus memasukkan nama akun OSM Anda serta kata sandinya di dalam JOSM. Tujuannya adalah agar ketika Anda melakukan edit atau menambahkan data di peta OSM, server akan mengenali bahwa hasil edit tersebut dibuat oleh Anda. Jika Anda tidak memasukkan nama akun, maka Anda tidak dapat memasukkan data yang sudah Anda edit atau tambahkan ke dalam peta OSM.  Berikut ini adalah langkah-langkah untuk memasukkan akun OSM Anda di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![Ikon_preferences_di_JOSM](images/0311_Ikon_preferences_di_JOSM.png "Ikon preferences di JOSM")
_Ikon preferences di JOSM_

*   Pada sisi sebelah kiri, klik ikon **_Connection Setting_ **yang terlihat seperti gambar globe atau bola dunia.

![Ikon_connection_setting](images/0312_Ikon_connection_setting.png "Ikon connection setting")
_Ikon connection setting_

*   Pilih **_Authentication → Use Basic Autentication_**.
*   Masukkan nama akun dan kata sandi Anda.

![Tampilan_connection_setting_untuk_memasukkan_nama_akun_dan_kata_sandi](images/0313_Tampilan_connection_setting_untuk_memasukkan_nama_akun_dan_kata_sandi.png "Tampilan connection setting untuk memasukkan nama akun dan kata sandi")
_Tampilan connection setting untuk memasukkan nama akun dan kata sandi_

*   Klik **_OK_** dan kemudian **_restart_ **JOSM Anda.

**c. Menambahkan _Preset_**
Sekarang Anda telah memasukkan nama akun Anda. Selanjutnya adalah pengaturan untuk memasukkan _presets_ di JOSM. _Presets_ adalah sebuah _file_ yang dapat memberikan informasi terkait objek-objek yang Anda petakan di _OpenStreetMap_.  Untuk penjelasan lebih detail tentang presets dan pembuatan _presets_, Anda dapat melihatnya di Panduan Pembuatan _Presets_ di modul **Membuat Preset**. Berikut ini adalah langkah-langkah untuk menambahkan _presets_ di JOSM:

*   Akses jendela _Preferences_, klik **_Edit → Preferences_**.

![Menu_preferences_di_JOSM](images/0314_Menu_preferences_di_JOSM.png "Menu preferences di JOSM")
_Menu preferences di JOSM_

*   Pada sisi sebelah kiri, klik ikon **_Map Setting_** yang terlihat seperti _grid_ atau kotak-kotak.

![Ikon_Map_Setting](images/0315_Ikon_Map_Setting.png "Ikon Map Setting")
_Ikon Map Setting_

*   Dibawah kotak _Available Preset_ cari dan pilih preset yang bernama **_HOT PDC InAWARE Indonesian Project_**. Lalu klik tanda panah biru yang berada di sebelah kanan kotak.  

![Menambahkan_preset_di_JOSM](images/0316_Menambahkan_preset_di_JOSM.png "Menambahkan preset di JOSM")
_Menambahkan preset di JOSM_

Jika Anda sudah memiliki _file presets_ Anda sendiri di komputer Anda, Anda juga dapat langsung memasukkannya dengan cara:
*   Silahkan klik tanda **+** di samping kotak _active presets_. 

![Tanda_+_untuk_menambahkan_preset_dari_komputer](images/0317_Tanda_+_untuk_menambahkan_preset_dari_komputer.png "Tanda + untuk menambahkan preset dari komputer")
_Tanda + untuk menambahkan preset dari komputer_

*   Kemudian ikon **_Open a File_** untuk mencari_ file presets_ Anda.

![Ikon_Open_a_File](images/0318_Ikon_Open_a_File.png "Ikon Open a File")
_Ikon Open a File_

*   Jika sudah ditemukan klik **_Open _**kemudian **_OK_**.

**d. Memasukkan Citra Satelit**
Anda akan menggunakan citra satelit pada saat mengedit peta OSM. Jika koneksi internet Anda stabil pada saat membuka pengaturan JOSM, maka di bagian _**Edit** → **Preferences** → **Imagery Preferences**_, akan otomatis terpilih citra-citra satelit yang sering digunakan. Jika koneksi internet bermasalah dan saat dilihat bagian _Imagery Preferences_ tidak ada citra satelit yang terpilih, coba _restart _JOSM dan lihat kembali di bagian _Imagery Preferences_ apakah citra satelitnya  sudah terpilih atau belum. Jika masih belum terpilih juga, maka berikut ini adalah langkah-langkah untuk menambahkan _presets_ di JOSM:

*   Akses jendela _Preferences_, klik _**Edit** → **Preferences**._

![Ikon_preferences_di_JOSM](images/0319_Ikon_preferences_di_JOSM.png "Ikon preferences di JOSM")
_Ikon preferences di JOSM_

*   Pada sisi sebelah kiri, klik ikon **_Imagery Preferences_** atau yang bertuliskan **WMS TMS**.

![Ikon_imagery_preferences](images/0320_Ikon_imagery_preferences.png "Ikon imagery preferences")
_Ikon imagery preferences_

*   Kemudian klik citra satelit yang ingin Anda pilih (misalnya _Bing, Digital Globe, Mapbox, dan Esri_) pada kotak **_Available default entries_**.
*   Selanjutnya klik tombol **_Activate_** di bawah kotak _Available default entries_.

![Tombol_Activate](images/0321_Tombol_Activate.png "Tombol Activate")
_Tombol Activate_

*   Kemudian Anda akan melihat citra satelit yang sebelumnya Anda pilih sudah masuk ke dalam kotak **_Selected Entries_** seperti gambar di bawah ini. Kemudian klik **_OK _**dan JOSM akan meminta untuk _restart_.

![Tampilan_citra_yang_sudah_dipilih](images/0322_Tampilan_citra_yang_sudah_dipilih.png "Tampilan citra yang sudah dipilih")
_Tampilan citra yang sudah dipilih_

**e. Mengatur Tampilan Gambar Objek**
Pada pengaturan awal di JOSM, setiap objek _OpenStreetMap_ yang ada di JOSM tidak memperlihatkan titik, label, dan ikon dari setiap objek _OpenStreetMap_.

![Contoh_tampilan_awal_JOSM_yang_pengaturannya_belum_diubah](images/0323_Contoh_tampilan_awal_JOSM_yang_pengaturannya_belum_diubah.png "Contoh tampilan awal JOSM yang pengaturannya belum diubah")
_Contoh tampilan awal JOSM yang pengaturannya belum diubah_

Untuk memunculkannya Anda harus mengubah tampilan _style_ peta pada JOSM Anda. Berikut ini adalah langkah-langkah untuk mengubahnya:
*   Klik pada menu **_File → New Layer_** untuk memunculkan panel pada JOSM.
*   Pada bagian kanan di panel JOSM, lihat pada bagian **_Map Paint Styles_**.
*   Jika pada panel JOSM Anda belum ada jendela _Map Paint Styles_, silahkan Anda klik menu **_Windows_** pada sisi atas JOSM Anda, kemudian klik _Map Paint Styles_ untuk mengaktifkan jendela _Map Paint Styles_ di sisi kanan JOSM Anda.

![Tampilan_untuk_mengaktifkan_Map_Paint_Styles](images/0324_Tampilan_untuk_mengaktifkan_Map_Paint_Styles.png "Tampilan untuk mengaktifkan Map Paint Styles")
_Tampilan untuk mengaktifkan Map Paint Styles_

*   Setelah Anda klik, akan muncul jendela _Map Paint Styles _di sebelah kanan bawah JOSM Anda.
*   Klik kanan pada** _JOSM default (Map CSS)_** dan pilih _Style Settings._  
*   Samakan dengan tampilan di bawah ini.

![Pengaturan_Map_Paint_Styles_di_JOSM](images/0325_Pengaturan_Map_Paint_Styles_di_JOSM.png "Pengaturan Map Paint Styles di JOSM")
_Pengaturan Map Paint Styles di JOSM_  

Apabila semua pengaturan sudah disamakan dengan apa yang terlihat seperti di atas, tampilan gambar JOSM Anda nantinya akan memunculkan titik, label, dan ikon untuk setiap objek di _OpenStreetMap_ seperti contoh di bawah ini:

![Contoh_tampilan_awal_JOSM_yang_pengaturannya_sudah_diubah](images/0326_Contoh_tampilan_awal_JOSM_yang_pengaturannya_sudah_diubah.png "Contoh tampilan awal JOSM yang pengaturannya sudah diubah")
_Contoh tampilan awal JOSM yang pengaturannya sudah diubah_

### **IV. Tampilan Antarmuka JOSM**
Sekarang Anda sudah melakukan beberapa pengaturan di JOSM. Agar lebih memudahkan Anda untuk melakukan _editing_, Anda perlu untuk melihat beberapa bagian penting di JOSM. Untuk melihat tampilan antarmuka JOSM, klik pada menu **_File → New Layer_**. Berikut adalah beberapa bagian di antar muka di JOSM.

![Bagian_bagian_pada_tampilan_JOSM](images/0327_Bagian_bagian_pada_tampilan_JOSM.png "Bagian-bagian pada tampilan JOSM")
_Bagian-bagian pada tampilan JOSM_

Pada JOSM terdapat bidang peta, _toolbar_, dan panel. Bidang peta adalah bidang untuk melihat, mengedit, dan menambahkan data _OpenStreetMap_. Pada bagian kanan JOSM terdapat serangkaian panel yang memiliki fungsi tertentu. Biasanya ketika Anda pertama kali menginstal JOSM, beberapa panel yang akan ditampilkan dengan pengaturan standar, seperti _Layer, Selections, Tags/Memberships_, dan _Author_. 

*   Panel **_layers_** akan menampilkan _layer_ apa saja yang ditambahkan ke dalam JOSM, seperti citra satelit, hasil _download_ data OSM, dan sebagainya. 
*   Ketika Anda memilih sebuah objek, baik berupa titik, garis, atau poligon di dalam bidang peta, akan ditampilkan di panel **_selections_**. 
*   Informasi mengenai objek yang akan ditampilkan pada panel **_Tags/Memberships._**
*   Nama pembuat objek akan ditampilkan di panel **_author_**. 

Jika ingin menghilangkan panel-panel tertentu, Anda dapat mengklik tanda **x** pada pojok kanan panel yang ingin hilangkan. Jika ingin menambahkan panel lainnya, Anda dapat mengaktifkannya di menu **_Windows_** dan setelah diaktifkan akan muncul pada panel di sebelah kanan JOSM.

_Toolbar_ samping kiri pada JOSM adalah jendela alat yang berisi beberapa tombol untuk _editing_ seperti tombol **_Select object_** dan _**Draw nodes**_. Di bawahnya adalah alat-alat yang untuk **_zoom and move map, delete nodes or way,_** dan **_create areas_**. Untuk pilihan _toolbar_ lainnya, Anda dapat mengklik tombol dua panah ke kanan warna hitam. Kemudian klik _toolbar_ yang Anda inginkan dan akan muncul di _toolbar_.

![Tombol_untuk_mengatur_toolbar_pada_JOSM](images/0328_Tombol_untuk_mengatur_toolbar_pada_JOSM.png "Tombol untuk mengatur toolbar pada JOSM")
_Tombol untuk mengatur toolbar pada JOSM_

**RINGKASAN**
Jika Anda dapat mengikuti dan mempraktikkan seluruh tahapan dalam modul ini, maka Anda telah berhasil menginstal JOSM di dalam laptop atau komputer Anda. Selain itu, Anda juga telah berhasil mempelajari dan mempraktekkan bagaimana cara melakukan pengaturan standar di JOSM untuk memudahkan pekerjaan Anda. Pada modul selanjutnya Anda akan mempelajari bagaimana cara menambahkan data di JOSM mulai dari tingkat dasar hingga tingkat lanjut. 