import sys
import os
import time
import inspect
import os


class Logger:

    def __init__(self):
        self.os = os
        self.inspect = inspect
        self.time = time.ctime

        # print(str(" line nr " + str(self.inspect.currentframe().f_back.f_lineno)))

    def lineno(self):
        # Returns the current line number and script name in our program
        return str(" line nr " + str(self.inspect.currentframe().f_back.f_lineno))

    def all_log(self, logtext):
        os = self.os
        with open(os.path.join(os.getcwd(), "Logs\\full_log.txt"), "a") as logfile:
            logfile.seek(0, 0)
            logfile.write(self.time() + " " + logtext + "\n")

    def eingabe_log(self, logtext, char_name):
        os = self.os
        log_file_location = os.path.join(os.getcwd(), "Logs", "eingabe_log", char_name)
        file_loc = os.path.join(log_file_location, "eingabe_log.txt")

        if os.path.isdir(log_file_location):
            pass
        else:
            os.makedirs(log_file_location)
            ersteller = open(file_loc, "w+")
            ersteller.close()

        with open(file_loc, "a") as logfile:
            logfile.write(self.time() + " " + logtext + "\n")

class Backup:

    def __init__(self, originalfile):
        
        self.sys = sys
        self.os = os
        self.time = time
        self.logger = Logger()
        self.originalfile = originalfile
        self.pfad_dir_backup = ""
        self.backuploc = os.path.join(os.getcwd(), "Saved_Games", "Backups", originalfile)

        # Schritte für das Backup
        self.checkdir()
        self.checkfil()

    def checkdir(self):
        os = self.os

        # Momentaner Monat und Jahr
        pfad_dir_backup = os.path.join(self.backuploc, str(self.date_getter()))
        self.pfad_dir_backup = pfad_dir_backup

        # Boolean ob der Ordner Existiert
        check = os.path.isdir(pfad_dir_backup)

        # Wenn er exsistiert dann pass wenn nicht wird erstellt und nochmal getestet
        if check:
            self.logger.all_log("dir for backup found")
        elif not check:
            self.logger.all_log("dir not found in " + pfad_dir_backup)
            os.makedirs(pfad_dir_backup)
            self.logger.all_log("dir made")
            self.checkdir()
        else:
            self.logger.all_log("Unexpected Error " + self.logger.lineno())
            self.sys.exit("Fehler in checkdir")

    def checkfil(self):
        os = self.os

        # Überprüfung ob es die datei zum backup überhaupt gibt
        check = os.path.isfile(self.originalfile)
        if check:
            self.logger.all_log("Data found at " + self.originalfile)
        elif not check:
            self.logger.all_log("Data not found at " + self.originalfile)
        else:
            self.logger.all_log("Unexpected Error in " + self.logger.lineno())
            self.sys.exit("Kritischer Fehler beim Backup")

        # Filename ersteller
        time = str(self.time_getter())
        pfadfil = os.path.join(self.pfad_dir_backup, time + ".txt")

        # Backup Ersteller
        with open(pfadfil, "x") as backupfile:
            with open(self.originalfile) as originfile:
                for i in originfile:
                    backupfile.write(i)

        self.logger.all_log("Backup erstellt")

    def date_getter(self):
        time = self.time
        return str(time.localtime().tm_year) + "-" + str(time.localtime().tm_mon)

    def time_getter(self):
        time = self.time
        return (str(time.localtime().tm_mday) + "_" + str(time.localtime().tm_hour) + "-" +
                str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))
