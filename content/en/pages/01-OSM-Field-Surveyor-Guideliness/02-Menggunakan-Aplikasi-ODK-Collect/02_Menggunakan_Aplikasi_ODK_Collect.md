﻿---
title: Using ODK Collect
weight: 2
---


**Objective:**

*   Able to explain ODK Collect as one of the tools to collect infrastructure data
*   Able to set the initial setup for ODK Collect 
*   Able to apply how to use ODK Collect for data collection survey

### **I. What is ODK Collect?**

Open Data Kit Collect (ODK Collect) is a data collection application on Android. ODK Collect can replace form survey from paper to digital. Therefore, this application will help the mapping and data collection activities in the field which also allow to save the location and photo information at once.

### **II. Initial Setup for ODK Collect**

**1. Set the URL Server**

To take the form survey from the server for the first time, the user needs to set the URL server. There are the steps:

*   Open ODK Collect and press the three point button in the upper right corner, select **General Settings → Server**

![Option to fill the URL address menu in ODK Collect](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0201_Option_to_fill_the_URL_address_menu_in_ODK_Collect.png)
<p align="center"><i>Option to fill the URL address menu in ODK Collect</i><p align="center">


*   Type the URL address server in **URL → OK**

![Step to fill the URL address in ODK Collect](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0202_Step_to_fill_the_URL_address_in_ODK_Collect.png)
<p align="center"><i>Step to fill the URL address in ODK Collect</i><p align="center">


**2. Set the Image Size**

In addition to the location point, you can also take a picture as additional information. You can set the picture resolution as desired. But, the picture resolution will also affect the amount of your phone memory or file which will be uploaded to the server later. It is recommended that you choose the smallest resolution of the image during initial setup. You can follow this step: 

*   Open ODK Collect and press the three point button in the upper right corner, select **General Settings → Form Management**.

![Option menu to set image resolution](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0203_Option_menu_to_set_image_resolution.png)
<p align="center"><i>Option menu to set image resolution</i><p align="center">

*   Select **Image Size** then select the **Very Small (640px) option.**

![Image Size menu to set the image resolution](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0204_Image_size_menu_to_set_the_image_resolution.png)
<p align="center"><i>Image Size menu to set the image resolution</i><p align="center">


### III. ODK Collect basic operations

**1. How To Get a Blank Form Survey From Server**

Before you fill-out the form survey that you made before, you need to download the blank survey form from specified server.  For further explanation about create a survey form in ODK, you can learn in **Making Survey Form for ODK & OMK applications** module. You can follow this step to take a blank survey from the server:

*   Press **Get Blank Form** and wait for the form to download from the server and make sure your internet is active.

![Get blank form options to take form on a server](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0205_Get_blank_form_options_to_take_form_on_a_server.png)
<p align="center"><i>Get blank form options to take form on a server</i><p align="center">

*   Select the available form, tick the check box or if you want to select all the form, you can **Select All**. If your form does not appear, can press **Refresh** to reload the page.

![Page display on Get Blank Form menu](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0206_Page_display_on_Get_Blank_Form_menu.png)
<p align="center"><i>Page display on Get Blank Form menu</i><p align="center">

*   After select the form, you can press **Get Selected** to download the selected form.

![Page display on the Get Blank Form to get the survey form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0207_Page_display_on_the_Get_Blank_Form_to_get_the_survey_form.png)
<p align="center"><i>Page display on the Get Blank Form to get the survey form</i><p align="center">


**2. Fill the Survey Form**

*   To fill the form, back to the start page and select **Fill Blank Form** menu. And then select one form blank that you want to fill in the survey form list.

![Fill Blank Form options for filling out the survey form and blank survey form list](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0208_Fill_Blank_Form_options_for_filling_out_the_survey_form_and_blank_survey_form_list.png)
<p align="center"><i>Fill Blank Form options for filling out the survey form and blank survey form list</i><p align="center">


*   Swipe to right or left on the screen to move the next/previous page. Questions that have a red star in the top left are required and you can not go to next question if the answer is empty.

![Examples of mandatory question (red star)](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0209_Examples_of_mandatory_question_red_star.png)
<p align="center"><i>Examples of mandatory question (red star)</i><p align="center">


*   You can take photos directly by choose **Take Picture** option or select a photo from your photo gallery by select **_Choose Image_**.

![Take photo display in ODK Form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0210_Take_photo_display_in_ODK_Form.png)
<p align="center"><i>Take photo display in ODK Form</i><p align="center">


*   To add object location points include OSM object tag, you can use additional application, that is OpenMapKit (OMK). You can immediately switch to OMK application by press **Launch OpenMapKit** on the form. You can learn about using OMK application in the module **Using the OpenMapKit**. 

![Launch OpenMapKit button on the survey form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0211_Launch_OpenMapKit_button_on_the_survey_form.png)
<p align="center"><i>Launch OpenMapKit button on the survey form</i><p align="center">


*   At the end, you can name the form, tick check **Mark form as finalized** and at the end choose **Save Form and Exit** to finalize the final form survey.

![Finalization of page views on the survey form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0212_Finalization_of_page_views_on_the_survey_form.png)
<p align="center"><i>Finalization of page views on the survey form</i><p align="center">


**3. Edit the Completed Survey Form**

The saved form automatically save in ODK Collect. If you want to edit the completed form, you can follow this step:

*   You can back to start page and choose **Edit Saved Form**.

![Edit Saved Form for edit the saved form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0213_Edit_Saved_Form_for_edit_the_saved_form.png)
<p align="center"><i>Edit Saved Form for edit the saved form</i><p align="center">


*   Select the form that you want to edit by press the form and you can edit the form.

![Edit save form page to select the form that you want to edit](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0214_Edit_save_form_page_to_select_the_form_that_you_want_to_edit.png)
<p align="center"><i>Edit save form page to select the form that you want to edit</i><p align="center">


*   Then, press floppy disk icon  

![Edit save form page to select the form that you want to edit](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0215_A_completed_survey_form_and_icon_to_save_changes.png)
<p align="center"><i>Edit save form page to select the form that you want to edit</i><p align="center">


**4. Upload Survey Forms to Server**

After you fill and save the form, the next step is upload form survey to server.  You can follow this step to upload form to server:

*   To upload the form return to the server, you can choose **Send Finalized Form**.

![Send Finalized Form to upload a survey form to the server](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0216_Send_Finalized_Form_to_upload_a_survey_form_to_the_server.png)
<p align="center"><i>Send Finalized Form to upload a survey form to the server</i><p align="center">


*   Form survey is saved on that page and ready to send. You can choose **Select All** to select all forms first. 
*   Make sure you are connected on the internet. Then press **Send Selected** and wait until the process _upload_ the form is complete.

![Survey forms that are ready to send in the Send Finalized Form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0217_Survey_forms_that_are_ready_to_send_in_the_Send_Finalized_Form.png)
<p align="center"><i>Survey forms that are ready to send in the Send Finalized Form</i><p align="center">


*   All forms that have been successfully uploaded will be stored in **View Sent Form** menu and the icon turn into green.

![View Sent Form and survey form that have been successfully uploaded to the server](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0218_View_Sent_Form_and_survey_form_that_have_been_successfully_uploaded_to_the_server.png)
<p align="center"><i>View Sent Form and survey form that have been successfully uploaded to the server</i><p align="center">


*   After upload the form, you can delete the form in **_Delete Saved Form_** menu.

![Delete Saved Form menu for delete the form](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0219_Delete_Saved_Form_menu_for_delete_the_form.png)
<p align="center"><i>Delete Saved Form menu for delete the form</i><p align="center">


*   You can delete the the filled form in **Saved Forms** option and delete the blank form in **Blank Forms** option. You should choose the form that you want to delete or **Select All** for delete all form.

![Delete Saved Form option](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0220_Delete_Saved_Form_option.png)
<p align="center"><i>Delete Saved Form option</i><p align="center">


*   You need to confirm to delete the survey form by choose **Delete Forms**

![Delete confirmation dialog box](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0221_Delete_confirmation_dialog_box.png)
<p align="center"><i>Delete confirmation dialog box</i><p align="center">


**5. Upload Survey Form to Google Drive**

After you upload all the survey form to server, you need to save and upload the survey result file in .zip format in Google Drive folder that was created by your mapping supervisor. This is the step:

*   Go File Manager or File Explorer on your smartphone and open your internal storage. Then open ODK folder. This folder contains all the survey result file which stored on ODK Collect application. Then select instances folder which contains *.osm file from object survey result.

![Instances folder in ODK folder and the survey result in instances folder](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0222_Instances_folder_in_ODK_folder_and_the_survey_result_in_instances_folder.png)
<p align="center"><i>Instances folder in ODK folder and the survey result in instances folder</i><p align="center">


*   Before you move **instances** folder to your computer, you need to convert the folder to .zip format by pressing the **instances** folder and select **Compress**. You can change the .zip file name.

![The step for convert to .zip format](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0223_The_step_for_convert_to_zip_format.png)
<p align="center"><i>The step for convert to .zip format</i><p align="center">


*   After you move .zip file to your computer, you can upload the file to Google Drive that already set by your mapping supervisor.

![The .zip file that ready to move to computer](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0224_The_zip_file_that_ready_to_move_to_computer.png)
<p align="center"><i>The .zip file that ready to move to computer</i><p align="center">


*   You can upload the file to Survey Result folder (or another name that your mapping supervisor made) by click right on your mouse then choose **Upload Files** and choose the file that you want to upload.

![The folder on Google Drive for upload .zip file](/en/images/01-OSM-Field-Surveyor-Guideliness/02-Menggunakan-Aplikasi-ODK-Collect/0225_The_folder_on_Google_Drive_for_upload_zip_file.png)
<p align="center"><i>The folder on Google Drive for upload .zip file</i><p align="center">


**SUMMARY**

If you can follow all the stages in this module, you already then you have successfully understood the use of ODK Collect as a tool for collecting data in the field. In addition, you have also successfully implemented the operation of the initial settings in ODK Collect and how to use ODK Collect to retrieve field data. Later, you will learn about other data collection tools in the field, OpenMapKit (OMK) application.

