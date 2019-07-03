---
title: Menggunakan To-Do List di JOSM
weight: 6
---

**Tujuan Pembelajaran:**

*   Mampu melakukan instalasi alat tambahan untuk memasukkan data di JOSM
*   Mampu mengoperasikan alat tambahan _to-do list_ di JOSM untuk memasukkan data

Setelah melakukan kegiatan survei dengan menggunakan aplikasi _OpenMapKit_ (OMK), langkah selanjutnya yang perlu Anda lakukan ialah memasukkan data survei berupa objek-objek titik lokasi tersebut ke dalam _OpenStreetMap_ dengan menggunakan JOSM. Untuk memudahkan Anda dalam melakukan hal tersebut, Anda perlu menginstal perangkat tambahan pada JOSM yaitu _plugin_ **_Todo list_**. _Plugin Todo list_ merupakan perangkat tambahan yang dapat membantu Anda untuk menemukan objek hasil survei yang akan Anda _upload_ pada peta _OpenStreetMap_ (OSM). 

### **I. Menginstal _to-do list_  _plugin_ di JOSM**

Karena plugin _Todo list_ merupakan perangkat tambahan pada JOSM, Anda perlu melakukan instalasi _plugin_ JOSM terlebih dahulu sebelum menggunakannya. Langkah-langkah untuk menginstal _plugin todo list_ di JOSM adalah sebagai berikut:

*   Klik menu bar **_Edit → Preferences_**
*   Akan muncul jendela **_Preferences_** dan pilih menu **_Plugins_** untuk menginstal _plugins_ baru. Jika daftar _plugins_ belum muncul, Anda dapat mengklik **_Download list_** dan pastikan internet Anda telah terkoneksi untuk men-_download_ _plugins_.

![jendela_preferences](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0601_download_plugin.png)
<p align="center"><i>Tampilan kotak jendela Preferences untuk menu pilihan Plugins</i></p>

*   Untuk mencari _plugin todo list_ Anda dapat menggunakan kotak pencarian **_Search_**. Lalu  ketikkan **todo** pada kolom pencarian tersebut untuk menemukan _plugin_ _todo list_. Setelah pencarian berhasil, Anda perlu mencentang kotak _plugin_ **todo** untuk men-_download_ _plugin_ tersebut dan klik **_OK_** lalu tunggu sampai proses men-_download_ selesai.

![tampilan_hasil_pencarian](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0602_search_plugin.png)
<p align="center"><i>Tampilan hasil pencarian plugin todo</i></p>

*   Kotak jendela _plugin_ **todo** akan muncul di sebelah kanan kanvas peta dan apabila kotak todo tersebut belum muncul, Anda dapat mengaktifkan panel _plugin_ **todo** dengan cara klik pada bar menu **Windows**, kemudian klik menu **_todo_** Anda akan melihat panel **_Todo list_** di sebelah kanan JOSM Anda.

![jendela_todo_list](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0603_plugin_trinstal.png)
<p align="center"><i>Tampilan jendela plugin todo list yang telah terinstal</i></p>

### **II. Menggunakan _to-do list_**

Langkah-langkah penggunaan _plugin to-do list_ adalah sebagai berikut:

*   Anda perlu memasukkan terlebih dahulu semua _file_ dengan format _.osm_ yang akan dimasukkan kedalam _OpenStreetMap (OSM)_. _File .osm_ ini berisi objek titik hasil survei yang telah diekspor dari _OpenMapKit_ (OMK) dengan cara klik **_File → Open_** pada menu bar.
*   Dikarenakan satu _file_ berisi satu titik objek, Anda perlu menggabungkan _layer-layer_ tersebut hingga menjadi satu _layer_. Cara menggabungkan ialah pada panel **Layers** pilih semua _layer_ yang akan digabungkan lalu klik kanan dan pilih **_Merge_**. Anda dapat memilih beberapa _layer_ sekaligus dengan cara klik pada salah satu _layer_ lalu tahan untuk untuk memilih semua layer pada panel atau klik layer satu persatu dengan menekan tombol **Ctrl** pada keyboard Anda.

![menggabungkan_beberapa_layer](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0604_merge.png)
<p align="center"><i>Menggabungkan beberapa layer yang berbeda menjadi satu layer</i></p>

*   Setelah semua objek titik telah tergabung menjadi satu _layer_, Anda perlu memilih salah satu objek yang ingin Anda kerjakan. Setelah itu, Anda dapat memasukkan titik-titik objek tersebut ke dalam daftar _to-do list_ dengan cara klik **_Add_** pada panel _Todo list_.

![memasukkan_daftar_objek](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0605_input_panel.png)
<p align="center"><i>Memasukkan daftar objek ke dalam panel Todo list</i></p>

*   Untuk memperbesar tampilan ke salah satu objek yang ingin Anda kerjakan, Anda dapat menggunakan pilihan **_Zoom_** pada panel _Todo list_ atau klik dua kali pada objek di dalam daftar.

![memperbesar_objek](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0606_perbesar_objek.png)
<p align="center"><i>Memperbesar ke objek pada daftar Todo list</i></p>

*   Setelah Anda menemukan objek yang ingin dikerjakan dan telah melakukan perubahan yang diperlukan, Anda dapat menandai objek tersebut pada daftar todo untuk menghilangkan nama objek dari daftar dengan cara mengklik _**Mark**_ pada panel **_Todo list_**. Anda juga menandai dengan memilih objek langsung pada peta dengan cara pilih dan klik objek pada peta lalu klik **_Mark selected_**. Untuk memahami langkah pada proses penambahan data OSM, Anda dapat mempelajari modul **Menambahkan Data OSM Menggunakan JOSM**.

![menandai_objek_dengna_mark](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0607_tombol_mark.png)
<p align="center"><i>Menandai objek dengan opsi Mark</i></p>

*   Apabila Anda ingin melewati satu objek tetapi masih ingin meninggalkan objek tersebut di dalam daftar untuk dikerjakan kemudian, Anda dapat mengklik **_Pass_**.

![tombol_pass](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0608_tombol_pass.png)
<p align="center"><i>Melewati objek dengan pilihan Pass</i></p>

*   Untuk menandai langsung semua objek di daftar Anda bisa menggunakan pilihan **_Mark All_** dengan cara klik kanan pada panel **_Todo list_**. Lalu apabila Anda ingin memunculkan kembali semua objek yang telah ditandai seperti semula, Anda dapat menggunakan pilihan **_Unmark all_**. Anda juga dapat menghapus seluruh daftar nama objek pada panel **_Todo list_** dengan cara klik kanan pada panel dan klik **_Clear the todo list_**.

![pilihan_panel](/pages/03-JOSM/06-Menggunakan-to-do-list-di-JOSM/images/0609_pilihan_panel.png)
<p align="center"><i>Beberapa pilihan pada panel Todo list</i></p>

**RINGKASAN**

Jika Anda dapat mengikuti dan memperhatikan seluruh tahapan dalam bab ini, maka Anda telah berhasil memasang perangkat tambahan di JOSM. Selain itu, Anda juga telah berhasil mempelajari dan mempraktikkan bagaimana cara mengoperasikan _plugin Todo list_ di JOSM untuk memudahkan pekerjaan Anda nantinya. 
