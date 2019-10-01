---
title: Membuat dan Mengelola Map Campaigner untuk Pemetaan
---

**Learning Objectives:**



*   Knowing and understanding how to work with _Map Campaigners_
*   Operating _Map Campaigners_ to create mapping activities
*   Operate _Map Campaigners_ to monitor mapping activities

In implementing a mapping project you often need a report regarding the progress of the activity in a statistical data about how many objects have been mapped in the activity. There are several tools that can be used to obtain statistical data. One of the tools that we will learn today is _Map Campaigner._


## I. What is a _Map Campaigner_?

_Map Campaigner_ is a tool that is intended to gather all project managers and also surveyors into one platform. Project manager can arrange activities with specific types according to their needs. Each mapping activity created by the project manager can be specifically regulated regarding the data and objects collected then will be presented in each mapping project.


## II. Benefits and examples of using _Map Campaigner_

_Map Campaigner_ aims to make it easier for project managers to monitor their mapping projects. For example here is a mapping activity carried out by the HOT team to map all places of worship, schools, universities and high schools in Central Jakarta. By using _Map Campaigner_, you can see how many total objects have been mapped in this project activity, then how many _OpenStreetMap_ users are helping to participate in this mapping project, both voluntarily and incorporated into the mapping project team.

![Example of using Map Campaigner for Central Jakarta](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0101_contoh_penggunaan_map_campaigner_untuk__jakarta_pusat.png)
<p align="center"><i>Example of using Map Campaigner for Central Jakarta</i><p align="center">

By using _Map Campaigner,_ you can also find out how many objects that are complete by definition of _tags_ or attributes needed. For example, in the picture above, it can be seen that from the activities of this mapping project successfully obtained 1,705 objects by reaching 157 users (both voluntary and including surveyor team). _The Map Campaigner_ also provides information on the completeness of all data collected, for example from 486 mapped school objects, only 36.2% of these school objects are completely mapped in terms of the information attributes needed for this mapping project. 

_The Campaigner Map_ also presents a quality assurance feature in terms of the completeness of the attributes of an object in OSM. With _Map Campaigner_ you can see how many objects are still incomplete in terms of predetermined data attributes. You can download all of these objects and fix it using JOSM.


![Example of checking attributes by Map Campaigner](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0102_contoh_pengecekan_atribut_oleh_map_campaigner.png)
<p align="center"><i>Example of checking attributes by Map Campaigner</i><p align="center">


## III. Creating a New Mapping Project in the _Map Campaigner_

Until now you know what a _Map Campaigner is_ and what are the benefits and examples of _Map Campaigners_. You might use _Map Campaigner_ for your own mapping project. In order to create a new _project_, you must _log in_ first with your _OpenStreetMap_ account. After you have successfully _logged in_ with your account, then you need to click on **_Create Campaign_** button. Next there are several steps after you have successfully _logged in_ with _OpenStreetMap_ account. After clicking **_Create Campaign_** button, you will be directed to project creation _campaign_ page. On this page there are two stages: **managing basic information** and **organizing work areas**.


### a. Organizing Basic Information for your Project _Campaign_

In this section, you will fill in basic information for your project. You must fill in some information on this page:



*   **Project name.** In this section, you only need to fill in the name of the project that you are doing.
*   **The duration of the project.** In this section, you will set the duration of the project in progress. You can provide a date in the past if the mapping project that you are doing is a mapping project that has already been completed.
*   **Project Description.** In this section, you will fill in a description of the project activities.
*   **Attributes /_tags_ needed.** In this section you will provide the _OpenStreetMap_ attributes needed during the mapping project. For _OpenStreetMap_ attributes  the required, you can refer to the Wikipedia page[^1] [^2] or to **Data Model _OpenStreetMap_** module. You can choose to use **_YAML_** (which you already learned in the module _**Using YAML on HOT Export**_) or with an easy version already provided on this site.

![Display when entering OSM attributes for Map Campaigner](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0103_tampilan_saat_memasukkan_atribut_osm_untuk_map_campaigner.png)
<p align="center"><i>Display when entering OSM attributes for Map Campaigner</i><p align="center">)



```
Note:
When entering tags / attributes informat YAML. There are a number of things to be aware of:
* Use of space is very sensitive here. 
* One element consists of the main elements and supporting elements
* All elements under the main element (supporting elements) must be several spaces apart from the main
* The contents of the supporting elements = features, tags, & element_type
* features are categories in OSM. For more details, you can see OSM wikipedia
* To be more specific, you can use sets key & value such as building = school or amenity = hospital
* tags are a collection of key & value that will be checked by the system. Please check wikipedia or OpenStreetMap Data Model module
* element_type is the type of OSM object to be checked, such as point(point),line(line),or area(polygon) 
```

*   **Add another project manager (optional).** In this section you can add other OSM accounts as project _campaign_ if the project that you are working on there is more than one project manager. The role of the project manager is that they can add new attributes to be calculated or change the information that is in their project _campaign_ .

    
![Display on the basic information page](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0104_tampilan_pada_halaman_informasi_dasar.png)
<p align="center"><i>Display on the basic information page</i><p align="center">


### b. OrganizingWork for _Campaign Project_ You

Once you have successfully set the basic information, the next step is you have to organize your project work area. In this section, there are two ways to organize your project work area.

The first way is to use the tools on the left side of the map. You can draw a box or draw freely using the tool. The thing to remember is that **the project campaign area should not exceed 315 km<sup>2</sup>.** If your mapping project has more area than mentioned, it is recommended to divide the mapping project area into several sections so that it can be created in the _Map Campaigner_.

The second way is to use administrative boundary data informat _GeoJSON_. Using this data, you can immediately see the work area of ​​your project that has been divided into several sections.

After setting the project work area, you can specify which team is assigned to the predetermined project area. This team setting is optional and aims to make it easier to monitor the progress of your team.


![Display on work area settings page](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0105_tampilan_pada_halaman_pengaturan_area_kerja.png)
<p align="center"><i>Display on work area settings page</i><p align="center">


## IV. View Your Project Campaign Page

Having successfully made a campaign,you can go straight to the main page to see the project. When opening the mapping project, you will be presented with some information ranging from statistical data, a list of _errors_, and graphs of users who participated in the mapping.


![Display page of Map Campaigner](/en/images/07-Map-Campaigner/01-Membuat-dan-Mengelola-Map-Campaigner-untuk-Pemetaan/0106_tampilan_halaman_map_campaigner.png)
<p align="center"><i>Display page of Map Campaigner</i><p align="center">


1. **_Feature collected._** This section explains how many total objects are collected in the work area.
2. **_User engaged_.** Explain how many OSM users are participating in helping to map either voluntarily or not.
3. **_Area covered._** Explain what percentage of the area that has been completely mapped.
4. **_Feature selection_.** To select a predetermined OSM feature.
5. **_Selected attribute_.** Explain some OSM attributes that must be checked by the system to determine the completeness of its attributes.
6. **_Attribute completeness_.** Explain what percentage of complete OSM objects have the attributes as specified in thesection **_selected attribute_**.
7. **_Feature checked._** Explain the number of OSM objects that have been collected, specific to only one feature in accordance with thesection **_feature selection_**. 
8. **_Graph_.** Explain about the graph of the number of objects in detail

In addition to some of the above, there is also an **_Errors_** section which explains the list of objects that have not been completed in terms of OSM attributes. In addition you can also see the **_User Enggagement_** section to see the list of OSM users who participated helped map the area along with the number of contributions from each OSM user.


## V. Fixing an Incomplete Objects 

Using _Map Campaigner_, you can directly fix OSM objects that are incomplete in terms of their data attributes. To fix it there are two ways.



*   First is to fix OSM objects one by one by selecting the object id in thecolumn **_Name_**. This way you will be directed to the _OpenStreetMap_ webpage and then you can immediately change it using **JOSM** or **iD**.
*   The second way is to click **_Download_** button at the bottom of _error_ list. By using this, you will download _file_.osm and opened using JOSM. After the file has been downloaded successfully, you can immediately open it in JOSM to directly complete the attributes.


## SUMMARY

Congratulations! You have now successfully learned how to use the _Map Campaigner_ for the purposes of your mapping project. By using _Map Campaigner_ you will find it easier to find out how many objects have been successfully mapped easily and see which OSM objects do not have complete attributes that are suitable for your project.

[^1]:[https://wiki.openstreetmap.org/wiki/Map_Features](https://wiki.openstreetmap.org/wiki/Map_Features)

[^2]:[https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines](https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines)


