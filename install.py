import os
import logging


""" Beide folgenden Funktionen checken zunächst durch Konstanten, die verbunden werden, ob das jeweilige Verzeichnis existiert.

Wenn ja: Überspringen der Erstellung der Ordner
Wenn nein: Mithilfe der os-Funktion wird ein Verzeichnis erstellt, das je nach Funktion "export_dateien" oder "input_dateien" heißt. """


def createImportFolder():
    PARENT_DIR = './'
    DIR_NAME = "import_dateien"
    fullPath = os.path.join(PARENT_DIR, DIR_NAME)

    if os.path.exists(fullPath):
        logging.info(
            "Import-Verzeichnis existiert bereits, überspringe Erstellung")
        print("Import-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        logging.info("Kein Import-Verzeichnis erkannt, wird neu erstellt")
        print("Kein Import-Verzeichnis erkannt, wird neu erstellt")


def createExportFolder():
    PARENT_DIR = './'
    DIR_NAME = "export_dateien"
    fullPath = os.path.join(PARENT_DIR, DIR_NAME)

    if os.path.exists(fullPath):
        logging.info(
            "Export-Verzeichnis existiert bereits, überspringe Erstellung")
        print("Export-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        logging.info("Kein Export-Verzeichnis erkannt, wird neu erstellt")
        print("Kein Export-Verzeichnis erkannt, wird neu erstellt")


""" Alle folgenden Funktionen sind gleich aufgebaut und funktionieren praktisch gleich:
Zunächst wird dem Nutzer Zeit eingeräumt, die erforderlichen Dateien in dem Import-Ordner abzulegen und wartet auf seinen Input
Danach wird überprüft, ob die Datei gefunden wurde

Wenn ja, dann wird der while-Loop unterbrochen
Wenn nein, dann wird der while-Loop wiederholt und der Nutzer wiederum um Input gefragt (siehe oben) """


def checkMode1Files():

    while True:

        print(" ")
        input(
            "Bitte 'sibank_classes.csv'-Datei in den 'import_dateien'-Ordner platzieren! Danach Taste drücken, um fortzufahren... ")

        classlist_check = os.path.exists('./import_dateien/sibank_classes.csv')

        if classlist_check == True:
            logging.info("Sibank Klassenliste wurde erfolgreich gefunden!")
            print("Klassenliste aus Sibank erfolgreich gefunden!")
            break

        else:
            logging.warning("Konnte die Sibank Klassenliste nicht finden!")
            print("Klassenliste konnte nicht gefunden werden! Bitte erneut versuchen.")


def checkMode2Files():

    while True:

        print(" ")
        input(
            "Bitte die Dateien 'sibank_ez1.csv', 'sibank_ez2.csv' und 'iserv_account_data.csv' in den 'import_dateien'-Ordner platzieren! Danach Taste drücken, um fortzufahren... ")

        classlist_check = os.path.exists(
            './import_dateien/sibank_ez1.csv') & os.path.exists('./import_dateien/sibank_ez2.csv') & os.path.exists("./import_dateien/iserv_account_data.csv")

        if classlist_check == True:
            logging.info(
                "Sibank Erziehungsberechtigtenlisten und Iserv Nutzerdatenbank wurden erfolgreich gefunden!")
            print(
                "Erziehungsberechtigtenlisten aus Sibank und Nutzerdatenbank aus Iserv erfolgreich gefunden!")
            break

        else:
            logging.warning(
                "Konnte die Sibank Erziehungsberechtigtenlisten und Nutzerdatenbank (Iserv) nicht finden!")
            print(
                "Erziehungsberechtigtenlisten und Nutzerdatenbank (Iserv) konnten nicht gefunden werden! Bitte erneut versuchen.")


def checkMode3Files():

    while True:

        print(" ")
        input(
            "Bitte vergewissern, dass die Datei 'iserv_account_data.csv' in dem 'import_dateien'-Ordner ist und 'iserv_nutzer_converted.csv' im 'export_dateien'-Ordner sich befindet! Danach Taste drücken, um fortzufahren... ")

        classlist_check = os.path.exists(
            './export_dateien/iserv_nutzer_converted.csv') & os.path.exists('./import_dateien/iserv_account_data.csv')

        if classlist_check == True:
            logging.info(
                "Konvertierte Klassenliste und Iserv Nutzerdatenbank wurden erfolgreich gefunden!")
            print(
                "Konvertierte Klassenliste und Nutzerdatenbank aus Iserv erfolgreich gefunden!")
            break

        else:
            logging.warning(
                "Konnte die Sibank Erziehungsberechtigtenlisten und Nutzerdatenbank (Iserv) nicht finden!")
            print(
                "Erziehungsberechtigtenlisten und Nutzerdatenbank (Iserv) konnten nicht gefunden werden! Bitte erneut versuchen.")
