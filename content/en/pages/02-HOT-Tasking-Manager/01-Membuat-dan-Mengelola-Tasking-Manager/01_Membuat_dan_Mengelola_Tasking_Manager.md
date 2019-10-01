---
title: Creating and Managing Tasking Manager
weight: 1
---


**Objectives:**

*   Explain the functions of _Tasking Manager_ in the context of participatory mapping

*   Able to explain how to make _Tasking Manager_

*   Able to explain how to manage existing _Tasking Manager_

You must already know how to use _tasking manager_ to perform mapping activities together. When you use a tasking manager that doesn't suit the area you want, then you might want to make a tasking manager for your own area. In this module, you will learn how to make tasking manager. Making tasking manager requires the person responsible for the tasking, so that the resulting OSM data has good data quality. Also this is because the initial tasking manager was made for mapping needs as a disaster response in an area.


## I. What is a The Tasking Manager

### a. Definition of a _Tasking Manager_

_Tasking Manager_ is a tool specifically created for mapping collaborative and participatory. _The Tasking Manager_ allows you to map in an area together with other OSM users by dividing the mapping in the targeted area. The aim of the _Tasking Manager_ is to divide the mapping work into several different grids/ boxes so that everyone can choose a grid/box to be done. In addition, the _Tasking Manager_ can also make it easier for you to monitor the progress of mapping so you can find out which areas still need to be mapped and which areas have been mapped.

Imagine if you want to map in a certain area where you have to map together with 20 other people. If there is no division of tasks and mapping area, there will be a possibility that some people will map in the same area. With the _Tasking Manager_, things like this can be avoided and mapping work will be completed more quickly and effectively. 


### b. The example of the use of the _Tasking Manager_

_Tasking Manager_ first used was under a response when the Typhoon Haiyan disaster occurred in the Philippines on November 8, 2013. Mapping using the _Tasking Manager was_ conducted in Tacloban City, one of the cities that was severely affected when the disaster occurred. Within 24 hours after the project was created in _Tasking Manager_, as many as 10,000 buildings had been mapped or around 25% of the total number of buildings in Tacloban City. All of this mapping was carried out by 33 volunteers. 

![The condition of the building before and after being mapped with the Tasking Manager](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0101_tasking_manager.png "The condition of the building before and after being mapped with the Tasking Manager")
<p align="center"><i>The condition of the building before and after being mapped with the Tasking Manager</i></p>

In Indonesia, the Tasking Manager also use to respond when a disaster occurred. One example is when the earthquake and tsunami struck in the Sunda Strait in December 2018. Within a month, all the affected area were mapped by 60 people. 

![The Tasking Manager was created as a disaster response in the Sunda Strait](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0102_respon_bencana_di_selat_sunda.png "The Tasking Manager was created as a disaster response in the Sunda Strait")
<p align="center"><i>The Tasking Manager was created as a disaster response in the Sunda Strait</i></p>


## II. Makes New Project

To create new tasking in tasking manager, you must first have access as a project manager. If you do not have access, then you can request the access by sending _e-mail_ to [team.id@hotosm.org](mailto:team.id@hotosm.org) for a _tasking manager_ specific to Indonesia or [mapper-support@hotosm.org](mailto:mapper-support@hotosm.org) for global _tasking manager_. After you have managed to get access to tasking, you can look at the top right of the tasking front page and click **_Create New Project_** button. 

![How to make a new project in the tasking manager](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0103_membuat_proyek_baru_di_tasking_manager.png "How to make a new project in the tasking manager")
<p align="center"><i>How to make a new project in the tasking manager</i></p>

There are several steps that must be done when creating new task:

### a. Define the project area

#### Step 1: _Define Area_ = set your task area

After you press **_Create New Project_**, you will be directed to the first setup page, which is to set the area of ​​your mapping project. There are two ways to set the mapping of the project area:

*   **_Draw_**= with freely draw the area of interest 
*   **_Import_**= using spatial data format such as _GeoJSON, KML, OSM_ or _SHP_ compressed in _zip_.

Click **_Next_** when you have finished managing your work area.

![Options for setting work area](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0104_pilihan_mengatur_area_kerja.png "Options for setting work area")
<p align="center"><i>Options for setting work area</i></p>

#### Step 2: Choose Tasks Step = adjust the type of division for mapping area

After you have set up the work area, the next stage is that you are asked to set up the form of division of your work area. There are two types of division of work areas: square (**_square grid_**) and free (**_Arbitary Tasks_**). If you choose the shape of the box, your work area will be divided into several square boxes of the same size. Meanwhile if you choose the free form. Your work area will be divided into several random sizes. Click **Next** to go to the next stage.

![Options set the task type](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0105_pilihan_mengatur_tipe_pembagian_area_kerja.png "Options set the task type")
<p align="center"><i>Options set the task type</i></p>

#### Step 3: Set Task Sizes = Set size of the box

At this step, you will set the size of the grid. It is assumed that in the previous step you chose to divide the work area into boxes and at this step you will determine the number of boxes in the area that you specify. The bigger the size of the work box, the less the number of task area. However, this also means that mapping volunteers who participate in mapping your area may get a very large size of the mapping area and vice versa.

![Description of tools at step 3](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0106_alat_pada_tahapan_pengaturan_kotak_kerja.png "Description of tools at step 3")
<p align="center"><i>Description of tools at step three</i></p>


```
Note:
A few tips in determining the size of the task size, you certainly want to make a work box that is not too big and not too small. To determine it you can see it through the density of the road network seen in your mapping area, by using satellite imagery Bing or Mapbox. If you see a task in dense populated area, you can divide the box into several small boxes using Split (Polygon) or Split (Point).
```

#### Step 4: Trim Project = Cutting grid boxes that are not needed

After you set the size of the grid, in the next step you will be asekd whether you want to cut the grid specific to your project area or not. By using this feature, you can delete a grid that is outside the task area and leaves only a grid that matches the boundary area of ​​your area of interest. 

![Using the trim to cut the work area](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0107_menggunakan_trim_untuk_memotong_area_kerja.png "Using the trim to cut the work area")
<p align="center"><i>Using the trim to cut the work area</i></p>

#### Step 5: Review = Give the project name

The next step is that you give a name to your mapping project. At this step you should give a name that is easy to find by other users. In this section there is also a description of the number of grids / boxes that you will work on, as shown below, there are 56 _grids /_boxes. Click **_Create_ **to make your_ tasking manager_.

![The final stage before the project is made](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0108_tahapan_akhir_sebelum_proyek_dibuat.png "The final stage before the project is made")
<p align="center"><i>The final stage before the project is made</i></p>

###  b. Setting Project Descriptions 

After completing the project, you will be directed to additional settings where you will enter project descriptions, instructions, priority areas, etc. You must enter the project description and data mapped instructions, while others are optional.

*   **Description**= Provide a project description

    There are a number of things you do in this section. 

    1. You will set the status of your _tasking_(**_Draft, Published, Archived_**).
       1. **_Draft_**is the default setting when the project was first created. If aproject is _tasking _still _drafted_, mapping volunteers will not be able to help map your _tasking_. 
       2. **_Published_** means your project _tasking _has been published so that other people can see and help map your _tasking _your. 
       3. **_Archived_** means your tasking project has been archived because it's finished or there is a new tasking project with the same area. 

        Select **_Published_** so that volunteers and your team can see your _task_.

    2. You will set priorities of your _tasking_. In the _tasking manager_, you will be given three priority choices, such as urgent, high, medium, and low where each level has different meanings. You can set your tasking to an **_urgent level_** if the project _tasking_ created by you aims to be mapped immediately like mapping responses when a disaster occurs so your tasking project will be displayed at the top of the _tasking_ list. Set priority to **_high_** if your mapping is the mapping for disaster response but the disaster has passed the emergency response phase. Set priority to **_medium_** if your mapping project is not too urgent to map but is included in the scope of mapping for disaster. Set priority to **_low_** if your project activities are not urgent and not an activities for disaster mapping.

    3. You will set a summary (**_Short description_**) and a full description of your _tasking manager_. In providing a summary (_short description_) and a description for your tasking, there is a choice of languages ​​from English (**EN**) and Indonesian (**ID**). The choice of language will appear when the users change the language of _tasking manager_ to the language they want. If you want to enter Indonesian only, select **ID** as a language choice and then fill in the brief description in format _markdown_. _Markdown_ is the same format as _html_ with simpler writing. For writing guidelines with _markdown_, you can see it on the _Markdown Guide_[^1].

        
![Explanation for the Section Description of Your Mapping Project](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0109_penjelasan_deskripsi_proyek_pemetaan_anda.png "Explanation for the Section Description of Your Mapping Project")
<p align="center"><i>Explanation for the Section Description of Your Mapping Project</i></p>


*   **_Instructions_**= Provide mapping instructions
  
    In this section you will provide information about objects that should be mapped to the _Tasking Manager_ that you have created. 

    1. In the section **_Entitles to map,_** you can describe what objects you need from this project _tasking_. Suppose you need data on road, building and river networks. So in this section, you can describe these objects.
   
    2. In the section **_Changeset comment,_** you can set the default changeset comments that will appear automatically when users upload their edits to _OpenStreetMap_.

    3. In the section **_Detailed Instruction,_** You can enter mapping instructions in detail. This explanation is very helpful for volunteers who want to contribute to your tasking project but do not have experience in mapping either the _Tasking Manager_ or OpenStreetMap. You can provide detailed instructions in this section. 

![Display in the instruction section](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0110_tampilan_pada_bagian_instruksi.png "TDisplay in the instruction section")
<p align="center"><i>Display in the instruction section</i></p>



*   **_Metadata _**= Set project metadata (optional)

    1. **Mapper Level**

        In this section, you can set the difficulty of the mapping project and arrange it based on your own perceptions. For example, if the mapping area is a densely populated residential area with poor satellite imagery and the data needs to be mapped are public building data, you can adjust the level of difficulty in mapping the area such as beginner, intermediate, or advanced.

    2. **Type (s) of Mapping**

        You can identify objects that will be mapped on your tasking project by checking the list of objects in the **_Type (s) of Mapping_** section. 

    3. **Organization Tag**

        In this section you can write your organization tag to make it easier to find _tasking_ project in the search column.

    4. **Campaign Tag**

        Just like an _organization tag_ in this section you can add _tags_ that match your mapping project to make searching easier.


![Display metadata page](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0111_tampilan_halaman_metadata.png "Display metadata page")
<p align="center"><i>Display metadata page</i></p>


*   **Priority Areas** = Set priority area (optional)

    In this menu you can draw priority areas for your _taski_ng in several ways:

    1. Draw area using **_DRAW POLYGON_**
    2. Draw a box-shaped area using **_DRAW RECTANGLE_**
    3. Draw a circle using **_DRAW CIRCLE_**
    4. Change the priority area that has been drawn using **_EDIT_**
    5. Delete the priority area by using **_DELETE_**, and
    6. Delete all priority areas by using **_CLEAR ALL_**


![Priority Areas page display](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0112_tampilan_halaman_priority_areas.png "Priority Areas page display")
<p align="center"><i>Priority Areas page display</i></p>




*   **_Imagery _**= Provides additional satellite imagery (optional)

    If you have additional satellite imagery in the TMS (_Tile Map Service_) format. You can enter the _url _in this section. Besides that you also need to set a license from the satellite image you are using. You must ensure that the satellite imagery you use has a license that can be used for mapping in OpenStreetMap.

![Imagery page view](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0113_tampilan_halaman_imagery.png "Imagery page view")
<p align="center"><i>Imagery page view</i></p>

*   **_Permissions _**= Set project permission level (optional)

    In this section you can manage your project tasking only accessible to users with skill levels from beginner to advanced level. By activating thefeature **_Mapper Level_**, your tasking project can only be done by users with the level you have specified.


    If you activate the **_Level Validator_** , the user who can access your tasking to do data validation is a user with alevel _validator_.


    If you activate **_Private Project_** then your tasking will only be accessible by the user whose name (_user_ OSM) you have specified before. Other people outside the set name cannot see the tasking made by you.


![Display page Permissions](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0114_tampilan_halaman_permissions.png "Display page Permissions")
<p align="center"><i>Display page Permissions</i></p>


After completion with additional settings. You can save your tasking project by clicking **SAVE CHANGES** at the bottom.

![Click the button to save the modified tasking project](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0115_menyimpan_proyek_tasking_yang_sudah_diubah.png "Click the button to save the modified tasking project")
<p align="center"><i>Click the button to save the modified tasking project</i></p>

## III. Tasking Project Management

### a. Changing Instructions and Descriptions

If you want to add a few sentences of new instructions or want to change the description of your project as the mapping progresses in your _tasking_, you can choose **_Edit Project_ **on your tasking page_ _. After that you can immediately change the description and instructions for your tasking.

![Click EDIT PROJECT to change the description of your tasking project](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0116_edit_project_mengubah_deskripsi_proyek_tasking_anda.png "Click EDIT PROJECT to change the description of your tasking project")
<p align="center"><i>Click EDIT PROJECT to change the description of your tasking projecta</i></p>


### b. Validation 

As your tasking progresses and the data increases in the area you are working on, some volunteers may be unfamiliar with digitizing with OSM so you need validation activities to improve the data quality. For more details, you can read **Data Quality Assurance with _Tasking Manager_**. Please click button **_Validate_ **to switch to the validation page for your tasking project.

![Tasking manager validation page](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0117_halaman_validasi_pada_tasking_manager.png "Tasking manager validation page")
<p align="center"><i>Tasking manager validation page</i></p>

There are 5 options on the validation page results in _tasking manager_:
1. Select the box on the map yourself. This way you can simply select the grid/box available on the map to start validation.
2. Choose boxes randomly. This way you will be helped to choose the box.
3. Choose a box by drawing a _polygon_. By using this feature. You can choose several boxes to validate by drawing a _polygon_ or area.
4. Select the box that has been locked before. If you have already got the box validated but don't remember choosing the box, you can use this feature. By clicking this button, you will be directed to the previously selected box.
5. Choose according to username. You can also validate a box by choosing based on the name of the participating user to map it on your tasking project.

### c. Changing Priority Areas. 

You can specify priority areas to map first. The trick is to click **_Edit Project_** first and after that you go to **_Priority areas._** Change and add your priority area using the method described in the previous section.

### d. Some Action Features in _Tasking Manager_. 
In your _tasking manager_ management menu, there are several action buttons:
   *   Send a message to the contributors to your tasking project. By using the button_ **Message All Contributors.** _You can send messages that will be read by all contributors to your tasking project. This is certainly very useful if there are changes to the object being mapped or changes in priority areas.
   *   Manage all tasking simultaneously. There is a tool that you can use to manage all the tasks simultaneously. 
        *   **_Map All Tasks_** used to indicate that all the boxes on your tasking have all been mapped.
        *   **_Invalidate All Tasks_** used to cancel all the validated boxes
        *   **_Validate All Tasks_** used to validate all boxes that have been mapped
        *   **_Reset All Bad Imagery Tasks is_** used to reset all boxes that have information that the satellite image in the box cannot be used.
   *   Removing tasking projects. Using **_Delete Project_** button **You** can immediately delete your tasking project with a note that there are no contributors participating in your tasking. 
   *   Reset the tasking project. With **_Reset Tasks_** button you will reset your tasking but can still keep a history of contributors who participated in mapping your tasking project.
   *   Duplicate tasking. With **_Clone Project_** button You can duplicate your tasking and create new tasking with the same description and work area as previous tasking. The different thing is your _tasking_ will in status _Draft_ and for the area to be mapped, the number of boxes and priority areas will not be duplicated so you have to make further arrangements.


![Display of the features contained on the Action page](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0118_tampilan_fitur-fitur_yang_terdapat_pada_halaman_action.png "Display of the features contained on the Action page")
<p align="center"><i>Display of the features contained on the Action page</i></p>

### e. Archives the Tasking Project
If the tasking project is complete, you are advised to archive the tasking project that you have created. This aims to avoid contributors from mapping your_tasking_ that is. To archive a tasking project, click **_Edit Project_** and select **_Description_.** On the status menu, change from **_Published_** to **_Archived_**. Click **_Save Changes_** to save changes.

![Change project status from Published to Archived](/en/images/02-HOT-Tasking-Manager/01-Membuat-dan-Mengelola-Tasking-Manager/0119_mengubah_status_proyek_dari_published_ke_archived.png "Change project status from Published to Archived")
<p align="center"><i>Change project status from Published to Archived</i></p>



## SUMMARY

Congratulations! You have now successfully learned how to create and manage projects in _tasking managers_. By using _tasking manager_, your mapping project will become more organized. Things that must be considered, when you make a _tasking manager_, the project must be completed and considered not only the quantity of data but also the quality of the data.  


[^1]: [https://www.markdownguide.org/basic-syntax](https://www.markdownguide.org/basic-syntax) 

