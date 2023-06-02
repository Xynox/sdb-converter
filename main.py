# Import aller benötigten Module

import sys

from logger import *

from install import *
from sibank_classlist_converter import *
from webuntis_parent_converter import *
from webuntis_student_converter import *


def askCurrentMode():
    """ In dieser Funktion werden die Modi abgefragt, in welchen das Programm laufen soll. 
     modeRequest fragt den Nutzer zunächst nach dem Modus und speichert diesen als Integer in numRequest ab.
      Wenn es keine Nummer ist, wird der Input wiederholt, sonst erfolgt eine Abfrage, welcher Modus gewählt wird
       Diese Abfrage setzt dann die globale Variable mode auf den jeweiligen Modus. """

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
    """ Hier ist die main()-Funktion des Skripts.
     Zunächst werden die Standardprozedere ausgeführt, bis der Modus anhand der globalen Variable mode gecheckt wird
      Daraufhin wird der Code in die jeweiligen anderen .py-Dateien verlagert.
       Falls zu diesem Zeitpunkt etwas schiefgeht, wird das Programm gezwungen, sich zu beenden. """

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
        iservParentAccountConverter()

    elif mode == 3:

        checkMode3Files()
        webUntisStudentConverter()

    else:
        print("Kein korrekter Modus erkannt. Kritischer Fehler")
        logging.critical(
            "Konnte den Modus nicht erkennen; Verlasse das Programm!")
        input("Programm wird beendet, bitte eine Taste drücken. ")
        sys.exit("Kritischer Fehler, Modus konnte nicht erkannt werden")

    input("Programm hat Modus ausgeführt und wird beendet, bitte beliebige Taste drücken: ")


# Ausführung der main()-Funktion
main()
