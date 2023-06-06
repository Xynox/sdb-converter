# sdb-converter

## Voraussetzungen
- mindestens Python 3.10
- **Pandas Library**
- Klassenliste aus Sibank ***(zu "sibank_classes.csv" umbenennen!)***
- Elternzugänge aus Sibank ***(zu "sibank_ez1.csv" & "sibank_ez2.csv" umbenennen!)***
- *später Iserv Accountdatenbank ***(zu "iserv_account_data.csv" umbenennen!)***

## Installation (Windows)
1. Python herunterladen, dabei **"PATH"-Variable im Installer aktivieren** (python.org/downloads)
2. WIN + R ---> cmd
3. Dort "pip install pandas" eingeben (falls pip nicht vorhanden ist, `python3 -m ensurepip` ausführen)
4. Repository herunterladen
5. main.py ausführen

## Funktionsweise
### **ACHTUNG: DIE REIHENFOLGE DER SCHRITTE IST WICHTIG!**
### **DIE EXPORT-DATEIEN BIS ZUM BEENDEN DES PROGRAMMS NICHT ENTFERNEN ODER UMBENENNEN!
1. Falls die Ordner nicht vorhanden waren, werden nun 2 Ordner namens "import_dateien" und "export_dateien" erstellt.
2. In den Import-Ordner muss nun "sibank_classes.csv" abgelegt werden. Falls die Dateien nicht vorhanden sind oder falsch benannt sind, wird das Programm die Abfrage immer wieder wiederholen, bis der exakte Name vorhanden ist.
3. Das Programm wandelt die Klassenliste in das Iserv-CSV-Format *(in export_dateien ---> "iserv_nutzer_converted.csv")* um. Diese CSV-Datei muss nun bei Iserv importiert werden. **Die daraus entstehende Accountdatenbank muss nun exportiert werden.**
4. In den Import-Ordner muss nun "iserv_account_data.csv" abgelegt werden. Falls die Dateien nicht vorhanden sind oder falsch benannt sind, wird das Programm die Abfrage immer wieder wiederholen, bis der exakte Name vorhanden ist.
5. Das Programm wandelt nun die Elternliste einmal für WebUntis um *(in export_dateien ---> "webuntis_elternzugang1_converted.csv" und "webuntis_elternzugang2_converted.csv")* und erzeugt die Datei für die Mailingliste *(in export_dateien ---> "mailingliste_converted.csv")*. Danach werden auch die Iserv-Elternzugänge erstellt *("iserv_elternzugänge_converted.csv")*.
6. Das Skript konvertiert die Schülerzugänge für WebUntis danach automatisch und speichert sie als *"webuntis_schülerzugang_converted.csv"* ab.
7. Alle verschiedenen Dateien sind nun im Export-Ordner vorzufinden und können ab diesem Zeitpunkt verändert werden.

## Fehler
Bei Fehlern bitte einen Screenshot von dem Fehler machen und ein Issue auf GitHub eröffnen. So kann ich Fehler am besten beheben.

##### Made with ❤️ by Xynox (Joel W.) © 2023
