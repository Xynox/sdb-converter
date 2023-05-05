# sdb-converter

## Voraussetzungen
- Python 3.10
- Pandas Library
-  genügend Speicherplatz (variabel, je nach Größe der Datenbanken)
- Klassenliste aus Sibank (zu "sibank_classes.csv" umbenennen!)
- Elternzugänge aus Sibank (zu "sibank_ez1.csv" & "sibank_ez2.csv" umbenennen!)
- *später Iserv Accountdatenbank (zu "iserv_account_data.csv" umbenennen!)*

## Installation
1. Python herunterladen, dabei "PATH"-Variable im Installer aktivieren (python.org/downloads)
2. WIN + R ---> cmd
3. Dort "pip install pandas" eingeben (falls pip nicht vorhanden ist, `python3 -m ensurepip` ausführen)
4. Repository herunterladen
5. main.py ausführen

## Funktionsweise
### **ACHTUNG: DIE REIHENFOLGE DER SCHRITTE IST WICHTIG!**
1. Zunächst fragt das Programm nach einem Modus. Daraufhin muss Modus 1 ausgewählt werden.
2. Falls die Ordner nicht vorhanden waren, werden nun 2 Ordner namens "import_dateien" und "export_dateien" erstellt.
3. In den Import-Ordner muss nun "sibank_classes.csv" abgelegt werden.
4. Das Programm wandelt die Klassenliste in das Iserv-CSV-Format *(in export_dateien ---> "iserv_nutzer_converted.csv")* um und beendet sich. Diese CSV-Datei muss nun bei Iserv importiert werden. Die daraus entstehende Accountdatenbank muss nun exportiert werden.
5. Nun das Programm wieder starten und Modus 2 auswählen.
6. In den Import-Ordner muss nun "iserv_account_data.csv" abgelegt werden.
7. Das Programm wandelt nun die Elternliste einmal für WebUntis um *(in export_dateien ---> "webuntis_elternzugang1_converted.csv" und "webuntis_elternzugang2_converted.csv")* und erzeugt die Datei für die Mailingliste *(in export_dateien ---> "mailingliste_converted.csv")*. Danach beendet sich das Programm wieder.
8. Hiernach das Programm wieder starten und Modus 3 auswählen. Hierfür müssen keine weiteren Dateien bereitgestellt werden. **ACHTUNG: AUF KEINEN FALL DATEIEN AUS DEM EXPORT-ORDNER ZU DIESEM ZEITPUNKT ENTFERNEN - MODUS 3 MUSS AUF EINE DIESER DATEIEN ZUGREIFEN!**
9. Das Skript hat nun auch die Schülerzugänge konvertiert.
10. Alle verschiedenen Dateien sind nun im Export-Ordner vorzufinden und können ab diesem Zeitpunkt verändert werden.

## Fehler
Bei Fehlern bitte einen Screenshot von dem Fehler machen und ein Issue auf GitHub eröffnen. So kann ich Fehler am besten ausmerzen.

##### Made with ❤️ by Xynox (Joel W.) ©️ 2023
