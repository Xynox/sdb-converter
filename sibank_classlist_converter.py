import pandas as pd
import csv
import logging

""" Folgende Funktion ist der Klassenlistenkonvertierer
Zunächst werden die Dateien über die Pandas-Library eingelesen und in ein Dataframe (interne Tabelle der Pandas Library) konvertiert
Danach wird unter jedem Header "KLASSE" die Werte "Q1" & "Q2" gesucht und per Regex alle folgenden Zeichen gelöscht.
Folgend wird der Dataframe exportiert. Die Parameter bedeuten folgendes:

index=False: Es werden die Nummern für die Zeilen des Dataframes nicht in der CSV-Datei ausgegeben
header=True: Der ursprüngliche Header wird beibehalten
index_label=False: Genauso wie index=False
quotechar='"': Zeigt an, dass alle Einträge mit Anführungszeichen gewrapped werden sollen
quoting=csv.QUOTE_ALL: Alle Werte werden in Anführungszeichen gewrapped """


def classlistConverter():

    csv_file = pd.read_csv(
        "./import_dateien/sibank_classes.csv", sep=",", quotechar='"')
    dataFrame = pd.DataFrame(csv_file)
    logging.info("CSV-Datei wurde importiert und kann modifiziert werden!")

    dataFrame["KLASSE"].replace(
        to_replace='Q1.*', value="Q1", regex=True, inplace=True)
    dataFrame["KLASSE"].replace(
        to_replace='Q2.*', value="Q2", regex=True, inplace=True)

    logging.info("DataFrame wurde editiert, Q1 und Q2 wurden ersetzt!")

    dataFrame.to_csv("./export_dateien/iserv_nutzer_converted.csv",
                     index=False, header=True, index_label=False, quotechar='"', quoting=csv.QUOTE_ALL)
    logging.info("Erfolgreich DataFrame in CSV-Datei exportiert!")

    print("Sibank Klassenliste wurde erfolgreich eingelesen und konvertiert!")
