
# Project list -- Summer 2023

## Cell images

* Stakeholders:
  * Roux contacts: Dr. Christine Lary & Dr. Michael Wan
  * MainHealth contacts: Dr. Katherine Motyl
* Story:
  * Researchers at MaineHealth and the Roux Institute are collaborating on a clinical trial to collect images 
  of human osteoclast cells from blood samples. The data collection is labor intensive and they've
  only had time to do a rough image analysis. In preparation for more extensive computer-vision analysis
  they're hoping to adapt machine learning methods that have been developed on mouse cells.
  The goal is to use the AI to detect the cells in these images.
  There are challenges with adapting the mouse-cell analysis to human cells, and they have yet to be understood.
  Dr. Michael Wan, a deep learning expert now in EAI begun collaborating on this work.
  The goal of the 5110 project will be to put together a reproducible data-processing pipeline using an 
  existing mouse-image dataset and existing algorithms. In the long run, this could inform the creation of
  an AI-based tool for scientists at MaineHealth.
* Data:
  * data will be available via dropbox
* Relevant papers and github repo
  * http://www.ncbi.nlm.nih.gov/pmc/ar8cles/PMC8186397
  * http://www.ncbi.nlm.nih.gov/pmc/ar8cles/PMC9038109
  * https://github.com/kiharalab/OC_Finder

## 911 Response

* Stakeholders:
  * Dr. Christine Lary and Dr. Qingchu Jin at The Roux Institute
  * Teresa May, OD at MaineHealth
* Story:
  * Critical Care Doctors at MaineHealth are modeling data from cardiac arrest patients in the 
  Intensive Care Unit (ICU) in order to find predictors of good or poor outcomes. 
  One of the databases they're using is the National Emergency Medical System (EMS) Information System (NEMSIS).
  The NEMSIS database contains all 911 calls nationwide.
  The full dataset for each year is huge.
  It can be sampled to pull out cardiac arrest patients and rurality.
  Researchers at The Roux Institute have only begun to look at the data
  and any interesing associations that could be explored would useful. 
  A long-term goal (beyond the scope of a 5110 project) would be an app for exploring or visualizing the data.
* Data:
  * www.nemsis.org
  * Sampled data for the project will be available via scientists at The Roux Institute.

## Digital Equity

* Stakeholder: 
  * Maine Connectivity Authority (MCA)
* Story: 
  * MCA is is a quasi-governmental agency charged with achieving the universal access of affordable 
  high-speed broadband in Maine. 
  Allocation of funds need to be distributed in an equitable fashion, and the concept of "digital equity"
  has emerged as an important metric for allocating those funds. The goal of this project is to build on
  ongoing work to define digital equity around the nation and refine it for the state of Maine.
  This project builds on previous work by DS 5010 students: https://ds5010.github.io/broadband-3
  and some DS5110 students.
* Data: 
  * Socieconomic data from the American Community Survey (census.gov) and broadband data from the FCC (fcc.gov)
  These datasets are entirely new, and were not used in previous work by DS 5010 students.
  The goal of this project is to use publicly available data to investigate possible causal relationships in Maine.

## EAI/Boston Globe

* Stakeholder: 
  * Dr. Giulia Torino, Northeastern University and EAI
* Story: 
  * The Northeastern Library has a growing archive of photographs from the Boston Globe.
  Those images need to be classified and organized, and a group of DS5110 students started working with
  the data and some deep learning CNN models in the spring of 2023.
  The current priority is to look into optical character recognition in order to automate
  transciption of the handwriting on the back of the photographs.
  This is a big-data, computer-vision task and will involve working with Dr. Torino.
* Data: 
  * Analysis will be based on a subsample of images archive. Dr. Torino is using ~200 right now.

## Equitable health care

* Stakeholder:
  * Prof. Brianne Olivieri-Mui, Dept of Health Sciences
* Story: 
  * Hundreds of millions of federal dollars have been allocated for treatment and eradication HIV. 
  The goal of this study is to look for socioeconomic factors that could give rise to more equitable 
  allocation of funds. The results could have implications for policy makers and government agencies 
  administering those funds. This project builds from previous work accomplished in DS5110 students.
  Dr. Olivieri-Mui is very interested in seeing this work continue and ready to engage as needed!
* Data: 
  * Socieeconomic data at Census.gov added as a new data source to build on work done by DS 5110 students.

## AK Walruses

* Stakeholders:
  * Paige Norris and Dr. Tony Fischbach of the USGS Alaska Ice Center
* Story:
  * This project builds on [Paige Norris' student project](https://github.com/paiyge/IceMail)
  to enable monitoring of Pacific Walrus monitoring and better understand the relationship
  to changing sea ice conditions. 
  This project will undertake a Python implementation of the original project, which used R.
  The R implementation encountered signification challenges with the geospatial analysis.
  Successful implementation in Python could lead to an official publication with the USGS.
* Data:
  * A variety of open source satellite datasets described in the 
  [USGS icemail repository](https://code.usgs.gov/asc/icemail/-/tree/master)

## Educate Maine

* Stakeholder: 
  * Jennifer Chace, now at Univ of Southern Maine, jennifer.chace@maine.edu --
  * Jennifer Chace is willing to work closely with students to develop a project idea
  that could include topic modeling (natural language processing).
* Story: 
  * Explore conversations about education throughout the state of Maine showing how
  the thoughts of concerns vary among citizens of the state, and relate these issues
  to socioeconomic factors in each region.
  This study will build on an project from Summer 2022 that focussed on text analysis of
  a relatively small dataset: https://github.com/ds5110/project-darylel.
* Data: 
  * Socioeconomic data from Census.gov can be combined with transcriptions of ongoing conversations
  around Maine collected over the last year.
  This project will build on an earlier project in the summer of 2022 that used a relatively small dataset
  from the summer of 2022 described [here](https://github.com/ds5110/project-darylel/blob/main/Manual.md) 
  and a follow-on project that looked at a more recent version of the dataset.
  Neither group did an extensive analysis of socioeconomic data.
  Oppportunities exist to build on the kind of analysis performed by
  DS5010 students who looked at digital equity in Maine: https://ds5010.github.io/broadband-3/
