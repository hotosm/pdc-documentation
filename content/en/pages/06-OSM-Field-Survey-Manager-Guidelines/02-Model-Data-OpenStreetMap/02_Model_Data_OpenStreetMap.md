---
title: OpenStreetMap Data Model
weight: 2
---

**Objectives:**

*   Understanding Concept of _tag_, _key,_ dan _value_ in _OpenStreetMap_
*   Knowing _OpenStreetMap_ wiki page as a guideline for _key_ and _value_
*   Understanding Objects which can be mapped into _OpenStreetMap_
*   Knowing and Understanding data model as a part of mapping preparation plan
*   Checking specific _key_ and _value_ in _TagInfo_ website

In this module, you will learn about _key_ and _value_ concept in _OpenStreetMap_ (OSM) as well as data model in OSM objects. Knowing about data model will help you to prepare your mapping activity plan efficiently start from planning, field survey and input the field survey data. You also learn some websites which can help you to find specific information key and value that you need based on OpenStreetMap standard.

### **I. _Tag_, _Key_, dan _Value_ Concept**

In _OpenStreetMap_ there are 3 types of object. They are: _Nodes_, _Ways_, and _Polygon/Closedways_. Each type of data has information that can represent the object. That information called _Tag_ which structured by _key_ and _value_.

For instance, there is a school in your area. Therefore, the school should be **Tagged** as a school in OpenStreetMap. The school’s tag has some details information that make the school being different from other schools. Those information such as  name, address, building level, school type, etc. In OpenStreetMap, they are **_Key_** while each information of them called **_Value_**. 

Example of School _Tag_: 

name=SDN Kebon Manggis 11 Pagi  

address= Jalan Slamet Riyadi II. 

In the example above, “name and address” are **_Key_** while “SDN Kebon Manggis 11 Pagi and Jalan Slamet Riyadi II” are **_Value_**. See the image below to see the explanation in OpenStreetMap website:

![Key and value of an object on OpenStreetMap](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0201_contoh_key_dan_value_di_osm.png)
<p align="center"><i>Key and value of an object on OpenStreetMap</i></p>

As you can see on the picture above, key and value always written in english according to the OpenStreetMap standard. You do not need to remember all key and value in OpenStreetMap because you can find them in wikipedia _OpenStreetMap_ website which will be explained in this module.

### **II. Wikipedia _OpenStreetMap_ to see Key and Value**

As a one of mapping participatory platform, OpenStreetMap has millions of contributors all around the globe. Therefore to produce and ensure a good quality data and information in OpenStreetMap, the contributors together established rules and standardization guidelines and put into one open-source platform site called wikipedia.



**a. Global Wikipedia _OpenStreetMap_**

Further explanation and list of key and value in OpenStreetMap have been made and put into specific OSM wikipedia page called _Map Feature_. In this page, you can search and find any key and value that used in OpenStreetMap globally. To access this page please visit at: [https://wiki.openstreetmap.org/wiki/Map_Features](https://wiki.openstreetmap.org/wiki/Map_Features) 

![Interface of Map Features Website Page](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0202_wiki_map_feature.png)
<p align="center"><i>Interface of Map Features Website Page</i></p>

Every key and value in this page is absolute and has been standard information for any object that you want to map in OpenStreetMap and cannot be changed or modified as you want. Therefore, this page is a guideline for all OSM contributors all over the world to find any information about their mapping object in OpenStreetMap.

**b. Indonesia OpenStreetMap Wikipedia**

Number of OSM Contributors in Indonesia has been increasing in recent years. As one of biggest OSM contributors in the world, Indonesia OSM contributors need a guideline about key and value information especially particular information for objects in Indonesia. However, they are usually difficult to find a tag that match with the mapping object. There are so many information in the Map Feature page yet sadly most of them are unneeded or unnecessary   for objects in Indonesia. Moreover, object’s name in Map Feature often can not be recognized by OSM contributors in Indonesia because it is using global name while Indonesia using local name. Therefore, Humanitarian _OpenStreetMap_ Team (HOT) Indonesia made another page in OSM wikipedia that shows specific information about key and value mapping objects in Indonesia as a guideline for Indonesia OSM contributors.

Main difference between _Map Features_ and Indonesia OSM Wikipedia page is list of the mapping objects. While Map Features shows all information for mapping objects all over the world, Indonesia OSM Wikipedia only showing information about objects in Indonesia and some of them do not available in the map feature. For instance, schools in Indonesia have various information including types of school start usually called SD (elementary school), SMP (junior high school) and SMA (senior high school). Health facilities also has various type depending of its type such as Rumah Sakit (Hospital), Puskesmas ( hospital in village level) , Posyandu (hospital in rural area). These information are essential in Indonesia therefore they have been placed in Indonesia OpenStreetMap Wikipedia page. Another example is you only can find name kiosk as a name and key of small store in Map Feature while the name is not familiar and known by most of Indonesian in Indonesia OpenStreetMap Wikipedia page this small store has been given a local name called “warung” even though still has key=kiosk for its tag in OpenStreetMap. 

You can see list of objects information in Indonesia OpenStreetMap Wikipedia page by click this link: [https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines](https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines) 

![Page of Indonesia OpenStreetMap Wikipedia Page](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0203_wiki_osm_indonesia.png)
<p align="center"><i>Page of Indonesia OpenStreetMap Wikipedia Page</i></p>

### **III. Mapping Objects in _OpenStreetMap_**

**a. Data types in _OpenStreetMap_**

In this module, you have been explained about data types in OpenStreetMap: point (_Nodes_), line (_Ways_) and area (_Polygon/Relation_). These are further explanation of each data type in OpenStreetMap.

*   **Point (_Nodes_)**

Point usually being used to represent position or location of certain object. For instance, objects which drawn as a point (nodes) in OpenStreetMap such as traffic light, gas station or restaurant in a mall or shopping center.

![Example of Points in OpenStreetMap](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0204_objek_titik.jpg)
<p align="center"><i>Example of Points in OpenStreetMap</i></p>

*   **Line (_Ways_)**

Line is an object that is formed by sequence of  points (_nodes_) which connect one to another. Some objects which usually drawn as a line in OpenStreetMap such as road, river, railway and administration boundary.

![Example of lines in OpenStreetMap](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0205_objek_garis.jpg)
<p align="center"><i>Example of lines in OpenStreetMap</i></p>


*   **Area (_Polygon_)**

Area is formed by sequence of lines (_ways_) which connect one to another. Some objects in OpenStreetMap such as building, park, land use and lake are drawn as area.

![Example of area (polygon) in OpenStreetMap](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0206_objek_area.jpg)
<p align="center"><i>Example of area (polygon) in OpenStreetMap</i></p>


**b. Mapping Objects in HOT-PDC Project**

In _OpenStreetMap_, you can map any object on earth surface as long as it is real and permanent. Real means that the object has physical form and can be seen such as building and roads whereas non-real object such as high level or population density. Permanent means the object has specific location and not moving in particular time.

Choosing what objects that we want to map in OpenStreetMap depends on the purposes of the mapping project itself. In HOT-PDC InAWARE, the purpose is to collecting critical infrastructures which can be used for disaster management. These are list of objects that has been mapped into OpenStreetMap in HOT-PDC InAWARE project:

**1.Economic Facilities**

*   Traditional Market
*   Supermarket
*   Bank

**2. Education Facilities**

*   University
*   College
*   School (SD, SMP, SMA)
*   Kindergarten

**3. Health Facilities**

*   Hospital
*   Clinic

**4. Communication**

*   Communication Tower

**5. Emergency Service**

*   Police Office
*   Fire Station
*   Evacuation Center
*   Hydrant

**6. Government**

*   Government Office (Governor, Mayor, District, Sub-district, village and sub-village office)
*   Embassy
*   Government Institution (Ministry)

**7. Electricity**

*   Power tower
*   Power substation
*   Power Plant

**8. Transportation**

*   Airport
*   Bus Station
*   Train Station
*   Harbour / Dock

**9. Public Facilities**

*   Place of Worship (Mosque, Church, Temple)
*   Sport Facility (Sport Center, Stadium, Sports Field)
*   Public Spaces

**10. Water**

*   Water Tower
*   Water Gate
*   Pump House
*   Embankment
*   River
*   Lake / Dam

**11. Gas Station**

**12. Administration Boundary**

*   City / District Boundary
*   Sub-district boundary
*   Village boundary
*   Sub-village boundary

**13. Road Network**

### **IV. Data Mapping Model in _OpenStreetMap_**

Data model is a compilation of some information for an object where consisted from key and value in OpenStreetMap. A data model does not have a standard for what information that should be put in an object. The model should be followed the purposes of mapping project. For instance, if you want to map school in you area and you need information of **school name**, **address**, **school type**, **school operator**, and **building level** then your data model should be like this:

School Tag Information Table

| key | (possible) values |
|---|---|
|<font  color="99DBFF"> amenity | <font  color="99DBFF"> school |
|<font  color="#FF7278"> building | <font  color="#FF7278"> school |
| school:type_idn | sd [SD/MI (Elementary School)], smp [SMP/MTs (Junior High School)], sma [SMA/SMK/MA (Senior High School)] |
| name | (building name) |
|addr:full | (address) |
| operator:type | government, private, community |
| building:levels | (number of building floor) |

<font  color="99DBFF">amenity=school</font>  is a compulsory tag for the school information. _Key_ and _value_ in this tag are main information that identify the object as a school.

<font  color="#FF727dima8"> building=school</font> is a tag that show the school has its own building. Some schools are located in another building such as government office area therefore if that was the case then this tag is unnecessary.


**a. HOT-PDC InAWARE Data Model**

The purpose of HOT-PDC InAWARE mapping project is to gather information of critical infrastructures in context of disaster management. Therefore, you need to create data model that can help the survey team to collect the information in the field and upload them into OpenStreetMap. These are data model for each priority object in HOT-PDC InaWARE mapping project:

**Color Information:**

*  <font  color="99DBFF"> Warna biru </font> the _key_ and _value_ are compulsory for the object.
*  <font  color="#FF7278"> Warna merah </font> the _key _and _value _are information for building of the object. This tag /information only collected if the object has its own building. Otherwise, the tag is unnecessary.
* Warna hitam artinya _key_ dan _value_ tersebut **sebaiknya** dimasukkan ke dalam objek pemetaan baik objek tersebut memiliki bangunan sendiri ataupun menumpang di bangunan yang lain.
*   Black color means the _key_ and _value_ **should be** added regardless the object has its own building or not.

**1.Economic Facilities**

*   Table of Traditional Market Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>marketplace
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>marketplace
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><traditional market name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Supermarket Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>shop
   </td>
   <td>supermarket
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>supermarket
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><supermarket name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Bank Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>bank
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>bank
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><bank name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**2. Education Facilities**



*   Table of University Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>university
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>university
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><university name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of College Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>college
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>college
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><college name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of School Data Model (SD, SMP, SMA)

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>school:type_idn
   </td>
   <td>sd [SD/MI (Elementary School)], smp [SMP/MTs (Junior High School)], sma [SMA/SMK/MA (Senior High School)]
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>school
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>school
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><school name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of Kindergarten Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>Kindergarten [PAUD/ Play Group / TK (Early education / Play group / Kindergarten)]
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>kindergarten
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><kindergarten name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**3. Health Facilities**



*   Table of Hospital Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>hospital
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><hospital name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>hospital
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of Clinic Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>clinic
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><clinic name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator:type
   </td>
   <td>government, private, community
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>clinic
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>


**4. Communication**



*   Table of Communication Tower Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>man_made
   </td>
   <td>tower
   </td>
  </tr>
  <tr>
   <td>tower:type
   </td>
   <td>communication
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><tower name></em>
   </td>
  </tr>
  <tr>
   <td>height
   </td>
   <td><em><tower height in metre></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td>Telkomsel, Indosat, XL, Tri, Smartfren
   </td>
  </tr>
  <tr>
   <td>communication:mobile
   </td>
   <td>yes,no
   </td>
  </tr>
  <tr>
   <td>communication:radio
   </td>
   <td>yes,no
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**5. Emergency Services**



*   Table of Police Office Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>police
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>police
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><Police Office name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Fire Station Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>fire_station
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>fire_station
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><fire station name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Hydrant Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>emergency
   </td>
   <td>fire_hydrant
   </td>
  </tr>
  <tr>
   <td>fire_hydrant:type
   </td>
   <td>underground, pillar, wall, pond
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><hydrant name></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator name></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**6. Government**



*   Table of Government Office Data Model Model (Governor, Mayor, District, Sub-district, village and sub-village office)

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>office
   </td>
   <td>government
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>governor_office, townhall, subdistrict_office, village_office , community_group_office
   </td>
  </tr>
  <tr>
   <td>admin_level
   </td>
   <td>4 (governor office), 5 (town hall), 6 (subdistrict office), 7 (village office), 9 (subvillage office) 
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><government office name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of Government Institution Data Model (Ministry)

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>office
   </td>
   <td>government
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>government_office
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><government institution name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>admin_level
   </td>
   <td>7 (village level), 6 (sub district level), 5 (city level), 4 (Province level)
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**7. Electricity**



*   Table of Power Tower Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>power
   </td>
   <td>tower
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><tower name>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><name of the electricity company></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Power Sub Station Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>power
   </td>
   <td>substation
   </td>
  </tr>
  <tr>
   <td>substation
   </td>
   <td>transmission (Main substation), distribution (Distribution sub station)
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>power_substation
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><<em>power substation name</em>>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>rating
   </td>
   <td><<em>user define</em>>  
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><name of the electricity company></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Power Plant Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>power
   </td>
   <td>plant
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>power_plant
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><power plant name></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><name of the electricity company></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**8. Transportation**



*   Table of Airport Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>aeroway
   </td>
   <td>aerodrome
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>aerodrome
   </td>
  </tr>
  <tr>
   <td>Name 
   </td>
   <td><em><airport name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Bus Station Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>bus_station
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><bus station name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Train Station Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>railway
   </td>
   <td>station
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><train station name>
   </td>
  </tr>
  <tr>
   <td>ele
   </td>
   <td><em><station height above sea level></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><name of companye></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Harbour / Dock Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>ferry_terminal
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>ferry_terminal
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><Dock Name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><addresst></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**9. Public Facilities**



*   Table of Place of Worship Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>place_of_worship
   </td>
  </tr>
  <tr>
   <td>religion
   </td>
   <td>muslim, christian, hindu, buddhist, confucian
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><place of worship name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>mosque, church, temple
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><jumlah lantai></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry (Rangka beton bertulang), steel_frame (Rangka baja), wood_frame (Rangka kayu), bamboo_frame (Rangka bambu)
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick (Bata), concrete (Beton), wood (Papan kayu), bamboo (Bambu), glass (Kaca)
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground (Tanah), wood (Papan kayu), cement (Plester / Semen), tekhel (Tegel), ceramics (Keramik)
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile (Genteng), tin (Seng), asbestos (Asbes), concrete (Beton)
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes (Ada), no (Tidak ada)
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor (Buruk), good (Baik)
   </td>
  </tr>
  <tr>
   <td>ground_floor:height=
   </td>
   <td>Tinggi bangunan dari jalan dalam satuan meter
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes (Ada), no (Tidak ada)
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes (Ya), no (Bukan)
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent (Tenda), building (Bangunan)
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works (PDAM), manual_pump (Pompa Tangan), powered_pump (Mesin Pompa)
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes (Ada), no (Tidak ada)
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes (Ada), no (Tidak ada)
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilets></em>
   </td>
  </tr>
</table>




*   Tabel Model Data Fasilitas Olahraga (GOR,Lapangan Olahraga, Stadium)

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>leisure
   </td>
   <td>stadium (Stadion), sports_centre (Pusat Kegiatan Olahraga / GOR), pitch (Lapangan Olahraga)
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>stadium, sports_centre, yes (futsal field)
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><nama fasilitas olahraga></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><alamat></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><kota pemetaan></em>
   </td>
  </tr>
  <tr>
   <td>sport
   </td>
   <td>soccer,futsal,basketball,badminton,tennis,volleyball,swimming,athletics,
<p>
baseball,cycling,multi
   </td>
  </tr>
  <tr>
   <td>capacity:persons
   </td>
   <td><50, 50-100, 100-250, 250-500, >500
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>ground_floor:height
   </td>
   <td>building ground floor to the surface in metre
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>




*   Table of Park Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>leisure
   </td>
   <td>park
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><park name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td><em>HOT_InAWARESurvey_2018</em>
   </td>
  </tr>
  <tr>
   <td>evacuation_center
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>shelter_type
   </td>
   <td>tent, building
   </td>
  </tr>
  <tr>
   <td>water_source
   </td>
   <td>water_works, manual_pump, powered_pump
   </td>
  </tr>
  <tr>
   <td>kitchen:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilet:facilities
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>toilets:number
   </td>
   <td><em><number of toilet available></em>
   </td>
  </tr>
</table>


**10. Sarana Perairan**



*   Table of Water Tower Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>man_made
   </td>
   <td>water_tower
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><water tower name></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator name></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Flood Gate Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>waterway
   </td>
   <td>floodgate
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><flood gate name></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator name></em>
   </td>
  </tr>
  <tr>
   <td>floodgate:unit
   </td>
   <td><em><number of gate></em>
   </td>
  </tr>
  <tr>
   <td>elevation
   </td>
   <td><em><elevation above sea level></em>
   </td>
  </tr>
  <tr>
   <td>condition
   </td>
   <td><em>good , poor</em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Tabel Model Data Rumah Pompa

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>man_made
   </td>
   <td>pumping_station
   </td>
  </tr>
  <tr>
   <td>building
   </td>
   <td>pumping_station
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><pumping station name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator name></em>
   </td>
  </tr>
  <tr>
   <td>pump:unit
   </td>
   <td><em><number of pump></em>
   </td>
  </tr>
  <tr>
   <td>elevation
   </td>
   <td><em><elevation above sea level></em>
   </td>
  </tr>
  <tr>
   <td>capacity:pump
   </td>
   <td><em><pump capacity (l/s)></em>
   </td>
  </tr>
  <tr>
   <td>building:levels
   </td>
   <td><em><building level></em>
   </td>
  </tr>
  <tr>
   <td>building:structure
   </td>
   <td>confined_masonry, steel_frame, wood_frame, bamboo_frame
   </td>
  </tr>
  <tr>
   <td>building:material
   </td>
   <td>brick , concrete, wood, bamboo, glass
   </td>
  </tr>
  <tr>
   <td>building:floor
   </td>
   <td>ground, wood, cement, tekhel, ceramics
   </td>
  </tr>
  <tr>
   <td>building:roof
   </td>
   <td>tile, tin, asbestos, concrete
   </td>
  </tr>
  <tr>
   <td>access:roof
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>building: condition
   </td>
   <td>poor, good
   </td>
  </tr>
  <tr>
   <td>backup_generator
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>




*   Table of Embankment Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>man_made
   </td>
   <td>embankment
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><embankment name></em>
   </td>
  </tr>
  <tr>
   <td>material
   </td>
   <td><em>concrete, stone, soil, sand</em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td><em>HOT_InAWARESurvey_2018</em>
   </td>
  </tr>
</table>




*   Table of River Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>waterway
   </td>
   <td>river, riverbank, canal
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><nama sungai></em>
   </td>
  </tr>
  <tr>
   <td>width
   </td>
   <td><em><river name></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td><em>HOT_InAWARESurvey_2018</em>
   </td>
  </tr>
</table>




*   Table of Reservoir Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>landuse
   </td>
   <td>reservoir
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><reservoir name></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><operator namer></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**11. Gas Station**



*   Table of Gas Station Data Model

<table>
  <tr>
   <td>
<strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>amenity
   </td>
   <td>fuel
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><gas station name></em>
   </td>
  </tr>
  <tr>
   <td>addr:full
   </td>
   <td><em><address></em>
   </td>
  </tr>
  <tr>
   <td>addr:city
   </td>
   <td><em><mapping city></em>
   </td>
  </tr>
  <tr>
   <td>operator
   </td>
   <td><em><PT Pertamina, Shell, etc></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**12. Administration Boundary**


<table>
  <tr>
   <td><strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>type
   </td>
   <td>boundary
   </td>
  </tr>
  <tr>
   <td>boundary
   </td>
   <td>administrative
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><em><name></em>
   </td>
  </tr>
  <tr>
   <td>admin_level
   </td>
   <td>4 (Province), 5 (City / District), 6 (Sub-district), 7 (Village), 8 (Hamlet), 9 (Sub-Village), 10 (Sub-sub Village)
   </td>
  </tr>
  <tr>
   <td>is_in:province
   </td>
   <td><em><province name></em>
   </td>
  </tr>
  <tr>
   <td>is_in:city <strong>(City)</strong>
<p>
is_in:town <strong>(District)</strong>
   </td>
   <td><em><city / district name></em>
   </td>
  </tr>
  <tr>
   <td>is_in:municipality
   </td>
   <td><em><sub-district name></em>
   </td>
  </tr>
  <tr>
   <td>is_in:village
   </td>
   <td><em><village name></em>
   </td>
  </tr>
  <tr>
   <td>is_in:RW
   </td>
   <td><em><sub-village name></em>
   </td>
  </tr>
  <tr>
   <td>flood_prone 
<p>
<strong>[*only for sub village relation]</strong>
   </td>
   <td>yes,no
   </td>
  </tr>
  <tr>
   <td>landslide_prone
<p>
<strong>[*only for sub village relation]</strong>
   </td>
   <td>yes,no
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td>HOT_InAWARESurvey_2018
   </td>
  </tr>
</table>


**13. Road Network**


<table>
  <tr>
   <td><strong>key</strong>
   </td>
   <td><strong>possible values</strong>
   </td>
  </tr>
  <tr>
   <td>highway
   </td>
   <td>motorway , trunk , primary , secondary , tertiary , service , residential , pedestrian, path , living_street, track
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td><road name>
   </td>
  </tr>
  <tr>
   <td>layer
   </td>
   <td>5,4,3,2,1,-1,-2,-3,-4,-5
   </td>
  </tr>
  <tr>
   <td>width
   </td>
   <td><em><road width></em>
   </td>
  </tr>
  <tr>
   <td>lanes
   </td>
   <td><em><number of lanes></em>
   </td>
  </tr>
  <tr>
   <td>surface
   </td>
   <td>asphalt , concrete, metal, wood, grass, ground, gravel, mud, sand, paving_stones
   </td>
  </tr>
  <tr>
   <td>smoothness
   </td>
   <td>good, intermediate, bad, impassable
   </td>
  </tr>
  <tr>
   <td>motorcycle
   </td>
   <td>yes,no
   </td>
  </tr>
  <tr>
   <td>oneway
   </td>
   <td>yes, no
   </td>
  </tr>
  <tr>
   <td>ref 
   </td>
   <td><em><reference></em>
   </td>
  </tr>
  <tr>
   <td>source
   </td>
   <td><em>HOT_InAWARESurvey_2018</em>
   </td>
  </tr>
</table>


** **

**b. Data Type in OpenStreetMap Based on Object**

After knowing data model based on object tag in OpenStreetMap particularly in HOT-PDC InAWARE Project, you also need to know data type based on the object itself. The table below shows you what type of data for each object that you can add into OpenStreetMap:

**Color Information:**



*   Green Color means the object **allowed** to be mapped in that data type
*   Red Color means the object **not allowed** and **prohibited** to be mapped in that data type

Table of Object and Its Data Type in _OpenStreetMap_

![Object Data Type Table](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0207_tabel_infrastruktur.png)


### **V. Search _key_ and _value_ in _Tag Info_ Website**

On previous subchapter, you have been explained about a guideline to see key and value in _OpenStreetMap_ using _Map Features_ and Indonesia OpenStreetMap Wikipedia page. However, there are certain _key_ and _value_ that do not explained in the page especially detail and specific information of certain object. For instance, for **building capacity** or **building floor material**. To see the information (_tag_) you can visit a website called tag info: [https://taginfo.openstreetmap.org/](https://taginfo.openstreetmap.org/) 


![Tag Info Website Interface](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0208_halaman_tag_info.png)
<p align="center"><i>Tag Info Website Interface</i></p>



The picture above shows _KEYS_ colom where showing some most searched keys by OpenStreetMap contributor such as _building, highway, name, source_, etc. Moreover, you also can see combination between certain _key_ and _value_ (tag) which quite common such as _building=yes_ and _highway=residential TAGS_ colom or you can search your key manually in search box at the top right corner on the website page. 

For example, if you want to search information about **how to put your mapping activity as a source of the object** or **Level of Certain Building**, you can click building option in _Keys_ colom and you will see this:


![Example Combination of tag and value in Tag Info](/en/images/06-OSM-Field-Survey-Manager-Guidelines/02-Model-Data-OpenStreetMap/0209_kombinasi_tag_info.png)
<p align="center"><i>Example Combination of tag and value in Tag Info</i></p>


You can choose _Combinations_ tab and you will see some combinations for _building_ key that commonly used by _OpenStreetMap_ contributor. For instance, if you are looking for information about source of building and building level, you can use **_source_** and **_building:levels_**. Moreover, you can see another combination for key and value related to building.  You can see how often the key have been used in OpenStreetMap by look at _Count_ colom. The bigger the number means the key more often and commonly used by OpenStreetMap contributors all over the world. 


> Notes :
 key and value in OpenStreetMap HAVE TO BE WRITTEN in English
 key and value in OpenStreetMap HAVE TO BE WRITTEN in lower case
Information interface can be set to show in Bahasa Indonesia on JOSM by editing / make special presets
Make new presets will be explained in other module called  Making OpenStreetMap Presets



**SUMMARY**

Congratulation! You have learned about data model in _OpenStreetMap_ . This material is important and really to be understand by OpenStreetMap contributors so you can do your mapping based on international standard from OpenStreetMap community guidelines. Moreover, you also have known about certain websites which can help you to find the information (tag) for you mapping objects such as OSM wiki _Map Feature_ Indonesia, OpenStreetMap Wikipedia page, and _Tag Info_.