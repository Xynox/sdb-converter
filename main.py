# todo: here will be the main function of the converter

from install import *
from logger import *
from sibank_classlist_converter import *
from webuntis_parent_converter import *
import sys


def askCurrentMode():
    print("Aufgrund der verschiedenen Anwendungsarten muss ein Modus spezifiziert werden. Weitere Informationen befinden sich, wie die Anforderungen der jeweiligen Operationen, in der README.md-Datei.")
    print("Schreiben Sie: \n 1, wenn die Klassenliste aus Sibank in das Iserv-Format konvertiert werden soll, \n 2, wenn die Elternlisten + Mailinglisten für WebUntis erstellt werden sollen oder \n 3, wenn eine WebUntis-Schülerliste erstellt werden soll.")
    ready = False
    global mode

    # the code following feels somewhat not good
    # need to revisit at later point with more knowledge

    while ready == False:

        modeRequest = input("Welcher Modus soll aktiviert werden? ")
        numRequest = int(modeRequest)

        if numRequest == 1:
            mode = 1
            logging.info("Modus 1 erkannt")
            ready = True

        elif numRequest == 2:
            mode = 2
            logging.info("Modus 2 erkannt")
            ready = True

        elif numRequest == 3:
            mode = 3
            logging.info("Modus 3 erkannt")
            ready = True

        else:
            print("Nicht erkennbare Nummer! Bitte Nummer erneut eingeben!")
            logging.error(
                "Falscher Modus erkannt! Modus-Abfrage wird wiederholt!")


def main():
    startLogger()

    # check for the import and export folders and create them when necessary
    createImportFolder()
    createExportFolder()

    askCurrentMode()  # using the function to determine the mode that will be executed

    # check the mode the user has selected, the else function shouldnt be triggered, if, then critical error

    if mode == 1:

        checkMode1Files()
        classlistConverter()

    elif mode == 2:

        checkMode2Files()
        webUntisParentConverter()
        createMailingList()

    elif mode == 3:
        # use here webuntis_parent_converter.py functions, remove the return statement!
        return
    else:
        print("Kein korrekter Modus erkannt. Kritischer Fehler")
        logging.critical(
            "Konnte den Modus nicht erkennen; Verlasse das Programm!")
        input("Programm wird beendet, bitte eine Taste drücken. ")
        sys.exit("Kritischer Fehler, Modus konnte nicht erkannt werden")


main()
