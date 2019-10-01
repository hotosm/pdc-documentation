---
title: Upload survey form to ona.io
weight: 6
---


**Learning Objectives:**



*   Able to explain the benefits of using Ona.io
*   Explain how to upload survey forms to the Ona.io server

After we have successfully created the survey forms that have been studied in the module **Making Survey Forms for the ODK Collect & OpenMapKit Application**, You will learn the platform used to upload survey forms to one of the platforms. The platform used in this material are Ona.io.  Ona.io is a platform that can be used to place survey forms which will be used for field survey activities using _ODK Collect_ or _OpenMapKit_. Here you will learn what can be done using _Ona.io_ and how to upload the survey form into Ona.io.


## I. Introduction to _Ona.io_

### a. What is _Ona.io_

_Ona.io_ is a social enterprise that builds infrastructure data for data collection needs in the field. They provide several platforms that can be used to assist data collection, one of which is a field data storage platform. You can upload your survey form to the server provided by _Ona.io_ and then you use it for your field activities. _Ona.io_ provides several capabilities that will assist data collection activities. One of them is:

*   Statistics of the amount of data entered in the form of graphs and tables
*   Location map of the distribution of data collected in the field
*   Display of images that were successfully collected during data collection
*   Ability to download data in several types of files such as _CSV, XLS, KML, Osm_ or _Json_


### b. Limitations in _Ona.io_

If you want to use the Ona.io platform you can create an account for free and then use the platform to upload survey forms. But there are some restrictions on using a free account on Ona.io:

*   Can only create one private project
*   For a private project can only hold 500 data entry.
*   In one private project can accommodate as many as 10 types of survey forms


## II. Survey Form Management on _Ona.io_

Now that you know what is _Ona.io_ and its limitations, in this module you will now try to upload the survey forms that you created earlier in the **Create Form Survey for ODK Collect and OpenMapKit** module. If you have not created a survey form, you can download a sample survey form by accessing the link: [http://bit.ly/sample_form_survey](http://bit.ly/sample_form_survey). 


### a. Creating an account on _Ona.io_

Before you _upload_ your survey form, you must have an account on _Ona.io_ first. To create an account on _Ona.io_ click on the button **Get Free Account** and then enter your name (lowercase) which will be the _url_ where you save the form and will later be used in the _ODK Collect._

![Display create account on Ona.io](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0601_tampilan_ona.io.png)
<p align="center"><i>Display create account on Ona.io</i></p>

### b. Upload Survey Form

First time you successfully create an account on _Ona.io,_ you will automatically create a personal project with your own name. 

![Private project with your own account name](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0602_proyek_nama_akun_anda_sendiri.png)
<p align="center"><i>Private project with your own account name</i></p>

To _upload_ your form, click on the name of your own project. After successfully entering into your project. Click on the **_Add a form_** button and a new window will appear. Here you are asked to enter _the XLSForm file_. Select _file_ your survey form. After you have successfully selected _file_ your survey form, click on the **_Upload Selected File_**. The system will check whether your form has errors or not. 

![Display window when uploading survey forms](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0603_tampilan_meng-upload_formulir_survei.png)
<p align="center"><i>Display window when uploading survey forms</i></p>

If you have successfully uploaded survey forms, a pop up of will appear **Verified Form.** Click on the **Save form** button to immediately save the survey form.

![Select Save Form to save the verified form](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0604_save_form_untuk_menyimpan_formulir.png)
<p align="center"><i>Select Save Form to save the verified form</i></p>

### c. Changing survey forms

If you make changes in survey forms that have been successfully uploaded to your project, you can update the survey forms. But the thing to remember is that **when you update your survey form, if the form has already been filled out with some data, then there is a potential that the data already entered will be deleted**. Therefore, before you change survey forms, it is recommended to download your data first in case something goes wrong.

To replace your survey form, click on the down arrow located to the far right of your survey form. Then select **_Replace Form_**. 

![Click on the right side of your survey form to bring up the Replace Form menu](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0605_replace_form.png)
<p align="center"><i>Click on the right side of your survey form to bring up the Replace Form menu</i></p>

If your survey form already contains some fields, a warning will appear so the users can understand the consequence when changing survey forms, especially replacing variables, _Ona.io_ will use the new variables contained in the new survey form.

![Warning When Changing the Survey Form](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0606_peringatan_saat_mengganti_formulir_survei.png)
<p align="center"><i>Warning When Changing the Survey Form</i></p>

After you click thebutton **_I Understand_**, you will be directed to a window to upload the survey form. Select your new survey form and click **_Upload Selected file_**. After the form has been successfully validated, click on thebutton section **Save form**.


### d. Delete / Deactivate Survey Forms

If you have survey forms that you want to delete / deactivate. You can do this by selecting the ↓ arrow located to the right of your survey form and then selecting **_Delete Form_ **to erase or **_Make inactive_ **to deactivate your form.

 ![Display to delete or deactivate survey forms](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0607_menghapus_atau_menonaktifkan_formulir_survei.png)
<p align="center"><i>Display to delete or deactivate survey forms</i></p>


```
Note:
If you choose to Delete Form. You will be asked to rewrite the name of your survey form before you can delete your survey form.
By selecting Make inactive, your survey form will not appear in ODK Collect during the stage of getting the blank form in ODK Collect.
```



### e. _Downloading_ XLSForm

You can download XLSForm format of the survey forms that you have created by clicking the arrow ↓ at the right part of your survey form and then select **_Download XLSForm_**. 


### f. _Download_ Survey Results

To download data from the survey. You must first choose your survey form. After you have successfully selected the survey form, you will be directed to the survey form management page.

![View to download survey data](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0608_mengunduh_data_hasil_survei.png)
<p align="center"><i>View to download survey data</i></p>

Click on thebutton **_Prepare Data Export_** to start downloading your survey form data. After that you will be directed to choose the type of _file_ you want to download. 

![Choice of file types that you can download](/en/images/06-OSM-Field-Survey-Manager-Guidelines/06-Meletakkan-form-survey-ke-Ona.io/0609_pilihan_jenis_file_yang_dapat_anda_unduh.png)
<p align="center"><i>Choice of file types that you can download</i></p> 

If your survey form does not use photos, you can choose CSV. But if your survey form uses photos, you can choose **_Zip folder of media attachment._** The process to download survey data depends on how much data you produce in the data collection activity.


The survey data from _Ona.io_ can later be used for various mapping purposes for example **_KML_** you can open it with **_Google Earth_**, with the **_OSM_** you can use **_JOSM_** application, and data with format **_CSV_** you can open with **_Spreadsheet_** or **_QGIS_**.

**SUMMARY**

Congratulations! Now you understand how to upload files survey form into one of the platforms that can be used to store survey forms online. There are several options you can use besides Ona.io to _upload_ survey forms. Ona.io can be an option because it is very easy and free to use based on the terms previously explained.

