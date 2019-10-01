---
title: Creating survey form for ODK Collect & OpenMapKit
weight: 5
---


**Objectives:**



*   Explain the concept of XLSForm
*   Operate the creation of an XLSForm for _ODK Collect_
*   Operate the creation of an XLSForm for _OpenMapKit_

In field survey activities sometimes you need a survey form to collect the data. Imagine if you need a form survey with dozens of questions for each respondent, you will certainly experience difficulties when filling data and also when entering data into a laptop. In this material you will learn how to create a survey form in digital format which will later be entered into your mobile phone.


## I. Understanding the concept of _XLSForm_

_XLSForm_ is a standard form created to help speed up the process of creating survey forms in **Excel.** The creation of this survey form is done in an easy-to-read format and uses a familiar tool - **Excel / Google Sheets**. _XLSForm_ produces standard standards for sharing and cooperating in making survey forms. _XLSForm_ is very easy to use but can also be very complicated if you are familiar with making it. 

![Example of XLSForm](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0501_contoh_format_XLSForm.png)
<p align="center"><i>Example of XLSForm</i></p>

_XLSForm_ will then be converted to _XForm_, an open standard format, where the format allows you to create a form with very complex functions, such as multilevel questions, into a format that has been recognized by both data collection tools or in the form of sites on the internet, as well as in mobile devices.


![Examples of XForms format](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0502_contoh_format_XForm.png)
<p align="center"><i>Examples of XForms format</i></p>


The main requirement in making _XLSForm_ is the final survey form must in this type of **Microsoft Excel** format (_.xls_ or _.xls_).If you create survey forms using other applications such as **Google Sheets** or **Libre Office**, you must ensure that the final file is saved informat _.xls_ or _.xlsx_.


## II. Making XLSForm for ODK Collect applications 

You certainly understand how to use _ODK Collect_ described in the **Using the ODK Collect application**module. All questions that appear on _ODK Collect_ made in format _XLSForm_. Now we will learn how to create forms survey so they can be displayed in _ODK Collect_.



### 1. Standard Format

In making survey forms, there are some conditions that you must follow so the survey forms that we make can be changed into format _XForm_. Some rules that must befollowed to create an appropriate survey form are:

#### a. Three main worksheets /_sheets_ .

In the _spreadsheet_ we create, it must consist of 3 main worksheets, the named worksheet _**survey, choices, settings.**_ The naming of this worksheet must match and must not be mistaken because it will fail when _uploading_ your survey form.


![Three main worksheets in each XLSForm](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0503_tiga_lembar_kerja_utama.png)
<p align="center"><i>Three main worksheets in each XLSForm</i></p>

The first worksheet is **_survey_.** On this worksheet, all questions we make must be put on this worksheet. All questions that we make do not need to be included with the list of answers. All the list of answers we need will refer to the next worksheet.

The second worksheet is **_choices_**. On this worksheet we include all of our answer lists for each question that requires answer choices. 

The third worksheet is **_settings_.** On this worksheet we can only enter the name of our form if the name of our form is different from the name of our file. For example, if our file name is _form_survei_air_bersih_.xls then in this worksheet we can name our form with the name we want, for example the _Water Condition Form_.

#### b. Three main column names.

On each worksheet there must be two or three different column names on each worksheet. The column names for each of these worksheets are also different.

##### b.1. *Worksheet survey*

In **survey** worksheet we have to insert three columns name: **type, name,** and **label.** Column with name **type** indicates the type of question that will appear later, whether the question is in the form of choices, free entries or capture locations. 

Column with **name** indicates the unique variable for each question list. These variables cannot be the same, do not use spaces, and are only numbers, letters or underscores.  

Column **label** shows the question that will appear on the user's mobile device. There is no standard format for this column, you are free to use letters, numbers, and special characters in this column.

![Examples of columns for survey worksheet](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0504_ct_kolom_survey.png)
<p align="center"><i>Examples of columns for survey worksheet</i></p>

##### b.2. *Worksheet choices*

At the **choices** worksheet we have to insert three columns namely **name**, **list_name**, & **label.** Inc **list_name** you create a group that contains a set of answer choices. For example like a set of answer choices that will appear under multiple choice questions. For naming variable in ***list_name*** this must follow the naming provided in **survey** worksheet. For example on **survey** worksheet we enter a multiple choice type with the name **select_one jns_bencana**. So on the **choices** worksheet we must fill ***list_name*** with name **jns_bencana**. This will be explained further in the next discussion.


Column **name** has the same rules as column **name** on the **survey** worksheet. All must be in unique variables that are not the same as the others both on the **survey** worksheet or **choices**; do not use spaces but are replaced by _underscores_; and do not use special characters such as question marks, exclamation marks, etc.


Column **_label_** has the same rules as column **label** on the **survey** worksheet. This column contains the answer text that will appear on the user's cellphone. You can freely use spaces, special characters or letters in this column.


![Examples naming column on the choice worksheet](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0505_penamaan_kolom_choices.png)
<p align="center"><i>Examples naming column on the choice worksheet</i></p>

##### b.3. *Worksheet settings*

Worksheet **_settings_** used when you want to make additional settings such as giving the name of your survey form, giving form a specific id, and version of your survey form. In order to use this feature, you must provide these three column names: **form_title, form_id,** & **version**. 


Column **form_title,** you can provide free naming for your form. This naming will later appear on the user's cellphone. 


Column **form_id**, you can provide your form id. The terms for naming this column are that you can't have the same id as the other forms, don't use spaces, and don't use special characters.


Column **version**, you can provide a version of your form. Adding column **version** is not mandatory. If you frequently add / change your survey forms, by providing column **version**, it will be easier for you to upload the forms on the server.

![Examples of settings on the worksheet settings](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0506_pengaturan_settings.png)
<p align="center"><i>Examples of settings on the worksheet settings</i></p>



#### c. All entries must be in a standard format and starting from the first box.

One of the most important requirements is that when we make a survey form, everything must start in the _field /quadrant **A-1.**_

![Initial position of making survey forms](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0507_posisi_awal_membuat_formulir_survei.png)
<p align="center"><i>Initial position of making survey forms</i></p>

All entries form must start in those quadrant/_field_ because the system will convert _spreadsheet_ file to _XForm_, so if you do not start from that position, and error will occur in the system.

In addition, the other main requirement is that you cannot use table formats such as *merge, center, hide row / coloum, wrap text,etc*. Everything must be in a standard format. Settings that we can use are to add letters in bold, give color to columns or rows, and change the shape and size of letters.

### 2. Types of Standard Questions

In the paper survey form, we usually find several questions such as short answers, long answers, entering the date of birth, and multiple choices. Some of these questions, have different type questions, such as: 

#### a. Question type *text*

This type will generate a type of question with a free response question format. Users can freely enter numbers, letters, and special characters if we use this type of question.


![Examples ofquestion text](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0508_contoh_tipe_pertanyaan_text.png)
<p align="center"><i>Examples ofquestion text</i></p>



#### b. Question type *Integer / decimal*

This type of question will produce a question format with answers of integer numbers (specifically for **integer** type) or decimal numbers (specifically for **decimal** type). Users can only enter numbers with this type of question, a combination of numbers and letters cannot be entered if we use this type of question.

![Example question for integer type](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0509_contoh_tipe_pertanyaan_integer.png)
<p align="center"><i>Example question for integer type</i></p>

#### c. Question type *select_one*

This type of question will give the user a choice of answers where the user may only choose one answer. In creating this type of question, you must use a format such as **select_one [options]**. Where **[option]** is a group variable that will be included in the **list_name** inside worksheet **choices**.

![Example question type select_one](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0510_contoh_select_one.png)
<p align="center"><i>Example question type select_one [options]. Note that the list_name matches with  [options] in survey worksheet.</i></p>

#### d. Question type *select_multiple*

This question type is the same as the previous question type. The answers presented to the user are of several choices and the user may choose more than one answer. The rules for creating this type of question are the same as **select_one**. You must use a format such as **select_multiple [option],** where **[option]** is a group variable that will be included in **choices** under **list_name**.


![Example question type select_multiple](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0511_contoh_select_multiple.png)
<p align="center"><i>Example question type select_multiple [options]. The option in the picture above is the floodcause which also appears in the worksheet choices.</i></p>

#### e. Type of *geopoint*

This type of question will ask the user to record the coordinates of their position and will produce data in the form of latitude and longitude coordinates. 


![Example of question using geopoint](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0512_contoh_geopoint.png)
<p align="center"><i>Example of question using geopoint</i></p>

#### f. *Note*

This type is used to add a note or notification page. Users will be presented with a single page containing only the appearance of the text without having to fill in any information. For the writing format, it still follows the writing conventions in **label**, where we are free to give any writing format.

![Examples of using note](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0513_contoh_note.png)
<p align="center"><i>Examples of using note</i></p>


#### g. *image, video or audio*

This type of question will ask the user to take a picture, sound or video. 

     
![Example of using image type](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0514_contoh_image.png)
<p align="center"><i>Example of using image type</i></p>

### 3. Additional Format

You can directly use your survey form by simply entering a number of standard question types that have been explained previously. The more you are good at creating _XLSForm_, you might ask if there are other types of questions that can make your survey forms easier to use and retrieve data according to your wishes. To see all types of questions that can be used in making _XLSForm_, you can go to the site [http://xlsform.org](http://xlsform.org). In this material, we will only discuss a few types of additional questions that you can use if you want to make your survey form more informative and easier to use.

#### a. *Hint*

Hint is one additional feature that we can add to our digital survey forms. By using this feature, we can provide additional information or instructions on how to fill in a question that we make. To create this feature, we must add a new column to **survey** worksheet called **hint**. By adding this column, for each type of question we make, we can add it with the information, such as instructions to filling the form, in column **hint**.

![Examples of using thecolumn hint](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0515_contoh_kolom_hint.png)
<p align="center"><i>Examples of using thecolumn hint</i></p>

#### b. *Required*

This feature is needed if on your survey form, there are questions that must be answered. By using this feature, users will not be able to fill in further questions if they have not answered the question first. The types of questions that use this feature will also have a red asterisk when viewed on your phone. To use this feature, you only need to create a new column called **required** that is located on **survey** worksheet. In order to set questions becomes mandatory, you must add the value **yes** in this required column.

![Example required](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0516_contoh_penggunaan_fitur_required.png)
<p align="center"><i>Example of using required features. Any questions that activate this feature cannot be skipped by the user if they are not already filled in.</i></p>

#### c. *Field-list*

The function of this feature is that users will be presented with a number of questions on just **one page** on the application screen. By default, each page will only be presented with one question. If we want all questions to appear on one page, then we must use this feature.

To enable this feature, you must make a number of settings:

1.  You must insert format **begin_group** at the beginning of the question that you want to display on one page and **end_group** at the end of the question that you want to display on one page. These **begin_group** and **end_group** formats must be in the column **type**. By tucking in this format, the system will read that all questions that are after **begin_group** and before **end_group** format are one question group.
   
2. After you have created the question group, you must add column **appearance** and fill with **field-list** format. By adding this column, you inform the system that all groups of questions that you have created, will be included in a single page list.

![Example of using the field-list feature in several groups of questions](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0517_contoh_field-list.png)
<p align="center"><i>Example of using the field-list feature in several groups of questions</i></p>

#### d. *Relevant*

This feature allows us to make a list of questions that follow the answers to the previous questions. Suppose we are asked a question about "What causes floods?" With the answer choices "A. Bad Drainage B. Garbage C. Others". When we answer "C. Other", then the next question will only relate to the previous (other) type of answer, such as "Because in the previous question you answered others, explain further about the causes of other floods". The question will not appear if we answer with other answers such as "A. Bad Drainage". How to enable this **relevant** consists of several stages:

1. Creating the initial question type

    Before using **relevant**, you must first create an Initial question that you will enter into format **relevant**. For example, by using the type question **select_one**:

    ![Example questions on survey worksheet](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0518_contoh_lembar_kerja_survey.png)
    <p align="center"><i>Example questions on survey worksheet</i></p>

1. Making choices on **choices** worksheet

    After you make the initial question, the next step is you have to make the choice of answers on **choices** worksheet. 

    ![Example answer choices on theworksheet choices](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0519_contoh_pilihan_jawaban_choices.png)
    <p align="center"><i>Example answer choices on theworksheet choices</i></p>

1. Insert **relevant** features in the next question

    After you make the initial question and answer choices, the next step is you will make the question that will appear in accordance with the answer choices selected in the previous question. For example, in the previous question, you chose the **prasasti** for the type of object in question, then the next question will be specific only about the **prasasti**. To enable this feature, you must enter an additional column named **relevant** on **survey** worksheet. After entering additional columns you can fill in the question rows that require **relevant** functions with the format:

    |Format                    | Deskripsi                           |
    |--------------------------|-------------------------------------|
    |${field_name} = ‘choice’  | For type select_one only          |
    |selected(${field_name}, ‘choice’) | For type select_multiple & select_one|

    For **field_name** refers to the variable that you specified earlier in the **name** column on the **survey** worksheet. Meanwhile, **choice** refers to the variable of choice of answers available on the **choices** worksheet.

    ![Example of making relevant features](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0520_contoh_pembuatan_fitur_relevant.png)
    <p align="center"><i>Example of making relevant features</i></p>


## III. Creating survey forms for theapplication _OpenMapKit_

In addition to using _ODK Collect_, for data collection in the field we also use _OpenMapKit_. You certainly understand how to use _OpenMapKit_ for data collection in the field. If you don't know it yet, you can read the **Using the OpenMapKit Application** module. Now we will learn how to create survey forms for use in _OpenMapKit_.

Generally, creating survey forms for _OpenMapKit_ follows rules such as _ODK Collect_ form. Making this survey form can also be done in the same file when making _ODK Collect_. There are a number of standard settings that we must follow so that the survey form we make can be used for _OpenMapKit_.

### 1. Four main worksheets

In general, to make _OpenMapKit_ is not much different from the format ODKCollect. The worksheets needed by _ODK Collect_ are **surveys, choices,** & **settings**. But for _OpenMapKit_, we have to **add a new worksheet named osm**. 

![Main worksheet for OpenMapKit](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0521_lembar_kerja_utama_untuk_openmapkit.png)
<p align="center"><i>Main worksheet for OpenMapKit</i></p>

**osm** worksheet contains questions and answer choices that will appear on _OpenMapKit_. It is on this worksheet that we must enter all the list of questions that will appear in _OpenMapKit_. Meanwhile, three other worksheets followed the rule when making _ODK Collect_.

### 2. Types of main questions

In order for the questions that we make successfully raised in _OpenMapKit_, we have to enter a special type of question, which is **osm**. By entering this question into **survey** worksheet, the system will bring up all the questions in _OpenMapKit_ that we have created on **osm** worksheet.

This type of question must be followed by a variable that need to be linked to the variable in **list name** column on **osm** worksheet.

![Types osm question with the same variables on osm worksheet](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0522_tipe_pertanyaan_osm.png)
<p align="center"><i>Types osm question with the same variables on osm worksheet</i></p>

### 3. Three main columns

On **osm** worksheet, we must enter three main columns, namely **list name**, **name**, and **label**. The **list name** column contains questions and answer choices. The **name** column contains the unique variables that follow thes tandards _key_ and _value_ of _OpenStreetMap._ For a list of _keys_ and _values,_ you can look at the **Data Model _OpenStreetMap_** module or you can go directly to the site [https://wiki.openstreetmap.org/wiki/Map_Features](https://wiki.openstreetmap.org/wiki/Map_Features) and [https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines](https://wiki.openstreetmap.org/wiki/Id:Indonesian_Tagging_Guidelines). 
     
![name column follows the key and value rules on OSM](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0523_aturan_key_dan_value_pada_osm.png)
<p align="center"><i>name column follows the key and value rules on OSM</i></p>

### 4. Questions and answer choices in one worksheet

Unlike creating survey forms for _ODK Collect_, where each question and answer choices are separate on different worksheets, for creating survey form in _OpenMapKit_ we must enter all questions and choices answers on one worksheet.

## IV. Exercises to Create Survey Forms _ODK Collect_ and _OpenMapKit_

Until now we have understood how to create survey forms for _ODK Collect_ and _OpenMapKit_. Now we will try to make a survey form that can be used for both of these applications.

Imagine that you currently want to conduct data collection activities at a facility by using _ODK Collect_ and _OpenMapKit_. Some data that you want to collect are:

*   name _Surveyor_. (Required)
*   To be at a disaster-prone location or not
*   If at the disaster location, specify the type of disaster (can be more than one answer)
*   Coordinates of the location of survey objects
*   Name of place of amenity
*   Type of amenities Amenity
*   complete address of the

From the data above, you have successfully identified which types questions that go into survey forms _ODK Collect_ and any kind of questions that go into survey _OpenMapKit_ form. Questions that enter into _ODK Collect_ are the **name of the surveyor, disaster-prone, type of disaster** & **coordinates of the location of the survey object**. Meanwhile the questions that go into _OpenMapKit_ are the **name of the place** & **type of amenities, and full address**. 

First of all, we have to make a survey form for _ODK Collect_. As the requirements you have learned before, in _spreadsheet_ we have to make four worksheets, which are **survey, choices, settings** & **osm.**

After that, on the **survey** worksheet we must provide our main column, which is **type, name** & **label**. The types of questions we have to make for this survey form are **text, select_one, select_multiple,** & **geopoint**. Because surveyor questions are mandatory questions, we must use **required** on **survey** worksheet. Apart from that we also have to use **relevant** for disaster type questions. This **relevant** feature will make it easier for us to make a conditioned question.

![Type questions on the worksheet survey](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0524_tipe_pertanyaan_untuk_lembar_kerja_survey.png)
<p align="center"><i>Type questions on the worksheet survey</i></p>

On **choices** worksheet we put the answer choices for the type of questions **select_one** and **select_multiple** that we have created on the **survey** worksheet. Here we have to make three main columns namely **list_name, name,** & **label**.

![The answer choices entered in worksheet choices](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0525_pilihan_jawaban_lembar_kerja_choices.png)
<p align="center"><i>The answer choices entered in worksheet choices</i></p>


Because we want to use _OpenMapKit_ for our field data collection, we have to add the type of questions that will lead us to _OpenMapKit_, the type of questions we have to enter is **osm**. On **osm** worksheet, we include all questions related to _OpenMapKit_. In the variable **name** we must refer to the _key_ and _value_ on the _OpenStreetMap_ wikipedia .

![Fill in the survey and osm](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0526_isi_lembar_kerja_survey_dan_osm.png)
<p align="center"><i>Fill in the survey and osm</i></p>

Finally, in **settings** worksheet we enter our form id and the title of our form. On this worksheet, only two main columns are needed, namely **form_id** and **title.**

![Examples of settings on the worksheet settings](/en/images/06-OSM-Field-Survey-Manager-Guidelines/05-Membuat-Formulir-Survei-untuk-Aplikasi-ODK-Collect-&-OpenMapKit/0527_contoh_pengaturan_pada_lembar_kerja_settings.png)
<p align="center"><i>Examples of settings on the worksheet settings</i></p>


## SUMMARY

Congratulations! Currently you have successfully created a survey form for _ODK Collect_ and _OpenMapKit applications_. To find out more about the types of questions that can be made on _ODK Collect_, you can directly access the page [http://xlsform.org](http://xlsform.org). Making the right form will make it easier for surveyors to collect data in the field.


