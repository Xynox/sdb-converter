# todo: this will be a script creating a folder for input/output
# it could also be used as a way to give the user feedback on what files are missing etc.
import os


def createImportFolder():
    parentDir = './'
    dirName = "import_dateien"
    fullPath = os.path.join(parentDir, dirName)

    if os.path.exists(fullPath):
        print("Import-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        print("Kein Import-Verzeichnis erkannt, wird neu erstellt")


def createExportFolder():
    parentDir = './'
    dirName = "export_dateien"
    fullPath = os.path.join(parentDir, dirName)

    if os.path.exists(fullPath):
        print("Export-Verzeichnis existiert bereits, überspringe Erstellung")

    else:
        os.mkdir(fullPath)
        print("Kein Export-Verzeichnis erkannt, wird neu erstellt")
