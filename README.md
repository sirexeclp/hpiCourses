# hpiCourses
ganz tolles Readme haben wir hier :)

## Abhängigkeiten

Folgende Pakete müssen installiert sein:

- lxml
- requests

    pip install -r requirements.txt

## ER-Model

![Ein Bild des ER-Models](ER-Model/HPICoursesERModel.PNG "Hier könnte ihre Werbung stehen!")

## Abfolge

### Übersichtsseite mit Studiengängen

Holen der Liste von Studiengängen von:
[https://hpi.de/studium/lehrveranstaltungen.html](https://hpi.de/studium/lehrveranstaltungen.html)
![Ein Bild LV-Website](img/LV-list.png "Hier könnte ihre Werbung stehen!")

### Liste der LVs für jeden Studiengang

Holen der Liste aller LVs für jeden Studiengang und erstellen einer Liste mit Links zu den Seiten der LVs.

[https://hpi.de/studium/lehrveranstaltungen/it-systems-engineering-ma.html](https://hpi.de/studium/lehrveranstaltungen/it-systems-engineering-ma.html)
![Ein Bild LV-Website für ITSE](img/LV-list-ITSE.png "Hier könnte ihre Werbung stehen!")

### Informationen von LV-Seiten sammeln

Holen aller LV-Seiten und extraktion von wichtigen Infos.

[https://hpi.de/studium/lehrveranstaltungen/it-systems-engineering-ma/lehrveranstaltung/course/0/wintersemester-20182019-data-preparation-for-science.html](https://hpi.de/studium/lehrveranstaltungen/it-systems-engineering-ma/lehrveranstaltung/course/0/wintersemester-20182019-data-preparation-for-science.html)
![Ein Bild der Data-Prep Seite](img/DataPrep1.png "Hier könnte ihre Werbung stehen!")

Suchen nach Link zur Kursseite des Lehrstuhls.
[https://hpi.de/naumann/teaching/teaching/ws-1819/data-preparation-for-science-ps-master.html](https://hpi.de/naumann/teaching/teaching/ws-1819/data-preparation-for-science-ps-master.html)

![Ein Bild der Data-Prep Seite des Lehrstuhls](img/DataPrep2.png "Hier könnte ihre Werbung stehen!")

Suche nach Links die auf PDF Dokumente zeigen (potenzielle Vorlesungsfolien).

