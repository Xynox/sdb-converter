# todo: this program will use the generated iserv user file as input as well as the classlist
# puts together the whole classlist + an additional field at the back containing the iserv-email

from sibank_classlist_converter import *
import pandas as pd
import csv


def webUntisStudentConverter():

    baseFile = pd.read_csv(
        "./export_dateien/iserv_nutzer_converted.csv", sep=",", quotechar='"')
    dataFrame_base = pd.DataFrame(baseFile)

    iserv_file = pd.read_csv(
        "./import_dateien/iserv_account_data.csv", sep=";", quotechar='"')
    dataFrame_iserv = pd.DataFrame(iserv_file)
    logging.info(
        "CSV-Dateien für Schüler wurden importiert und können modifiziert werden!")

    dataFrame_iserv.drop(columns=["Account", "Vorname", "Nachname", "Status", "Erstellt am",
                         "Erstellt von", "UUID", "Benutzertyp", "Import-ID", "Klasse/Information", "Gruppen"], inplace=True)

    concatFrames = [dataFrame_base, dataFrame_iserv]
    dataFrame_student = pd.concat(concatFrames, axis=1)

    logging.info(
        "Erfolgreich unnötige Header gelöscht und mit Klassenliste verbunden!")

    dataFrame_student.rename(
        columns={"E-Mail-Adresse": "EMAIL-ADRESSE"}, inplace=True)

    dataFrame_student.to_csv("./export_dateien/webuntis_schülerzugang_converted.csv",
                             sep=',', quotechar='"', quoting=csv.QUOTE_ALL, index=False, header=True, index_label=False, float_format='%.0f')

    logging.info("Erfolgreich CSV-Datei für Schülerzugang erstellt!")

    print("Schülerzugänge wurden erfolgreich konvertiert!")
