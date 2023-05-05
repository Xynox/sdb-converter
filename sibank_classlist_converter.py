# todo: this program will go through the provided Sibank classlist and change all Oberstufe classes into their respective Stufe (Q1xxx; Q2xxx --> Q1; Q2)
# this will export the updated list into Iserv .csv sheets, for the Iserv users and the SBA
# WILL BE FUNCTION NO 1

import pandas as pd
import csv
import logging


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
