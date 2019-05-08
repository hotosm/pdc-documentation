
# Menggunakan Alat Filter di JOSM
**Tujuan Pembelajaran:**
*   Melakukan aktivasi mode penyaring data di JOSM
*   Mengoperasikan alat untuk menyaring data di JOSM

JOSM memiliki berbagai macam alat yang dapat memudahkan penggunanya untuk melakukan pemetaan. Salah satu alat yang dapat digunakan adalah filter. Filter merupakan sebuah alat tambahan untuk memilih salah satu objek berdasarkan informasi (tag) objek di _OpenStreetMap_  (_key_ dan _value_), sehingga Anda dapat mengedit dan memeriksa data OSM berdasarkan informasi tertentu dari suatu objek. Filter juga memudahkan Anda untuk menampilkan dan melihat data berdasarkan informasi tertentu yang ingin Anda lihat. Hal ini sangat membantu ketika Anda ingin memeriksa data yang sangat banyak dan kompleks.   

### I. Mengaktifkan Jendela Filter di JOSM

*   Untuk dapat mengaktifkan jendela filter, silakan Anda pilih menu **_Window_** kemudian pilih **_Filter_**

    <p align="center"><img width=30% src="../images/0701_Mengaktifan_jendela_filter_pada_JOSM.png"</p>
    <p align="center"><i>Mengaktifkan jendela filter pada JOSM</i></p>


*   Jendela filter akan ditampilkan di sebelah kanan layar Anda. 

    <p align="center"><img width=30% src="../images/0702_Jendela_filter_pada_JOSM.png"</p>
    <p align="center"><i>Jendela filter pada JOSM</i></p>

### II. Menggunakan Alat Filter di JOSM

<p align="center"><img width=70% src="../images/0703_Contoh_data_OpenStreetMap_di_Daerah_Cengklik.png"</p>
<p align="center"><i>Contoh data OpenStreetMap di Daerah Cengklik</i></p>

Bayangkan jika Anda mempunyai data seperti gambar di atas. Seringkali tampilan data seperti gambar di atas tersebut terlihat membingungkan karena banyaknya data yang ditampilkan. Untuk itu Anda dapat menggunakan filter untuk menyederhanakan tampilan data tersebut dengan menampilkan objek-objek yang hanya ingin Anda lihat. Sebagai contoh, kita akan melakukan filter untuk objek jalan. Langkah-langkah yang perlu Anda lakukan adalah sebagai berikut:



*   Pada jendela filter, pilih menu **_Add_**. 

    <p align="center"><img width=40% src="../images/0704_Tombol_Add_di_jendela_filter.png"</p>
    <p align="center"><i>Tombol Add di jendela filter</i></p>

*   Pada bagian **_Filter string_**, silakan Anda masukkan informasi _key_ dan _value_ yang ingin Anda filter. Pada kasus ini, silakan Anda tulis _highway=*_ (untuk memilih semua objek jalan yang ada). Kemudian pilih **_Submit filter._**

    <p align="center"><img width=70% src="../images/0705_Tampilan_filter.png"</p>
    <p align="center"><i>Tampilan filter</i></p>

*   Pada jendela filter Anda akan melihat tiga buah kotak yang dapat anda _checklist_. 

    <p align="center"><img width=40% src="../images/0706_Hasil_filter.png"</p>
    <p align="center"><i>Hasil filter</i></p>

1. Jika Anda aktifkan kotak di angka 1, maka objek jalan akan disembunyikan namun terlihat pada _layer_ peta dengan warna hitam pekat
    <p align="center"><img width=70% src="../images/0707_Hasil_filter_1.png"</p>
    <p align="center"><i>Hasil filter 1</i></p>

2. Jika Anda aktifkan kotak di angka 1 dan 2, maka objek jalan akan disembunyikan sepenuhnya dan tidak terlihat sama sekali di _layer_ peta
    <p align="center"><img width=70% src="../images/0708_Hasil_filter_2.png"</p>
    <p align="center"><i>Hasil filter 2</i></p>

3. Jika Anda aktifkan kotak di angka 1, 2 dan 3, maka _layer_ peta hanya akan menampilkan objek jalan di JOSM
    <p align="center"><img width=70% src="../images/0709_Hasil_filter_3.png"</p>
    <p align="center"><i>Hasil filter 3</i></p>


Perlu diingat bahwa ketika Anda menggunakan fungsi filter pada JOSM, hasil filter tersebut akan secara otomatis selalu muncul meskipun Anda sudah menutup _software_ JOSM ataupun berpindah lokasi pada saat melakukan pemetaan. Hal ini dapat menimbulkan masalah karena jika Anda memetakan daerah lain dengan fungsi filter yang sama, objek jalan yang ada di daerah tersebut menjadi tidak terlihat dan bisa saja Anda petakan lagi, padahal jalan tersebut sudah dipetakan sebelumnya. Oleh karena itu, pastikan Anda menonaktifkan hasil filter terlebih dahulu setelah selesai menggunakan fungsi tersebut. Untuk melihat apakah fungsi filter masih aktif pada JOSM, Anda dapat melihat melihatnya pada bagian kanan atas bidang peta di JOSM. Jika tulisan _Filter active_ masih muncul maka hal itu  menandakan bahwa fungsi filter masih aktif. 

<p align="center"><img width=70% src="../images/0710_Filter_active_yang_menandakan_fungsi_filter_masih_aktif_pada_JOSM.png"</p>
<p align="center"><i>Filter active yang menandakan fungsi filter masih aktif pada JOSM</i></p>

Untuk menghapus filter yang masih aktif, silakan pilih hasil filter yang ingin Anda hapus di jendela filter, setelah itu pilih tombol **_Delete_**.

<p align="center"><img width=40% src="../images/0711_Pilih_tombol_Delete_untuk_menghapus_hasil_filter.png"</p>
<p align="center"><i>Pilih tombol Delete untuk menghapus hasil filter</i></p>

Setelah Anda berhasil menghapus hasil filter tersebut, maka tampilan data _OpenStreetMap_ Anda akan kembali seperti semula.




<p align="center"><img width=70% src="../images/0712_Tampilan_Data_OpenStreetMap_setelah_fungsi_filter_dihapus.png"</p>
<p align="center"><i>Tampilan Data OpenStreetMap setelah fungsi filter dihapus</i></p>

>Catatan :
Saat Anda menggunakan fungsi filter pada JOSM, hasil filter tersebut akan selalu muncul pada saat Anda membuka JOSM. Pastikan Anda selalu menghapus fungsi filter setelah Anda menggunakannya!



**RINGKASAN**
<br>Jika Anda telah berhasil mengikuti semua langkah-langkah yang ada, pada akhir  modul ini Anda telah berhasil mengetahui apa itu mode filter atau mode penyaringan data di JOSM. Anda juga telah mampu mengoperasikan mode filter di JOSM untuk memilih data mana saja yang ingin Anda lihat. Silakan Anda gunakan filter untuk membantu proses pemetaan Anda supaya menjadi lebih mudah. 



