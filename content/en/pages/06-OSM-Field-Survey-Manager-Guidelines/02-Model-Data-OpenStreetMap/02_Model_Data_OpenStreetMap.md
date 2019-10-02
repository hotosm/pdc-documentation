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
|<span style="color:#3333cc"> amenity  |  <span style="color:#3333cc"> school |
|<span style="color:#FF7278"> building   | <span style="color:#FF7278"> school |
| school:type_idn | sd [SD/MI (Elementary School)], smp [SMP/MTs (Junior High School)], sma [SMA/SMK/MA (Senior High School)] |
| name | (building name) |
|addr:full | (address) |
| operator:type | government, private, community |
| building:levels | (number of building floor) |

<span style="color:#3333cc">amenity=school</font>  is a compulsory tag for the school information. _Key_ and _value_ in this tag are main information that identify the object as a school.

<span style="color:#FF7278"> building=school</font> is a tag that show the school has its own building. Some schools are located in another building such as government office area therefore if that was the case then this tag is unnecessary.


**a. HOT-PDC InAWARE Data Model**

The purpose of HOT-PDC InAWARE mapping project is to gather information of critical infrastructures in context of disaster management. Therefore, you need to create data model that can help the survey team to collect the information in the field and upload them into OpenStreetMap. These are data model for each priority object in HOT-PDC InaWARE mapping project:

**Color Information:**

*  <span style="color:#3333cc">  Warna biru </font> the _key_ and _value_ are compulsory for the object.
*  <span style="color:#FF7278"> Warna merah </font> the _key _and _value _are information for building of the object. This tag /information only collected if the object has its own building. Otherwise, the tag is unnecessary.
* Warna hitam artinya _key_ dan _value_ tersebut **sebaiknya** dimasukkan ke dalam objek pemetaan baik objek tersebut memiliki bangunan sendiri ataupun menumpang di bangunan yang lain.
*   Black color means the _key_ and _value_ **should be** added regardless the object has its own building or not.

**1.Economic Facilities**

*   Table of Traditional Market Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc">marketplace  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> marketplace |
|  name | (traditional market name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |



*   Table of Supermarket Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> supermarket  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> supermarket |
|  name | (supermarket name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |



*   Table of Bank Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> bank  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> bank |
|  name | (bank name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |


**2. Education Facilities**

*   Table of University Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> university  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> university |
|  name | (university name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


*   Table of College Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> college  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> college |
|  name | (college name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


*   Table of School Data Model (SD, SMP, SMA)

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> school:type_idn |<span style="color:#3333cc"> sd (Elementary School)], smp (Junior High School)], sma (Senior High School)  |
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> school  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> school |
|  name | (school name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


*   Table of Kindergarten Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> kindergarten  |
| <span style="color:#FF7278"> building (Early education / Play group / Kindergarten)| <span style="color:#FF7278"> school |
|  name | (kindergarten name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |



**3. Health Facilities**

*   Table of Hospital Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> hospital  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> hospital |
|  name | (hospital name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


*   Table of Clinic Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> clinic  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> clinic |
|  name | (clinic name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator:type |  government, private, community |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


**4. Communication**

|key   | possible values  |
|---|---|
|<span style="color:#3333cc"> man_made  |<span style="color:#3333cc"> tower  |
|<span style="color:#3333cc"> tower:type | <span style="color:#3333cc"> communication  |
| name  | (tower name)  |
| height | (tower height in meter unit)  |
| operator   | Telkomsel, Indosat, XL, Tri, Smartfren  |
| communication:mobile  | yes, no  |
| communication:radio  | yes, no   |
| addr:city  | (mapping city)  |
| source  | HOT_InAWARESurvey_2018  |


**5. Emergency Services**


*   Table of Police Office Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> police  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> police |
|  name | (police office name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |




*   Table of Fire Station Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> fire_station  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> fire_station |
|  name | (fire station name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |


*   Table of Hydrant Data Model

|  key  | possible values  |
|---|---|
|<span style="color:#3333cc"> emergency  |<span style="color:#3333cc"> fire_hydrant  |
|<span style="color:#3333cc"> fire_hydrant:type |<span style="color:#3333cc"> underground, pillar, wall, pond |
| name  |  (hydrant name) |
| operator  | (operator name)  |
| addr:city  | (mapping city)  |
| source  | HOT_InAWARESurvey_2018  |


**6. Government**


*   Table of Government Office Data Model Model (Governor, Mayor, District, Sub-district, village and sub-village office)

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> office | <span style="color:#3333cc"> government  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> governor_office, townhall, subdistrict_office, village_office, community_group_office |
| <span style="color:#3333cc"> admin_level | <span style="color:#3333cc"> 4 (for governor office), 5 (for townhall), 6 (for subdistrict office), 7 (for village office), 9 (for community group office)  |
|  name | (government office name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |


*   Table of Government Institution Data Model (Ministry)

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> office | <span style="color:#3333cc"> government  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> government_office |
|  name | (government institution name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
| <span style="color:#3333cc"> admin_level | <span style="color:#3333cc"> 4 (provincial level), 5 (city level), 6 (subdistrict level), 7 (village level)  |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |


**7. Electricity**

*   Table of Power Tower Data Model

|  key | possible values  |
|---|---|
|  <span style="color:#3333cc"> power |<span style="color:#3333cc"> tower  |
| name  |  (tower name) |
| addr:city  | (mapping city)  |
| operator  |  PT Perusahaan Listrik Negara |
|  source | HOT_InAWARESurvey_2018  |


*   Table of Power Sub Station Data Model

|  key | possible values  |
|---|---|
| <span style="color:#3333cc"> power |<span style="color:#3333cc"> substation  |
| <span style="color:#3333cc"> substation | <span style="color:#3333cc"> transmission, distribution |
| <span style="color:#FF7278"> building |<span style="color:#FF7278"> power_substation  |
| name  |  (power substation name) |
| addr:city  | (mapping city)  |
| rating  | (user defined)  |
| operator  |  PT Perusahaan Listrik Negara |
|  source | HOT_InAWARESurvey_2018  |

*   Table of Power Plant Data Model

|  key | possible values  |
|---|---|
| <span style="color:#3333cc"> power | <span style="color:#3333cc"> plant  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> power_plant  |
| name  |  (power plant name) |
| operator  |  (power plant operator) |
| addr:city  | (mapping city)  |
| addr:full  | (address)  |
|  source | HOT_InAWARESurvey_2018  |


**8. Transportation**

*   Table of Airport Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> aerodrome  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> aerodrome |
|  name | (airport name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |


*   Table of Bus Station Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> amenity |<span style="color:#3333cc">  bus_station  |
|  name | (bus station name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |


*   Table of Train Station Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> amenity | <span style="color:#3333cc"> station  |
|  name | (train station name)  |
| <span style="color:#3333cc"> ele | <span style="color:#3333cc"> (train station's height above sea level)  |
|  operator | PT Kereta Api Indonesia  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |


*   Table of Harbour / Dock Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> ferry_terminal  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> ferry_terminal |
|  name | (ferry terminal name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |


**9. Public Facilities**

*   Table of Place of Worship Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">amenity | <span style="color:#3333cc"> place_of_worship  |
|  <span style="color:#3333cc"> religion | <span style="color:#3333cc">  muslim, christian, hindu, buddhist, confucian  |
|  name | (place of worhsip name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> mosque, church, temple|
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |

*   Table of Sport Facilities (Sports Center,Sport Field, Stadium)

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc">leisure | <span style="color:#3333cc"> stadium, sports_centre, pitch |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> stadium, sports_centre, yes (futsal field)  |
|  name | (sport facility name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
| <span style="color:#FF7278"> sport | <span style="color:#FF7278"> soccer,futsal,basketball,badminton,tennis,volleyball,swimming,athletics, baseball,cycling, multi|
|  <span style="color:#FF7278"> capacity:persons |<span style="color:#FF7278"> <50, 50-100, 100-250, 250-500, >500  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building|
| water_source  |  water_works, manual_pump, powered_pump|
| kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no|
| toilets:number  |  (number of toilets) |

*   Table of Park Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> leisure |<span style="color:#3333cc"> park  |
|  name | (park name)  |
|  addr:full | (address)   |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |
|  evacuation_center |  yes, no |
|  shelter_type |  tent, building |
| water_source  |  water_works, manual_pump, powered_pump|
|kitchen:facilities   |  yes, no |
| toilet:facilities |  yes, no |
| toilets:number  |  (number of toilets) |


**10. Waterway Facilities**

*   Table of Water Tower Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> man_made | <span style="color:#3333cc"> water_tower  |
|  name | (water tower name)  |
|  operator | (water tower operator)   |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |


*   Table of Flood Gate Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> waterway |<span style="color:#3333cc"> floodgate  |
|  name | (flood gate name)  |
|  operator | (flood gate operator)   |
|  floodgate:unit | (number of floodgate)   |
|  elevation | (flood gate's height above sea level)   |
|  <span style="color:#3333cc"> condition | <span style="color:#3333cc"> good, poor |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |

*   Tabel Model Data Rumah Pompa

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> man_made |<span style="color:#3333cc"> pumping_station  |
| <span style="color:#FF7278"> building | <span style="color:#FF7278"> pumping_station |
|  name | (pumping station name)  |
|  addr:full |(address)   |
|  addr:city |  (mapping city) |
|  operator | (operator name)   |
|  pump:unit | (number of pumping station)   |
|  elevation | (pumping station's height above sea level)   |
| <span style="color:#FF7278"> capacity:persons | <span style="color:#FF7278"> (pump's capacity (l/s))  |
|  <span style="color:#FF7278"> building:levels | <span style="color:#FF7278"> (number of building floor) |
|<span style="color:#FF7278"> building:structure   | <span style="color:#FF7278">  confined_masonry , steel_frame , wood_frame , bamboo_frame |
| <span style="color:#FF7278"> building:material  | <span style="color:#FF7278"> brick , concrete , wood , bamboo , glass|
| <span style="color:#FF7278"> building:floor  |<span style="color:#FF7278"> ground, wood, cement, tekhel, ceramics |
| <span style="color:#FF7278"> building:roof  | <span style="color:#FF7278"> tile, tin, asbestos, concrete |
| <span style="color:#FF7278"> access:roof | <span style="color:#FF7278"> yes, no |
| <span style="color:#FF7278"> building: condition | <span style="color:#FF7278"> poor, good |
| <span style="color:#FF7278"> ground_floor:height | <span style="color:#FF7278"> (building base floor height from the road  (meter unit)) |
| backup_generator  | yes, no  |
|  source |  HOT_InAWARESurvey_2018 |

*   Table of Embankment Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> man_made | <span style="color:#3333cc"> embankment  |
|  name | (embankment name)  |
| <span style="color:#3333cc"> material | <span style="color:#3333cc"> concrete, stone, soil, sand |
|  source |  HOT_InAWARESurvey_2018 |

*   Table of River Data Model

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> waterway |<span style="color:#3333cc"> river, riverbank, canal |
|  name | (river)  |
| <span style="color:#3333cc"> width |<span style="color:#3333cc"> (river width)   |
|  source |  HOT_InAWARESurvey_2018 |

*   Table of Reservoir Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> landuse |<span style="color:#3333cc">  reservoir  |
|  name | (resevoir/lake name)  |
|  operator | (operator name)   |
|  addr:city |  (mapping city) |
|  source |  HOT_InAWARESurvey_2018 |

**11. Gas Station**

*   Table of Gas Station Data Model

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> amenity | <span style="color:#3333cc"> fuel  |
|  name | (gas station name)  |
|  addr:full |  (address) |
|  addr:city |  (mapping city) |
|  operator | (PT Pertamina, Shell, etc)   |
|  source |  HOT_InAWARESurvey_2018 |

**12. Administration Boundary**

| key  |  possible values |
|---|---|
|  <span style="color:#3333cc"> type | <span style="color:#3333cc"> boundary  |
| <span style="color:#3333cc">  boundary |  <span style="color:#3333cc"> administrative |
| <span style="color:#3333cc"> name | <span style="color:#3333cc"> (boundary name)  |
|  <span style="color:#3333cc"> admin_level |<span style="color:#3333cc"> 4 (Province), 5 (City / District), 6 (Sub-district), 7 (Village), 8 (Hamlet), 9 (Sub-village), 10 (Sub-sub village)   |
| <span style="color:#3333cc"> is_in:province | <span style="color:#3333cc"> (province name) |
| <span style="color:#3333cc"> is_in:city (city) / is_in:town (district)|<span style="color:#3333cc"> (city/subdistrict name) |
| <span style="color:#3333cc"> is_in:municipality |<span style="color:#3333cc"> (sub-district name)   |
| <span style="color:#3333cc"> is_in:village |<span style="color:#3333cc"> (village name)   |
| <span style="color:#3333cc"> is_in:RW |<span style="color:#3333cc"> (sub village name)  |
|  flood_prone *only for sub village relation |  yes, no|
|  landslide_prone *only for sub village relation |  yes, no|
|  source |  HOT_InAWARESurvey_2018 |


**13. Road Network**

| key  |  possible values |
|---|---|
| <span style="color:#3333cc"> highway |<span style="color:#3333cc"> motorway, trunk, primary, secondary, tertiary, service, residential, pedestrian, path, living_street, track |
|  name | (street name)  |
|  layer | 5,4,3,2,1,-1,-2,-3,-4,-5  |
|  width |  (road width) |
|  lanes | (number of road lanes)   |
| <span style="color:#3333cc"> surface | <span style="color:#3333cc"> asphalt, concrete, metal, wood, grass, ground, gravel, mud, sand, paving_stones |
|  smoothness | good, intermediate, bad, impassable |
|  motorcycle | yes, no  |
| <span style="color:#3333cc"> oneway | <span style="color:#3333cc"> yes, no |
| ref  |  (refference) |
|  source |  HOT_InAWARESurvey_2018 |


**b. Data Type in _OpenStreetMap_ Based on Object**

After knowing data model based on object tag in OpenStreetMap particularly in HOT-PDC InAWARE Project, you also need to know data type based on the object itself. The table below shows you what type of data for each object that you can add into OpenStreetMap:

**Color Information:**

*   <span style="color:#7EFF83">Green Color</span> means the object **allowed** to be mapped in that data type.
*   <span style="color:#FF7278">Red Color</span> means the object **not allowed** and **prohibited** to be mapped in that data type.

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