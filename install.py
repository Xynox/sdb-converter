# todo: this will be a script creating a folder for input/output
# it could also be used as a way to give the user feedback on what files are missing etc.
import os
import logging


def createImportFolder():
    parentDir = './'
    dirName = "import_dateien"
    fullPath = os.path.join(parentDir, dirName)

    if os.path.exists(fullPath):
        logging.info(
            "Import-Verzeichnis existiert bereits, überspringe Erstellung")
        print("Import-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        logging.info("Kein Import-Verzeichnis erkannt, wird neu erstellt")
        print("Kein Import-Verzeichnis erkannt, wird neu erstellt")


def createExportFolder():
    parentDir = './'
    dirName = "export_dateien"
    fullPath = os.path.join(parentDir, dirName)

    if os.path.exists(fullPath):
        logging.info(
            "Export-Verzeichnis existiert bereits, überspringe Erstellung")
        print("Export-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        logging.info("Kein Export-Verzeichnis erkannt, wird neu erstellt")
        print("Kein Export-Verzeichnis erkannt, wird neu erstellt")


def checkMode1Files():

    while True:

        input(
            "Bitte die Dateien in den 'import_dateien'-Ordner platzieren! Danach Taste drücken, um fortzufahren... ")

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

        input(
            "Bitte die Dateien in den 'import_dateien'-Ordner platzieren! Danach Taste drücken, um fortzufahren... ")

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

        input(
            "Bitte die Dateien in den 'import_dateien'-Ordner platzieren! Danach Taste drücken, um fortzufahren... ")

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
