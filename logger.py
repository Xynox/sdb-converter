import logging

""" Folgende Funktion initialisiert den Logger.
Der Logger beginnt ab dem Level "DEBUG" und speichert den Log als "sdb-log.txt" im Directory der main-Datei.
Format ist folgendes: "STUNDE:MINUTE:SEKUNDE LEVEL NACHRICHT" """


def startLogger():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        level=logging.DEBUG, filename='sdb-log.txt', datefmt="%H:%M:%S")
    print("Logger gestartet! Damit die Konsole nicht zu voll wird, werden Aktionen in sdb-log.txt geloggt! Wichtige Ereignisse werden weiterhin hier angezeigt.")
    logging.info("Logger gestartet!")
