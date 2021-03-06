﻿---
title: Using YAML
weight: 4
---

**Objectives:**

*   To be able to explain about YAML concept
*   To be able to create YAML for export data in Export Tool
*   To be able to demonstrate how to get OSM data in Export Tool using YAML

As explained before, we have learned how to create a customized presets on OpenStreetMap and determine the OpenStreetMap data model to use in the mapping process. In the chapter Using Export Tool, we found the result data attributes only show the attribute from the OSM format. Therefore, you can use YAML to download the OSM data with the specific attribute that will be the same with the OpenStreetMap data model. 

### **I. YAML Concept**

**YAML** ("YAML Ain't Markup Language") is a [human-readable](https://en.wikipedia.org/wiki/Human-readable) [data serialization language](https://en.wikipedia.org/wiki/Serialization). It is commonly used for [configuration files](https://en.wikipedia.org/wiki/Configuration_file), but could be used in many applications where data is being stored (e.g. debugging output) or transmitted (e.g. document headers). We can use to create data structures in YAML format according to tag (key and value) in the OpenStreetMap data model. 

### **II. Creating YAML to Data Filter in Export Tool**

**a. YAML Structure Data**

  There are 4 sections to define a YAML structure:

1. Title 	   = define the name of file
2. Types 	    = define the name of mapping, consist of points, lines, and polygons
3. Select 	    = define key from OSM data
4. Where     = define key and value by OSM data to pull up the data  

![YAML Structure for OSM data](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0401_Struktur_format_YAML.png)
<p align="center"><i>YAML Structure for OSM data</i><p align="center">


**b. Requirements to Creating YAML Structures Data**

   There are some requirements that important to create the YAML structure:

*   All formats are lowercase, Not allow the uppercase
*   The position of the title has to put at the beginning of the document. Using the (_) sign to separate the title, an example bank_points  
*   The position of all formats are equal, an example in the image above

**c. Creating YAML**

We will create the YAML structure form OpenStreetMap Data Model that you can open the chapter **OpenStreetMap data Model **to refer the lists of OSM data Models that the objects mapped in the project. There are steps to create the YAML:

*   Open the lists OSM data model or you can create a table like below

    Bank Tag Information Table

    | key | possible values |
    |---|---|
    |amenity|bank|
    |building|bank|
    |amenity|bank|
    |name|fill the name of bank|
    |addr:full|detail of address|
    |capacity|<50, 50-100, 100-250, 250-500, >500|
    |building:levels|number|
    |building:structure|confined_masonry, steel_frame, wood_frame, bamboo_frame|
    |building:walls|brick, concrete, wood, bamboo, glass|
    |building:floor|ground, wood, cement, tekhel, ceramics|
    |building:roof|tile, tin, asbestos, concrete|
    |access:roof|yes, no|
    |building:condition|poor, good|
    |backup_generator|yes, no|


*   Open Notepad that already on your computer
*   The first line, type the name of title, an example bank

        bank:

*   The second line, click enter + space four times and typing the **types:**, and click enter + space eight times + typing **- points/polygons/lines**, an example 

             types:
                 - points
                 - polygons

*   Click enter on your keyboard and suitable the position with “types:”, and type **select:** → enter + space eight times and type the lists of the key in the Bank Tag Information Table.

            select:
                - amenity
                - name
                - addr:full
                - addr:city
                - capacity:persons
                - building
                - building:levels
                - building:structure
                - building:walls
                - building:floor
                - building:roof
                - access:roof
                - building:condition
                - backup_generator
                - source

*   The last step, click enter and suitable position types and select → type **where: key dan value**        

             where: amenity='bank'

*   If the format was completed, you can save the format in .txt file in your computer.

        bank:
            types:
                - points
                - polygons
            select:
                - amenity
                - name
                - addr:full
                - addr:city
                - capacity:persons
                - building
                - building:levels
                - building:structure
                - building:walls
                - building:floor
                - building:roof
                - access:roof
                - building:condition
                - backup_generator               
                - source
            where: amenity='bank'                                                                                                                     

### **III. How to Using YAML in  Export Tool**

**a. Login with OSM account**

*   Open your browser, and type this link https://export.hotosm.org

![The interface of Export Tool ](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0402_Halaman_Situs_Export.png)
<p align="center"><i>The interface of Export Tool </i><p align="center">

*   The first we have login with your OSM account to using Export Tool. Click on **Login** in the right corner. The next click on ‘Authorize access to your account’ → **Grant Access**.

![Grant Access](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0403_Izin_akses_akun_OSM.png)
<p align="center"><i>Login to Export Tool</i><p align="center">

*   To create a new project in Export Tool click on **Start Exporting** 
*   The Export Tool window will be displayed like the image below 

  
![The fill from Export Tool](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0404_Lembar_kerja_Export_Tool.png)
<p align="center"><i>The fill from Export Tool</i><p align="center">

**b. Defining an area of interest**

There are 5 ways to define an Area of Interest for your export:

1. **Bounding Box:** Use the "Box" tool to the right to click and drag a rectangle, or use the "Current View" tool to match the map's viewport.

    ![Bounding box](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0405_Penentuan_area_box.png)
    <p align="center"><i>Bounding box</i><p align="center">

2. **Draw Polygon:** Draw a freeform polygon. This must be a simple (not multi-) polygon.

    ![Manually edit](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0406_Penentuan_area_dengan_bentuk_manual.png)
    <p align="center"><i>Manually edit</i><p align="center">


3. **Upload:** By uploading a GeoJSON polygon in WGS84 (geographic) coordinates. If you have not the GeoJSON data, you can refer to this chapter **Using GeoJSON**.

    ![Import the administrative boundary](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0407_Penentuan_area_dengan_import.png)
    <p align="center"><i>Import the administrative boundary</i><p align="center">


4. **Search Bar:** input a minX,minY,maxX,maxY string into the search bar. This will define a rectangular area of interest.

5. **Current View:** Use "Current View" to match the map's viewport.

The maximum extent of export on the Export Tool is determined by the density of OSM data in the defined area. **The bounding box of the area can contain at most 10,000,000 OSM nodes. **This limitation means that a 10,000 square kilometer box over a heavily mapped area like Western Europe or North America will likely be rejected, but an equal-sized box over a sparsely mapped area will be accepted by the Export Tool. If you need larger exports, please Contact Us or use an alternative resource such as downloads from [Geofabrik](http://download.geofabrik.de/) or [Mapzen](https://mapzen.com/data/metro-extracts/).

**c. Naming and Describing your Export**

*   **Name (required):** choose a short, descriptive name.
*   **Description:** a long text body, perhaps describing what relevant features the export includes.
*   **Project:** Helps to group together exports particular to a project, e.g. "PDC InAWARE in Semarang City”

**d. Choosing File Format**

*   Check at least one file format to export. To learn more about each individual format, read the documentation: [Export Formats](https://export.hotosm.org/en/v3/learn/export_formats)

![Spatial data](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0408_Format_data_spasial.png)
<p align="center"><i>Spatial data</i><p align="center">

**e. Choosing Map Features**

*   Click on **Data Menu → YAML**. You can copy and paste the YAML from the section “Creating YAML” in the box.

 ![menu yaml](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0409_Menu_YAML.png)
<p align="center"><i>Menu YAML</i><p align="center">


**f. Downloading your File**

*   The last step is the Summary Menu that will be displayed about the projects. Click the **Create Export** to starting the process

![menu summary](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0410_Menu_summary.png)
<p align="center"><i>Menu summary</i><p align="center">


*   After you submit your export using **Create Export**, you will be redirected to the **Export Detail Page**, which shows a list of **Export Runs**. You will see the first run at the top of the page. It will be in one of the following states:

    **Submitted:** The export is waiting to be processed. This should be brief, depending on the server load.
    **Running:** The export is waiting to be processed. City-sized regions should be a few minutes - larger regions can take upwards of 20 minutes, depending on the density of OSM data.
    **Completed:** Your export files are available for download. Each export format has a separate download link for its ZIP archive.

![menu export](/en/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0411_Menu_export.png)
<p align="center"><i>Menu Export</i><p align="center">


*   If the status will be **COMPLETED**, we can download the data with a click on **bank_smg_shp.zip **and save in your directory. 

![Completed Process](/id/images/06-OSM-Field-Survey-Manager-Guidelines/04-Penggunaan-YAML-pada-Export-Tool/0412_Done.png)
<p align="center"><i>Completed Process</i><p align="center">


**Exercise!**

*   Create the new projects form this link [https://tinyurl.com/group-stats](https://tinyurl.com/group-stats). 
*   You can use the administrative boundary from Semarang City for Import in the project, download the admin in this link [https://tinyurl.com/admin-semarang](https://tinyurl.com/admin-semarang). 
*   The results will be used in the next chapter **Group Stats Plugin for Calculate The Objects**. If you have finished, the results consist of two shapefile (public facilities and highways).

**SUMMARY**

You have learned about how to download the spatial data using YAML in the Export Tool. The results data from YAML, the attributes table will be the same with the data in your mapping projects and the attributes table have organized. You can open the file in mapping software, like QGIS. 

