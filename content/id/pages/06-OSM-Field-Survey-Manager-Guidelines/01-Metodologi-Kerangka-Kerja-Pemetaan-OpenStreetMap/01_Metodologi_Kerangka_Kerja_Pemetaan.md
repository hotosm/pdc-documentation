---
title: Metodologi Perencanaan Proyek Pemetaan dengan OpenStreetMap
weight: 1
---


  **Tujuan Pembelajaran:**

*   Memahami cara membuat kerangka kegiatan pemetaan
*   Memahami cara pembagian arsip untuk masing-masing kelompok survei
*   Memahami cara pembagian area survei berdasarkan batas administrasi
*   Mengetahui cara pembagian kelompok yang efektif 

Perencanaan proyek pemetaan memerlukan metodologi survei yang tepat dan efisien untuk mencapai target dan tujuan pemetaan. Indikator-indikator yang perlu diperhatikan dalam pembuatan metodologi survei meliputi: luas wilayah survei, jumlah tim pemetaan, jumlah objek yang dikumpulkan, dan pendanaan proyek. Jika luas wilayah semakin besar dan jumlah objek yang dikumpulkan semakin banyak, maka pendanaan proyek juga semakin besar. 

Pada proyek pemetaan survei lapang akan dilaksanakan oleh tim pemetaan yang dibagi menjadi 3 (tiga) peran, 
yaitu :


*   _Mapping Supervisor_ = mengatur dan mengawasi jalannya proyek pemetaan, mempersiapkan keperluan pemetaan, membuat laporan hasil pemetaan dan memeriksa kualitas dan kuantitas data yang telah divalidasi oleh _Quality Assurance_.
*   _Quality Assurance_= menjamin kuantitas dan kualitas data yang dihasilkan oleh _data entry_ dan mengawasi _data entry_ dalam melakukan survei lapangan.
*   _Data Entry_ = melaksanakan survei lapangan dan memasukkan data lapangan ke dalam OSM beserta digitasi bangunan dan jalan.


### **I. Pembuatan Kerangka Kerja**

Perencanaan pemetaan memerlukan suatu kerangka kerja yang disesuaikan dengan indikator-indikator pemetaan yang telah disebutkan sebelumnya. Kerangka kerja tersebut dapat dijadikan acuan dalam pelaksanaan proyek pemetaan yang akan dimonitor oleh _Mapping Supervisor_ dan _Quality Assurance_. Kerangka kerja secara garis besar terdiri dari:


*   Persiapan proyek pemetaan
*   Penentuan jumlah tim _data entry_ dan tim _quality assurance_
*   Pelaksanaan pelatihan OSM untuk tim pemetaan
*   Proses pemetaan dan kegiatan mapathon
*   Pelaksanaan pelatihan QGIS untuk tim pemetaan
*   Pembuatan peta akhir

Sebagai contoh, dibawah ini merupakan kerangka kerja yang disusun untuk pemetaan di Kota Semarang tahun 2018 yang memiliki luas wilayah 373,8 km<sup>2</sup> dengan jumlah _data entry_ 16 orang dan jumlah _quality assurance_ 4 orang. Infrastruktur yang dikumpulkan berjumlah 58 kategori objek meliputi jaringan jalan, sungai, tanggul dan fasilitas umum. Semua tahapan-tahapan pemetaan dilakukan selama 6 bulan.


![kerangka_kerja](/id/images/06-OSM-Field-Survey-Manager-Guidelines/01-Metodologi-Kerangka-Kerja-Pemetaan-OpenStreetMap/0101_Kerangka_kerja_pemetaan.png)
<p align="center"><i>Kerangka kerja pemetaan</i></p>

#### **a. Pelatihan _OpenStreetMap_ dan QGIS untuk tim Pemetaan**

Pelatihan ini dilakukan untuk memberikan pemahaman terhadap metode pemetaan, penggunaan alat-alat survei lapangan, dan pembuatan peta cetak hasil survei lapang. Berikut ini pelatihan yang dapat Anda persiapkan sebelum pemetaan berlangsung :

*   Pelatihan _OpenStreetMap_ untuk _Data Entry_ dan _Quality Assurance_

Pelatihan dilakukan selama 3 hari, bertujuan untuk menggunakan alat-alat survei lapangan dan memasukkan hasil data survei ke dalam OpenStreetMap. Materi pelatihan yang diberikan, sebagai berikut: 

1. Memulai OpenStreetMap
2. Pengoperasian JOSM
3. Penggunaan Alat-Alat Survei (OpenMapKit, ODK Collect, OSMTracker, dan GPS)
4. Praktik Survei Lapang
5. Penggunaan Tasking Manager
6. Memasukkan Hasil Survei ke dalam OSM dengan menggunakan JOSM
7. Download Data OSM dengan Export Tool

*   Pelatihan Validasi Data untuk _Quality Assurance_

Pelatihan dilakukan selama 2 hari,  bertujuan untuk melakukan validasi data yang sudah dimasukkan oleh _data entry_ ke dalam _OpenStreetMap_. Materi pelatihan yang diberikan, sebagai berikut: 

1. Validasi Data OSM menggunakan JOSM
2. Validasi Data OSM menggunakan Tasking Manager
3. Membuat Batas Administrasi dengan Relasi

*   Pelatihan QGIS untuk _Data Entry_ dan _Quality Assurance_

Pelatihan dilakukan selama 1 hari, bertujuan untuk membuat peta hasil survei lapang yang telah divalidasi oleh _Quality Assurance_ dan _Mapping Supervisor_. Materi pelatihan yang diberikan, sebagai berikut: 

1. Download dan Install QGIS
2. Persiapan data 
3. Analisis Vektor
4. Pembuatan peta dengan Map Composer

#### **b. Persiapan Mapathon**

Mapathon adalah pemetaan yang dilakukan secara bersama-sama secara partisipatif dengan menggunakan _tasking manager_. Anda dapat bekerja sama dengan pihak universitas untuk membantu memetakan bangunan dan jalan di wilayah pemetaan Anda. Hal ini sangat efektif untuk membantu pemetaan sehingga _data entry_ dapat berfokus pada survei lapangan dan mempersingkat durasi pemetaan. Juga dapat menjalin kerjasama guna keberlanjutan data _OpenStreetMap_ di wilayah tersebut. Kegiatan mapathon dapat dilakukan selama 3 hari, dengan kegiatan di hari pertama diisi dengan pelatihan, kemudian hari kedua dan ketiga diisi dengan kegiatan pemetaan.

### **II. Pembuatan _Timeline_ Survei Pemetaan**

_Timeline_ survei pemetaan berbeda dengan kerangka kerja yang sebelumnya telah dibahas, pada bagian ini akan ditekankan bagaimana Anda dapat mengatur dan mengawasi pelaksanaan survei lapangan. Secara garis besar _timeline_ pemetaan terbagi menjadi tiga bagian, yaitu : 

#### 1. **Sebelum Survei Pemetaan**

Pada tahapan ini, kegiatan yang dilakukan akan berfokus pada persiapan peralatan survei. Peralatan survei lapangan terdiri dari GPS, _smartphone_ dan peta cetak. Semua peralatan itu harus dipersiapkan sebelum survei pemetaan dilaksanakan oleh _data entry._ Pada _smartphone_ akan dipasang aplikasi _ODK Collect, OpenMapKit (OMK)_, dan _OSMTracker_, dimana aplikasi OMK membutuhkan dua jenis data yang harus dipersiapkan yaitu batas administrasi dalam format *.osm* dan citra satelit dalam format _.mbtiles_. Peran _mapping supervisor_ sangat dominan di dalam bagian sebelum survei pemetaan, dimana mereka harus mempersiapkan peralatan yang diperlukan dalam pemetaan. Persiapan survei pemetaan terdiri dari:

*   Membuat MBTiles untuk citra satelit
*   Membuat peta survei berdasarkan batas administrasi
*   Membuat panduan survei pemetaan

Contoh Tabel _Timeline_ Pemetaan Tahap Sebelum Survei

| No | Timeline | Tim *Surveyor* | Kec | Jumlah Kel | Kel | Jumlah RW | *MBTiles* | Peta Kel (satelit) | Peta Kel (OSM) |
|---|---|---|---|---|---|---|---|---|---|
|1| Feb - Mar| A | Candisari | 3 | Candi | 11 | v | v | v |
|| | |100% Dipetakan | | Jatingaleh | 10 | v | v | v |
|| | |100% Divalidasi | | Jomblang | 10 | v | v | v |
|2| Feb - Mar| B | Banyumanik | 3 | Sumurboto | 5 | v | v | v |
|| | |100% Dipetakan | | Ngesrep | 11 | v | v | v |
|| | |100% Divalidasi | | Gedawang | 10 | v | v | v |

_*Pengisian dilakukan oleh Mapping Supervisor_

**b. Survei Pemetaan**

Pada saat proses survei pemetaan, masing-masing tim memiliki peran agar survei pemetaan dapat terlaksana dengan baik, yaitu:

*   _Data Entry_ = mempersiapkan peralatan survei pada _smartphone_, melaksanakan survei, memasukkan data survei dan meng-_upload_ ke dalam OSM, digitasi bangunan dan jalan dengan menggunakan JOSM.
*   _Quality Assurance_ = memastikan dan mengawasi kualitas data yang telah di-_upload_ oleh _data entry_, memastikan dan mengawasi pelaksanaan survei yang dilakukan oleh _data entry_ di lapangan, serta mengatur strategi kegiatan survei lapangan bersama _data entry._
*   _Mapping Supervisor_ = memastikan kualitas dan kuantitas data serta memantau pelaksanaan survei yang disesuaikan dengan _timeline_ yang telah ditetapkan.

Contoh Tabel *Timeline* Pemetaan Tahap Survei Pemetaan

|input mbtiles|*clear file manager*|Tgl Survei|Tgl Survey Batas RW|Infrastruktur|Posko|Jalur Evakuasi|Upload track|Kirim form ke OMK Server|Infrastruktur|RW|Jalur Evakuasi dan Posko|Tgl Validasi Data|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v | v | 1,5-6 Mar 2018 | 1 Mar 2018 | v | Ada | Tidak Ada | v | v | v | v | v | 26 Mar 2018 |
| v | v | 12 Feb 2018 | 12 Feb 2018 | v | Ada | Tidak Ada | v | v | v | v | v | 14, 19 Feb 2018 |
| v | v | 8,12-14 Mar 2018 | 12 Mar 2018 | v | Ada | Tidak Ada | v | v | v | v | v | 27-28 Mar 2018 |

#### **c. Setelah Survei Pemetaan**

Jika seluruh proses pemetaan sudah selesai, maka _mapping supervisor_ dan _quality assurance_ harus memastikan keseluruhan data yang dimasukkan ke dalam OSM memiliki kualitas yang baik dan bebas dari kesalahan. Langkah selanjutnya adalah pembuatan peta akhir yang diberikan untuk pemerintah lokal yang terlibat dalam proses survei lapangan.

Contoh Tabel _Timeline_ Pemetaan Tahap Setelah Survei 

| **Validasi Batas Administrasi**| **Perhitungan Kuantitas Data**| **Perhitungan Kualitas Data** | **Peta Cetak dan Distribusi**|
|---|---|---|---|
| v | v | v | v |
| v | v | v | v |
| v | v | v | v |

Contoh kelengkapan _timeline_ pemetaan dapat diunduh di tautan berikut [https://tinyurl.com/timeline-pemetaan](https://tinyurl.com/timeline-pemetaan)

### **III. Pembuatan dan Pengaturan Folder Kerangka Kerja Pemetaan**

Dalam mengatur dan memantau kerangka kerja pemetaan, Anda memerlukan suatu tempat penyimpanan data yang terorganisasi dan mempermudah pendistribusian ke semua pihak yang terlibat dalam proyek pemetaan. Hasil pemetaan terdiri dari data spasial yang akan di-_upload_ ke dalam _OpenStreetMap_. Data tersebut akan di _download_ kembali dan disimpan dalam beberapa format data spasial yang disesuaikan dengan _output_ pemetaan.  

_Database_ dapat disimpan dalam bentuk _file_ digital yang bersifat _online_, agar mudah pendistribusian kepada _data entry_ dan _quality assurance_. Nantinya data tersebut akan dipantau  juga oleh _mapping supervisor_, sebagai pengecekan dan perhitungan untuk kalkulasi data. 

Tempat penyimpanan yang mudah dari segi penggunaan dan pengaplikasian yaitu _google drive_. _Google drive_ dapat menyimpan berbagai jenis data dan dapat dibagikan kepada semua orang. _Mapping supervisor_ dapat membuat suatu folder didalam _google drive_ yang terdiri dari:

Contoh Tabel Folder Proyek Pemetaan

| **Nama Folder**| **Deskripsi**|
|---|---|
|_Timeline_| Kerangka kerja dan _timeline_ survei pemetaan|
|_Training_| Agenda pelatihan dan materi pelatihan|
|Tim Pemetaan| Daftar nama tim pemetaan (_data entry, quality assurance, dan mapping supervisor_)|
|Data Survei| Hasil pemetaan OpenMapKit (OMK) dan ODK Collect, batas administrasi, tempat pengungsian, jalur evakuasi, dll.|
|Dokumentasi Survei| Foto dan video selama kegiatan survei|
|Peta| Peta survei, _fieldpapers_, dan peta hasil|
|Laporan| Laporan perbulan yang dibuat oleh _quality assurance_ dan _mapping supervisor_|
|Kualitas Data| Perhitungan kualitas data yang dihasilkan sebelum dan sesudah pemetaaan|
|Kuantitas Data|Perhitungan kuantitas data yang dihasilkan sebelum dan sesudah pemetaaan|
|OMK _Equipment_| Peralatan survei yang dibutuhkan oleh OMK seperti MBTiles|

Data-data digital harus di-_upload_ ke dalam folder tersebut seiring dengan berjalannya proyek pemetaan, agar data tersebut dapat di-_backup_ dengan baik dan tidak ada data yang hilang atau rusak.

![gdrive](/id/images/06-OSM-Field-Survey-Manager-Guidelines/01-Metodologi-Kerangka-Kerja-Pemetaan-OpenStreetMap/0102_Contoh_folder_Google_Drive.png)
</p>
<p align="center"><i>Contoh folder di dalam Google Drive</i><p align="center">
 
### **IV. Pembagian Wilayah Survei Berdasarkan Batas Administrasi**

Luas wilayah, topografi, dan penggunaan lahan suatu wilayah sangat menentukan pembagian wilayah dan durasi pemetaan dalam survei. Pembagian wilayah dapat dibagi berdasarkan unit terkecil dari wilayah administrasi misalnya tingkat kelurahan. Jika Anda telah memiliki batas-batas kelurahan yang ada di dalam wilayah tersebut, maka Anda dapat memperhatikan aspek selanjutnya yaitu topografi dan penggunaan lahan. 

Misalnya pemetaan yang dilakukan di Kota Semarang memiliki luas wilayah 373,8 km<sup>2</sup> yang terdiri dari 16 kecamatan dan 177 kelurahan. Topografi yang dimiliki Kota Semarang mempengaruhi karakteristik wilayahnya yang terbagi menjadi dua bagian yaitu wilayah pesisir (Semarang Bawah) dan wilayah perbukitan (Semarang Atas). Wilayah semarang bawah merupakan pusat aktivitas perekonomian, pemerintahan, dan permukiman. Sedangkan wilayah Semarang Atas merupakan perkembangan permukiman, fasilitas pendidikan, dan perkebunan. Oleh karena itu, Semarang bawah memiliki infrastruktur yang lebih padat dibandingkan dengan Semarang atas. 

Analisis ketinggian wilayah dapat mempengaruhi dalam hal rute perjalanan saat _data entry_ melaksanakan survei lapangan karena masing-masing wilayah padat pemukiman dan wilayah perbukitan memiliki hambatan tersendiri. Faktor lainnya yang harus diperhatikan yaitu kondisi cuaca saat pemetaan dilakukan, musim hujan dapat menjadi penghambat survei lapangan, terutama di wilayah yang rawan banjir. Jika curah hujan tinggi, Anda dapat mengarahkan _data entry_ ke lokasi yang tidak rawan banjir terlebih dahulu.

Setelah Anda mengetahui faktor-faktor yang menentukan durasi pemetaan, Anda dapat membagi wilayah survei berdasarkan batas administrasi kecamatan atau kelurahan. Misalnya satu kecamatan dapat diselesaikan dalam waktu satu bulan dan dikerjakan oleh satu tim kelompok survei yang terdiri dari beberapa orang _data entry_. Berdasarkan analisis tersebut, pemetaan di Kota Semarang dapat diselesaikan dalam waktu 4 bulan dengan melibatkan 16 orang _data entry_.   

Tahapan pembagian wilayah untuk bulan pertama dapat dilakukan dengan area yang dekat dengan _basecamp_/kantor agar memudahkan dalam hal koordinasi penggunaan alat yang dilakukan oleh _data entry._ Jika _data entry_ menemukan masalah di lapangan, maka mereka dapat kembali ke kantor dengan jarak yang tidak terlalu jauh dari lokasi survei.

![timeline](/id/images/06-OSM-Field-Survey-Manager-Guidelines/01-Metodologi-Kerangka-Kerja-Pemetaan-OpenStreetMap/0103_peta_timeline.png)
<p align="center"><i>Peta timeline pemetaan Kota Semarang</i><p align="center">
   
Pada peta perencanaan pemetaan Kota Semarang dibawah ini, dibagi menjadi dua bagian berdasarkan karakteristik wilayah, sehingga diperlukan dua orang _mapping supervisor_ untuk mengatur dan memantau kegiatan pemetaan.

![peta](/id/images/06-OSM-Field-Survey-Manager-Guidelines/01-Metodologi-Kerangka-Kerja-Pemetaan-OpenStreetMap/0104_peta_survey.png)
<p align="center"><i>Peta pembagian wilayah Kota Semarang</i><p align="center">

Contoh Tabel _Timeline_ Pembagian Wilayah

|_Timeline_| Wilayah Kecamatan| _Mapping Supervisor_ Utara - Semarang Bawah| _Mapping Supervisor_ Selatan - Semarang Atas |
|---|---|---|---|
|Tahap 1 (1,5 Bulan)|Kecamatan yang dekat dengan kantor/_basecamp_. Misalnya berjarak kurang dari 20 km dari kantor| Kec Semarang Barat | Kec Candisari |
|| | Kec Semarang Tengah | Kec Semarang Selatan |
|| | Kec Semarang Timur | Kec Gayamsari |
|| | Kec Semarang Utara | Kec Gajah Mungkur |
|Tahap 2 (2,5 Bulan)|Kecamatan lebih dari 20 km| Kec Ngaliyan | Kec Banyumanik |
|| | Kec Pedurungan | Kec Tembalang |
|| | Kec Tugu | Kec Mijen |
|| | Kec Genuk | Kec Gunung Pati |

### **V. Pembagian Kelompok Tim Pemetaan**

Aspek pembagian wilayah sangat menentukan dalam pembagian kelompok survei, terutama untuk pendistribusian _data entry_. Anda dapat memilih berdasarkan orang-orang yang sudah mengenal wilayah tersebut. Untuk mendapatkan informasi tersebut, Anda dapat mencantumkan pertanyaan wilayah mana saja yang mereka pahami pada saat tahap penerimaan _data entry_ yang baru. Berdasarkan pembagian wilayah yang sudah dijelaskan sebelumnya, maka tim pemetaan memiliki bagan sebagai berikut:

![kelompok](/id/images/06-OSM-Field-Survey-Manager-Guidelines/01-Metodologi-Kerangka-Kerja-Pemetaan-OpenStreetMap/0105_bagan_kelompok.png)
<p align="center"><i>Bagan pembagian kelompok</i><p align="center">

Tabel Pembagian Kelompok Berdasarkan Wilayah Survei

| **_Mapping Supervisor_**|**_Quality Assurance_**| **_data entry_**| **Kecamatan**| **Jml Kelurahan**| **Total Kelurahan**|
|---|---|---|---|---|---|
|**Mapping Supervisor 1**| QA1 | DE1 | Candisari | 7 | 21 |
| | | DE2 | Mijen | 14 |  |
| | | DE3 | Semarang Selatan | 10 | |
| | | DE4 | Banyumanik | 11 | |
| | QA2 | DE5 | Gayamsari | 7 | 23 |
| | | DE6 | Gunung Pati | 16 | |
| | | DE7 | Gajah Mungkur | 8 | 20 |
| | | DE8 | Tembalang | 12 | |
|**Mapping Supervisor 2**| QA3 | DE9 | Semarang Barat | 16 | 23 |
| | | DE10 | Tugu | 7 |  |
| | | DE11 | Semarang Tengah | 15 | 25 |
| | | DE12 | Ngaliyan | 10 | |
| | QA4 | DE13 | Semarang Timur | 10 | 23 |
| | | DE14 | Genuk | 13 | |
| | | DE15 | Semarang Utara | 9 | 21 |
| | | DE16 | Pedurungan | 12 | |

**RINGKASAN**

Jika Anda dapat mengikuti dan memperhatikan seluruh tahapan dalam bab ini, maka Anda telah berhasil membuat perencanaan proyek pemetaan yang nantinya dapat diaplikasikan ketika survei pemetaan berlangsung. Perencanaan proyek yang tepat akan menghasilkan kualitas dan kuantitas data yang maksimal.
