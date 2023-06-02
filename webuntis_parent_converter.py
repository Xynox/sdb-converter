import pandas as pd
import numpy as np
import csv
import re
import logging


def webUntisParentConverter():

    csv_ez1 = pd.read_csv(
        "./import_dateien/sibank_ez1.csv", sep=",", quotechar='"')
    dataFrame_ez1 = pd.DataFrame(csv_ez1)

    csv_ez2 = pd.read_csv(
        "./import_dateien/sibank_ez2.csv", sep=",", quotechar='"')
    dataFrame_ez2 = pd.DataFrame(csv_ez2)
    logging.info(
        "CSV-Dateien (Erziehungsberechtigte) wurden erfolgreich importiert und können gefixt werden.")

    dataFrame_ez1["KLASSE"].replace(
        to_replace='Q1.*', value="Q1", regex=True, inplace=True)
    dataFrame_ez1["KLASSE"].replace(
        to_replace='Q2.*', value="Q2", regex=True, inplace=True)

    dataFrame_ez2["KLASSE"].replace(
        to_replace='Q1.*', value="Q1", regex=True, inplace=True)
    dataFrame_ez2["KLASSE"].replace(
        to_replace='Q2.*', value="Q2", regex=True, inplace=True)

    logging.info("DataFrames wurden editiert, Q1 und Q2 wurden ersetzt!")

    dataFrame_ez1[['EZ NAME', 'EZ VORNAME']] = dataFrame_ez1["EZ NAME, VORNAME"].str.split(
        ', ', expand=True)
    dataFrame_ez2[['EZ2 NAME', 'EZ2 VORNAME']] = dataFrame_ez2["EZ2 NAME, VORNAME"].str.split(
        ', ', expand=True)

    logging.info(
        "EZ-Namen wurden gesplittet und in zwei verschiedene Spalten konvertiert!")

    dataFrame_ez1["EZ1_Fullname"] = dataFrame_ez1["EZ VORNAME"] + \
        ' ' + dataFrame_ez1["EZ NAME"]

    dataFrame_ez2["EZ2_Fullname"] = dataFrame_ez2["EZ2 VORNAME"] + \
        ' ' + dataFrame_ez2["EZ2 NAME"]

    logging.info(
        "EZ-Namen wurden erfolgreich in einen vollen Namen konvertiert!")

    dataFrame_ez1.drop(columns=["EZ NAME, VORNAME"], inplace=True)
    dataFrame_ez2.drop(columns=["EZ2 NAME, VORNAME"], inplace=True)

    logging.info("Spalte mit Namen und Vornamen wurde erfolgreich gelöscht!")

    dataFrame_ez1 = dataFrame_ez1[["IDENTNUMMER",
                                   "FAMILIENNAME", "RUFNAME", "EZ E-MAIL", "EZ VORNAME", "EZ NAME", "KLASSE", "EZ1_Fullname"]]
    dataFrame_ez2 = dataFrame_ez2[["IDENTNUMMER",
                                   "FAMILIENNAME", "RUFNAME", "EZ2 E-MAIL", "EZ2 VORNAME", "EZ2 NAME", "KLASSE", "EZ2_Fullname"]]

    logging.info("Dokument wurde erfolgreich neu angeordnet!")

    dataFrame_ez1.to_csv("./export_dateien/webuntis_elternzugang1_converted.csv",
                         index=False, header=True, index_label=False, quotechar='"', quoting=csv.QUOTE_ALL)
    dataFrame_ez2.to_csv("./export_dateien/webuntis_elternzugang2_converted.csv",
                         index=False, header=True, index_label=False, quotechar='"', quoting=csv.QUOTE_ALL)

    logging.info("Erfolgreich alle EZ-Listen korrigiert und exportiert!")

    print("Die Sibank EZ-Listen wurden erfolgreich überarbeitet!")


def createMailingList():

    csv_iserv = pd.read_csv(
        "./import_dateien/iserv_account_data.csv", sep=";", quotechar='"')
    dataFrame_iserv = pd.DataFrame(csv_iserv)

    csv_ez1 = pd.read_csv(
        "./export_dateien/webuntis_elternzugang1_converted.csv", sep=",", quotechar='"')
    dataFrame_ez1 = pd.DataFrame(csv_ez1)

    csv_ez2 = pd.read_csv(
        "./export_dateien/webuntis_elternzugang2_converted.csv", sep=",", quotechar='"')
    dataFrame_ez2 = pd.DataFrame(csv_ez2)
    logging.info(
        "CSV-Dateien von Erziehungsberechtigten und Iserv wurden erfolgreich importiert und können zur Mailingliste hinzugefügt werden.")

    dataFrame_ez1.drop(columns=[
                       "IDENTNUMMER", "FAMILIENNAME", "RUFNAME", "EZ VORNAME", "EZ NAME", "KLASSE"])
    dataFrame_ez2.drop(columns=[
                       "IDENTNUMMER", "FAMILIENNAME", "RUFNAME", "EZ2 VORNAME", "EZ2 NAME", "KLASSE"])

    dataFrame_ez1 = dataFrame_ez1[["EZ1_Fullname", "EZ E-MAIL"]]
    dataFrame_ez2 = dataFrame_ez2[["EZ2_Fullname", "EZ2 E-MAIL"]]

    dataFrame_iserv.drop(columns=["Status", "Erstellt am", "Erstellt von",
                         "UUID", "Benutzertyp", "Klasse/Information", "Gruppen"])
    dataFrame_iserv = dataFrame_iserv[[
        "Import-ID", "Vorname", "Nachname", "Account", "E-Mail-Adresse"]]

    logging.info(
        "Bei allen Frames wurden unnötige Kategorien für Mailingliste erfolgreich entfernt!")

    concatFrames = [dataFrame_iserv, dataFrame_ez1, dataFrame_ez2]
    dataFrame_mail = pd.concat(concatFrames, axis=1)

    logging.info("Zusammenführen der verschiedenen Frames erfolgreich!")

    dataFrame_mail.rename(columns={"Import-ID": "IDENTNUMMER", "Vorname": "UserFirstName",
                          "Nachname": "UserLastName", "Account": "Username", "E-Mail-Adresse": "Email", "EZ1_Fullname": "EZ1_FullName", "EZ E-MAIL": "EZ1_Mail", "EZ2_Fullname": "EZ2_FullName", "EZ2 E-MAIL": "EZ2_Mail"}, inplace=True)
    logging.info("Erfolgreich alle Header richtig benannt!")

    dataFrame_mail = dataFrame_mail[dataFrame_mail['IDENTNUMMER'].str.isnumeric(
    )]
    dataFrame_mail = dataFrame_mail[dataFrame_mail['IDENTNUMMER'].notnull()]

    logging.info(
        "Leere Identnummern und falsche Identnummern wurden gefiltert!")

    def mailCheck(row):
        ez1_mail = row["EZ1_Mail"]
        ez2_mail = row["EZ2_Mail"]

        if not ez1_mail and not ez2_mail:
            return 0
        elif ez1_mail and not ez2_mail:
            return 1
        elif not ez1_mail and ez2_mail:
            return 2
        elif ez1_mail != ez2_mail:
            return 3
        else:
            return 4

    dataFrame_mail["MailPrüfung"] = dataFrame_mail.apply(mailCheck, axis=1)

    logging.info("Mailprüfung wurde hinzugefügt!")

    dataFrame_mail.to_csv("./export_dateien/mailingliste_converted.csv",
                          index=False, header=True, index_label=False, quoting=csv.QUOTE_NONE, float_format='%.0f')

    logging.info("Export der Mailinglisten erfolgreich abgeschlossen!")

    print("Mailinglisten erfolgreich erstellt!")
