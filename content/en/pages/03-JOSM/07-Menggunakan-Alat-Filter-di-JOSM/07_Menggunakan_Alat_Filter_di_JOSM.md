---
title: Using Filter on JOSM
weight: 7
---

**Objectives:**

* To be able to activate data filtering mode on JOSM
* To be able to operate a data filtering tool on JOSM

JOSM has many tools that can be used by the user to make mapping things easier, like a filter tool. Filter tool is an additional tool that allows you to select or shown only certain objects on JOSM based on key and value on OpenStreetMap. With these tools, you can edit or check specific data on OSM. Filter tool allows you to see only an object based on its attribute, so you don’t need to look at all the data if you only want to look at specific objects. 

  

### **I. Activating Filter Window on JOSM**

*   To activate filter window, you can click **Window** then click **Filter**
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0701_Mengaktifan_jendela_filter_pada_JOSM.png "image_tooltip")
<p align="center"><i>Activate window filter on JOSM</i></p>

*   Window filter will show up on the right side of your screen.
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0702_Jendela_filter_pada_JOSM.png "image_tooltip")
<p align="center"><i>Window filter on JOSM</i></p>

### **II. Using Filter Tool on JOSM**
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0703_Contoh_data_OpenStreetMap_di_Daerah_Cengklik.png "image_tooltip")
<p align="center"><i>Example of OpenStreetMap Data on Cengklik Area</i></p>

Imagine that you have data set like the picture above. Most people will get confused when they see complicated data like that. To make it simpler, you can use filters to select which object you want to see on the JOSM. For example, we will do filtering for highway. For doing so, you need to follow these steps:

*   On filter window, click **Add** menu. 
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0704_Tombol_Add_di_jendela_filter.png "image_tooltip")
<p align="center"><i>Add button on window filter</i></p>

*   On **Filter string** section, you need to input the key and value that you want to be filtered. In this example, please write highway=* (if you want to select all highway object available). After that, select **Submit filter.** 
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0705_Tampilan_filter.png "image_tooltip")
<p align="center"><i>Filter view</i></p>

*   On the filter window, you will see three checklist square.
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0706_Hasil_filter.png "image_tooltip")
<p align="center"><i>Filter result</i></p>

1. If you only activate square checkbox on number 1, all highway object will be shown as hidden but you still can see the object in the shade of black color. 
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0707_Hasil_filter_1.png "image_tooltip")
<p align="center"><i>Filter result 1</i></p>

2. If you activate checkbox number 1 and number 2, then all highway object will be shown as fully hidden on layer window.
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0708_Hasil_filter_2.png "image_tooltip")
<p align="center"><i>Filter result 2</i></p>

3. If you activate checkbox on number 1, 2 and 3, then you will only see highway object on JOSM.
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0709_Hasil_filter_3.png "image_tooltip")
<p align="center"><i>Filter result 3</i></p>


Remember when you using filter on JOSM, the result of your filter will always automatically show up even if you close you JOSM or change the location of your mapping area. If these things happen, it will cause another problem. If you still on the same filter mode (highway=*) and you change your mapping area, you will not see the existing highway on your mapping area. If you’re not careful enough, there are any changes you can make mistakes and draw the same exact highway existing before. Therefore, please make sure you already turn off filtering mode after you finish using filter function. You can check whether your filter mode is activated by checking your right side of your map canvas on JOSM. If you see Filter active still come up, it means that filter mode is currently active.

![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0710_Filter_active_yang_menandakan_fungsi_filter_masih_aktif_pada_JOSM.png "image_tooltip")
<p align="center"><i>Filter active shows that filter function is still activated</i></p>

To delete active filter, select which filter you want to erase on filter window, then select **Delete** button. 

![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0711_Pilih_tombol_Delete_untuk_menghapus_hasil_filter.png "image_tooltip")
<p align="center"><i>Select Delete button to erase your filter result</i></p>

After you delete the filter mode, you can see your OpenStreetMap data as it should be with the whole object show up on the map canvas. 
![alt_text](/en/images/03-JOSM/07-Menggunakan-Alat-Filter-di-JOSM/0712_Tampilan_Data_OpenStreetMap_setelah_fungsi_filter_dihapus.png "image_tooltip")
<p align="center"><i>OpenStreetMap data view after filter mode is deleted</i></p>


```
Note:
When you using filter on JOSM, the result of your filter will remain on your JOSM whenever you open JOSM. Make sure you always delete your filter function after using it!
```



**SUMMARY**

After you managed to follow all these steps, now you already learn what is filter mode about on JOSM. You also already have knowledge of how to do filter on JOSM to select which data you only want to see. Use filter mode to help you and make your mapping things easier. 

