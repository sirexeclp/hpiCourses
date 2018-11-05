# Report

## Description

### Task

Find interesting courses based on parameters such as ECTS Points, style of Course (eg. lecture, seminar, project), etc.
Find information about your choosen courses (eg. slides, creditability).

### Dataset

Our Dataset contains:

- course name
- enrolment dealine
- teaching form
- enrolment type
- course language
- maximum participants
- weekly hours
- credits
- graded: bool
- course website of the chair
- creditabililty
- pdf files linked on course site

## Problems

Websites don't use id-tags for most elements, so XPATH expressions needed to rely on heading text, etc.
No common format for websites of chairs. Different URLs lead to essentially the same website, but slightly adapted for field of study (eg. duplicate Websites for Data Prep for ITSE and DE). 
Inconsistencys in the field teaching form (eg. 'SP', 'Seminar/Projekt', 'Projekt/Seminar'), missing values (eg. teaching language).

## Method

We used python to crawl the HPI websites. A combination of XPATH and regex have been used to extract usefull information from the different sites.
Googles OpenRefine was used to refine the data and clear up some inconsistencys. 

## Libs

The following python librarys were used:

- requests webrequests/scraping
- lxml		xpath 
- pandas	dataframes
- urllib	handling urls/creating full path urls
- numpy
- pickle	saving intermediate data
- re		regular expressions

## Manual editing

Manual editing was done for correcting incosistencys in the teaching form field.

## Concrete steps

1. Crawl the [main hpi courses website]("https://hpi.de/studium/lehrveranstaltungen") to obtain a list of courselists (eg. Bachelor, Master courses, etc.) 
2. Crawl each table-page with courses and returns a dict with coursename and URL to coursepage.
3. Combine the list of dicts to one big list, which only contains URLs.
4. Downloads the individual course websites.
5. Use XPATH to extract information from the course websites. Store it in a dict.
6. If coursewebsite links to a coursesite from the chair, download the chair site as well.
7. Finds all Links, on the websites that destination ends with the given fileextension (eg. '.pdf', '.pptx').
8. Create Pandas dataframe.
9. Use pandas built in methods to remove duplicates and save the result as .csv file.
10. Import csv in OpenRefine.
11. Use OpenRefine to remove incosistencys in some columns.
