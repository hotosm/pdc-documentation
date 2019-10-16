---
title: JOSM for Data Quality
weight: 4
---

**Objectives:**

*   Understanding how to select and count numbers of objects in certain administration boundary
*   Understanding how to count numbers of _error_ and _warning_ in certain administration boundary
*   Understanding how to validate administration boundary

One of the expected results in doing mapping activity is to produce a good quality map. The quality including object information completeness and right topology. Using _OpenStreetMap_ as a base map to show the result of field survey could help you to monitor the progress of your mapping activity result by counting objects and information from the field. In this module you will learn how to count your field survey data and administration boundary using _Java OpenStreetMap_ (JOSM) 


### I. **Counting Objects in Certain Administration Boundary**

One of the stages of data quality monitoring is by counting the objects in your mapping area. The purpose is to know the progress of the mapping activity such as before and after the mapping started. Moreover, this activity can help you to validate the completeness of information for you mapping objects. You can use JOSM to count your mapping objects on your survey area. There are steps to count objects in certain administration boundary such as village level, as follows:

 **a. _Download_ OpenStreetMap Data in Mapping Area**

Before you start counting your mapping objects,  you need to _download_ _OpenStreetMap_ data in your mapping area. When counting the objects, you can use you mapping area administration boundary such as village boundary. In this example, you will count the objects in **Pleburan Village**. These are the steps that you need to follow to _download_ _OpenStreetMap_ data:


*   Open **JOSM** in your laptop / computer.
*   Select **_File → Download Data_** menu, you will see a download box around your mapping area in _OpenStreetMap._
*   Select **_Areas around Places_** menu and type village name “**Pleburan**” in the search box and remember to check **_OpenStreetMap Data_** and **_Download as New Layer_** option
*   If it has finished, please choose the most relevant result with your mapping area. You can look at the city location and has  _boundary=administrative_ tag. Your result will be in blue color

![Download Area Searching Window in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0401_josm_data_quality_1.png)
<p align="center"><i>Download Area Searching Window in JOSM</i></p>


*   After set all the options like the picture above, you can click **_Download._**

![JOSM Download Data Result](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0402_josm_data_quality_2.png)
<p align="center"><i>JOSM Download Data Result</i></p>

>Notes :
If your mapping area size is too large, please download it periodically into JOSM


**b. Counting Objects in Certain Administration Boundary Area**

If you have successfully download data in your mapping area, the next step is counting total of objects in it. The steps to count numbers of objects in your mapping area as follows:

*   Click **_Edit → Search_** menu to select administration boundary of **Pleburan Village**.

![Data Search Menu in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0403_josm_data_quality_3.png)
<p align="center"><i>Data Search Menu in JOSM</i></p>

*   In search string, please type “**admin_level=7**” (village level) and click **_Start Search_**

![Searching Window to select certain area in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0404_josm_data_quality_4.png)
<p align="center"><i>Searching Window to select certain area in JOSM</i></p>

*   You will see all objects that have _“admin_level=7_” tag will selected and listed in **_selection_** window. Then you can select **Pleburan Level** which you can count all object on it by **double click** it. You will see administration boundary of Pleburan Village will be shown in purple color in JOSM data layer which indicate that the village has been selected. 

![Selected Village Output in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0405_josm_data_quality_5.png)
<p align="center"><i>Selected Village Output in JOSM</i></p>

*   If your JOSM has not _Selection_ menu, you have to install _utilsplugin_  plugin in your JOSM. The explanation about how to install the plugin can be seen in **Adding OSM Data using JOSM** module. After that, please select **Selection → All inside [testing]** menu. You will see all objects inside Pleburan Village will be selected and have red color. 

![Data Selection Result in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0406_josm_data_quality_6.png)
<p align="center"><i>Data Selection Result in JOSM</i></p>


*   After that, please select **_Selection → Intersecting Ways_** menu to select all objects inside and intersected with Pleburan Village, such as road networks and river. Duration of this process depends on area size and number of objects inside the village.

![All Selection Result on Certain Administration Boundary in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0407_josm_data_quality_7.png)
<p align="center"><i>All Selection Result on Certain Administration Boundary in JOSM</i></p>

*   You can see all the total number of objects in **_properties/membership_** window.

![All Data Selection in Certain Area in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0408_josm_data_quality_8.png)
<p align="center"><i>All Data Selection in Certain Area in JOSM</i></p>

*   As you can see in the image above, there are 1995 objects in Pleburan Village have been selected. Please keep in your mind, this result is **whole** selection result of objects. You do not need to count for each specific object in your mapping area using JOSM. 

### **II.  Count Number of _Error_ and _Warning_ in Certain Administration Boundary**

After successfully counting the total number of objects in your mapping area ( in this module is Pleburan Village), you should continue to follow the steps to see and count number of _Error_ and _Warning_ on objects in the village:

*   Click **_Validation_** in your validation window. Wait until JOSM finish to count the number of  _Error_ and _Warning_ on your objects.

![Data Validation Window in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0409_josm_data_quality_9.png)
<p align="center"><i>Data Validation Window in JOSM</i></p>

*   If your JOSM has finished, you will see the results in the validation window. You better write the number of _error_ and _warning_ then try to fix them all. For further explanation about  how to  validate and fix error and warning in JOSM can be seen in **JOSM for Survey Data Validation.**

![Data Validation Result](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0410_josm_data_quality_10.png)
<p align="center"><i>Data Validation Result</i></p>

*   After you have fixed the _error_ and _warning_ , you can calculate data quality number in **Microsoft Excel or Google Sheet**. The result will show data quality comparison in the mapping area, before and after the mapping activity has done.  _Error_ and _Warning_ types also need to be added into calculation table.

Table of Data Quality Recapitulation

![Data Validation Result](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0411_josm_data_quality_11.png)

As you can see on the table above, the number of objects in Pleburan Village before the mapping activity was 1.863 where there were 4 _warnings_. After the mapping activity and validation have done, the number of objects is increasing to 1.963 where there are no _error_ and _warning_ have been found.  You can see the whole recapitulation table for Data Quality in Semarang in this link: [http://bit.ly/tabeldatasemarang](http://bit.ly/tabeldatasemarang) 

### **III. Administration Boundary Validation**

After have finished to calculate the number of objects and data quality in your mapping area, you need to calculate and validate the administration boundary of your mapping area. In this calculation, you will validate of  administration boundary such as village and sub-village boundary (RW) in your mapping area. You need to check number of sub-village in the mapping area, boundary information (tag) completeness, relations of village and sub village boundary and backup the boundary as an _.osm_ file. We still use **Pleburan Village** as an example in this validation.

**a. Counting Number of Sub-Village (RW)**

These are steps that you have to do for counting number of sub-village (RW) in your mapping area:

*   You have downloaded Pleburan Village in your JOSM. However, it also means you download all objects in the village and it could be difficult for you to see and edit the administration boundary because so many objects around it. Therefore, you have to filter the data. If you have not known about filter tools functions in JOSM, please look at **Menggunakan Alat Filter di JOSM** module

*   Activate your _filter _tool in JOSM by click **_Windows → Filter_**

![Activate the filter tool in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0412_josm_data_quality_12.png)
<p align="center"><i>Activate the filter tool in JOSM</i></p>


*   **_Filter_** window will appear in JOSM. please click **_add_** and write **_query_** to filter the data show it only shows administration boundary. The query is “**is_in:village”=”Pleburan**”. 

*   You will see your data will change like the picture below:

![Administration Boundary Filter in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/00413_josm_data_quality_13.png)
<p align="center"><i>Administration Boundary Filter in JOSM</i></p>


*   Select all sub-village boundary in Pleburan Village with _search_ function. Click **_Edit → Search_**. You will see a search window and write _query_ “**admin_level=9**” then click **_Start Search_**.

![Query for search sub-village boundary in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0414_josm_data_quality_14.png)
<p align="center"><i>Query for search sub-village boundary in JOSM</i></p>


*   You will sub-village boundary in your village be selected. It is shown by purple color in the boundaries. In **_selection_** window you will see all sub-village list in Pleburan Village.

![Selection Result for Sub-Village Boundary in Pleburan Village](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0415_josm_data_quality_15.png)
<p align="center"><i>Selection Result for Sub-Village Boundary in Pleburan Village</i></p>

*   You can compare number of sub-village (RW) in Pleburan Village which a result of selection function in JOSM in recapitulation table of field survey. 

![Table of Sub-Village Boundary Recapitulation](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0416_josm_data_quality_16.png)
<p align="center"><i>Table of Sub-Village Boundary Recapitulation</i></p>

As you can see on the table above, the number of sub-village (RW) in Pleburan Village is 6 sub-villages. This number is same with the selection result in JOSM which also select 6 sub-villages boundaries starting from RW 01 to RW 06. Therefore, there is no error on number of sub-villages in your mapping area. You can continue to validate the tag and relation of boundary administration. 

**b. Counting Tag Completeness and Boundary Administration Relations**

After counting number of sub-villages in Pleburan Village, now you need to validate the boundary administration tag completeness. These are the tags that need to have for each of sub-village (RW) boundary administration:

Table of Boundary Administrative (RW) Tag List

| key  |  possible values |
|---|---|
|  type | boundary  |
|  boundary |  administrative |
|  name | (RW name)  |
|  admin_level | 9 |
|  is_in:province |  (province name) |
|  is_in:city (City) / is_in:town (District)| (city/district name)   |
|  is_in:municipality | (sub-district name)   |
|  is_in:village | (village name)   |
|  flood_prone *only for RW  relation |  yes, no |
|  landslide_prone *only for RW  relation   |  yes, no |
|  source |  HOT_InAWARESurvey_2018 **(Based on the mapping project name)**|

To validate tag of sub-village administration boundary, please follow these steps:

*   Choose all sub-villages in **_selection_** list result from **_search_** feature in JOSM.

![Select sub-villages in Pleburan Village](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0417_josm_data_quality_17.png)
<p align="center"><i>Select sub-villages in Pleburan Village</i></p>


*   **Right click** on sub-villages list and choose **Edit**. You will see a warning window that remind you where all information related the sub-village in Pleburan Village will be open in 6 windows. Clik **Ok.**

![Notification to see Sub-Village Information](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0418_josm_data_quality_18.png)
<p align="center"><i>Notification to see Sub-Village Information</i></p>

*   After the window is open, you need to check the tag completeness **for each** sub-villages. Moreover, the  boundary relation checking needs to be done by see the relation connection in **_member_** . You can see whether your relation is a good relation if connection between sub-village member all connected and creating _loop_ or circle. If you want to know more details about connection between relation and how to add it, please see **Membuat Batas Administrasi di JOSM** module.

![Relation Window and Information of Administration Boundary](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0419_josm_data_quality_19.png)
<p align="center"><i>Relation Window and Information of Administration Boundary</i></p>

You can add another tag if there are some tag still not added in the sub-village based on tag list above. You also can fix the relation and member order and rules for each member.

> Note :
If the number of sub-village does not same with the field survey (more or less), you need to discuss this problem with the Data Entry and Quality Assurance who survey and input all the boundary into OpenStreetMap.
Do same validation steps for relation for sub-district ("admin_level=6") and village ("admin_level=7") administration boundary. 

**c. Administration Boundary Backup**

After doing recapitulation and validation for administrative boundary, you need to backup the administrative boundary. Thus, you will have a backup for your administration boundary when something unexpected events happen such as the boundary accidentally deleted or some users edit it wrong. To do so, the steps as follows:

*   Click **_Edit → Copy_**

![Copy Administration Boundary in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0420_josm_data_quality_20.png)
<p align="center"><i>Copy Administration Boundary in JOSM</i></p>

*   Choose **_File → New Layer_** You will see new layer in JOSM.

![Create New Layer in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0421_josm_data_quality_21.png)
<p align="center"><i>Create New Layer in JOSM</i></p>

*   Click **_Edit → Paste at source position_**

![Copy and Paste Administration Boundary in New Layer](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0422_josm_data_quality_22.png)
<p align="center"><i>Copy and Paste Administration Boundary in New Layer</i></p>

*   You now have a new layer that only show administration boundary of your mapping area. Please click **File → Save** and save it into _.osm_ file format and give name based on your mapping area.

![Save Adminstration Boundary Layer in JOSM](/en/images/04-Data-Validation-and-Quality-Assurance/04-JOSM-Untuk-Perhitungan-Kualitas-Data/0422_josm_data_quality_22.png)
<p align="center"><i>Save Adminstration Boundary Layer in JOSM</i></p>

**SUMMARY**

You have learned about how to recapitulate data quality in JOSM. This activity is one of the validation activities for field survey data that has been added into _OpenStreetMap **by** Quality Assurance_. By doing this, your data quality will be assured and have better quality. These are details about what objectives that have learned in this module:

*   Count number of objects in certain administration boundary (village)
*   Count number of _error_ and  _warning_ in certain administration boundary
*   Doing Recapitulation to compare number of objects and _error_/ _warning_
*   Validate administrative boundary including count number of sub-village in certain village, checking tag completeness and relation between administration boundary.
*   Backup the administration boundary into .osm file format