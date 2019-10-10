---
title: Download OSM Data using Export Tool
weight: 1
---


**Objectives:**

*   To be able to explain the definition and function of Export Tools
*   To be able to operate Export Tools

In this chapter, we can learn about how to download the OSM data that we have added and uploaded into OSM. The data can be used to analysis, customize with data symbology, create maps, and others depend on your necessary.

### **I. Export Tool Concept**

The Export Tool is an open service that creates customized extracts of up-to-date OSM data in various file formats, such as ESRI shapefiles (.shapefile), google KML (.kml), GeoPackage (.gpkg) dan MBTiles (.mbtiles). We can select the area and specific categories that we necessary. Download and use the data simply by crediting the **© OpenStreetMap contributors**. Anyone can create a custom OpenStreetMap export with the Export Tool - just register an account. You can register with an OpenStreetMap account from [OpenStreetMap.org](https://openstreetmap.org/) and a valid email address.

### **II. How to using Export Tool**

**a. Login with OSM account**

*   Open your browser, and type this link https://export.hotosm.org

![The interface of Export Tool](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0101_tampilanexporttool.png)
<p align="center"><i>The interface of Export Tool</i><p align="center">

*   The first we have login with your OSM account to using Export Tool. Click on **Login** in the right corner. The next click on ‘Authorize access to your account’ → **Grant Access**.
*   To create a new project in Export Tool click on **Start Exporting** 
*   The Export Tool window will be displayed like the image below 

![The fill from Export Tool](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0102_lembarkerjaet.png)
<p align="center"><i>The fill from Export Tool</i><p align="center">

**b. Defining an area of interest**

There are 5 ways to define an Area of Interest for your export:

1. **Bounding Box:** Use the "Box" tool to the right to click and drag a rectangle, or use the "Current View" tool to match the map's viewport.

    ![Bounding box](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0103_Penentuan_Area_dengan_Kotak.png)
    <p align="center"><i>Bounding box</i><p align="center">

2. **Draw Polygon:** Draw a freeform polygon. This must be a simple (not multi-polygon).

    ![Manually edit](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0104_penentuan_manual.png)
    <p align="center"><i>Manually edit</i><p align="center">

3. **Upload:** By uploading a GeoJSON polygon in WGS84 (geographic) coordinates. If you have not the GeoJSON data, you can refer to this chapter **Using GeoJSON**.

  
    ![Import the administrative boundary](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0105_penentuangeojson.png)
    <p align="center"><i>Import the administrative boundary</i><p align="center">

4. **Search Bar:** input a minX,minY,maxX,maxY string into the search bar. This will define a rectangular area of interest.

5. **Current View:** Use "Current View" to match the map's viewport.

    The maximum extent of export on the Export Tool is determined by the density of OSM data in the defined area. **The bounding box of the area can contain at most 10,000,000 OSM nodes.** This limitation means that a 10,000 square kilometer box over a heavily mapped area like Western Europe or North America will likely be rejected, but an equal-sized box over a sparsely mapped area will be accepted by the Export Tool. If you need larger exports, please Contact Us or use an alternative resource such as downloads from [Geofabrik](http://download.geofabrik.de/) or [Mapzen](https://mapzen.com/data/metro-extracts/).

**c. Naming and Describing your Export**

*   **Name (required):** choose a short, descriptive name.
*   **Description:** a long text body, perhaps describing what relevant features the export includes.
*   **Project:** Helps to group together exports particular to a project, e.g. "PDC InAWARE Indonesia”

**d. Choosing File Format**

*   Check at least one file format to export. To learn more about each individual format, read the documentation: [Export Formats](https://export.hotosm.org/en/v3/learn/export_formats)

![Spatial data](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0106_menuformat.png)
<p align="center"><i>Spatial data</i><p align="center">


**e. Choosing Map Features**

*   For your first time using the export tool, it's recommended to use the Tag Tree, which curates a set of filters and tags for common map features. As an example, check the box "**Buildings and Transportation → Roads**" to create an export of all building geometries, as well as related data such as name and address keys.

![Select the object in export Tool](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0107_buildingandroads.png)
<p align="center"><i>Select the object in export Tool</i><p align="center">

**f. Downloading your File**

*   The last step is the Summary Menu that will be displayed about the projects. Click the **Create Export** to starting the process

![menu summary](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0108_menusummary.png)
<p align="center"><i>Menu Summary</i><p align="center">

*   After you submit your export using **Create Export**, you will be redirected to the **Export Detail Page**, which shows a list of **Export Runs**. You will see the first run at the top of the page. It will be in one of the following states:

    **Submitted:** The export is waiting to be processed. This should be brief, depending on the server load.


    **Running:** The export is waiting to be processed. City-sized regions should be a few minutes - larger regions can take upwards of 20 minutes, depending on the density of OSM data.


    **Completed:** Your export files are available for download. Each export format has a separate download link for its ZIP archive.

![menu export](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0109_menuexporttool.png)
<p align="center"><i>Menu Exports</i><p align="center">

*   If the status will be **COMPLETED**, we can download the data with a click on **buildings_and-roads-bali-upate.shp.zip** and save in your directory. 

![Completed Process](/en/images/05-HOT-Export/01-Penggunaan-Export-Tool/0110_selesaiexport.png)
<p align="center"><i>Completed Process</i><p align="center">


**SUMMARY**

We have learned about how to download the OSM data using Export Tool. We can open the data in the mapping software as for example QGIS ([www.qgis.org](http://www.qgis.org)). You also can use the data to calculate the quantities of infrastructures.
