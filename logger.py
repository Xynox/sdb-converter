# todo this will be a logger of all steps (mainly for debugging, can be kept as verification for the program working)
# may get deprecated

import logging


def startLogger():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        level=logging.DEBUG, filename='sdb-log.txt', datefmt="%H:%M:%S")
    print("Logger gestartet! Damit die Konsole nicht zu voll wird, werden Aktionen in sdb-log.txt geloggt! Wichtige Ereignisse werden weiterhin hier angezeigt.")
    logging.info("Logger gestartet!")
