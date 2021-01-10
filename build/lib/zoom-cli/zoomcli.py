from configparser import ConfigParser
from os import name, system, path as pth
from sys import argv
import os

class ZoomCLI():
    def __init__(self):
        self.zm = ConfigParser()
        self.p = pth.join(pth.dirname(__file__), 'config.zcli')
        if not pth.isfile(self.p):
            with open(self.p, 'w') as x:
                x.write('[Meetings]')
        self.zm.read(self.p)
        self.meetings = dict(self.zm._sections["Meetings"])

    def runner(self):
        if len(argv) == 1:
            self.help()
            return
        if argv[1] in ('add'):
            self.add()
        elif argv[1] in ('delete'):
            self.delete()
        elif argv[1] in ('list'):
            self.list_all()
        elif argv[1] in ('path'):
            self.path()
        elif argv[1] in ('--help'):
            self.help()
        elif argv[1]:
            self.open()

    def help(self):
        os.system("figlet Zoom - CLI | lolcat")
        print("############################################################")
        print("# Commands:                                                #")
        print("# zcli [add/delete] [name] [code] [password]               #")
        print("# zcli delete [name]                                       #")
        print("# zcli list                                                #")
        print("# zcli path                                                #")
        print("# zcli --help                                              #")
        print("#----------------------------------------------------------#")
        print("# Created by JK3171                                        #")
        print("# https://github.com/jk3171/Zoom-CLI                       #")
        print("############################################################")

    def add(self):
        if len(argv) < 4:
            print(
                "ZCLI - Error: Please Check Your Input.\n"
                + "Usage: zcli [add/delete] [name] [code] [password]")
            return
        if argv[2] in ['add', 'delete', 'list', 'path',
                       '--help',]:
            print("ZCLI - Error: Invalid Name!")
            return
        try:
            formatted_meet = f"{argv[3]},{argv[4]}"
        except IndexError:
            formatted_meet = f"{argv[3]}"
        self.zm.set('Meetings', argv[2], formatted_meet)
        try:
            with open(self.p, 'w') as x:
                self.zm.write(x)
            print(f"ZCLI - Success: Meeting {argv[2]} added.")
        except PermissionError:
            print("ZCLI - Error: Couldn't write to file.")

    def delete(self):
        if len(argv) < 3:
            print(
                "ZCLI - Error: Please enter the correct amount of arguments.\n"
                + "Usage: zcli [delete/d] [name]")
            return
        if self.zm.has_option("Meetings", argv[2]):
            try:
                self.zm.remove_option("Meetings", argv[2])
                with open(self.p, 'w') as x:
                    self.zm.write(x)
                print(f"ZCLI - Success: Meeting {argv[2]} deleted.")
            except PermissionError:
                print("ZCLI - Error: Insufficent Permissions.")
        else:
            print("ZCLI - Error: Invalid Meeting.\nRun zcli add [name] "
                  "[code] [password] first, then `zcli [name]`")

    def open(self):
        joiner = '^' if name == "nt" else '\\'
        opener = 'start' if name == "nt" else 'open'
        if self.zm.has_option("Meetings", argv[1]):
            conf = self.meetings.get(argv[1])
            t = True
            if ',' in conf:
                conf = conf.split(",", 1)
                t = False
            system(f"{opener} zoommtg://zoom.us/join?confno={conf}" if t
                   else f"{opener} zoommtg://zoom.us/join?confno={conf[0]}"
                   f"{joiner}&pwd={conf[1]}")
            print(f"ZCLI - Success: Meeting {argv[1]} opened.")
        else:
            print("ZCLI - Error: Invalid Meeting.\nRun zcli add [name] "
                  "[code] [password] first, then `zcli [name]`")

    def list_all(self):
        print("Your Zoom Meetings:")
        for x in self.meetings:
            conf = self.meetings.get(x).split(",", 1)
            s = f"{x}: \nConference number: {conf[0]}"
            if len(conf) > 1:
                s += f", \nPassword: {conf[1]}"
            print(s)

    def path(self):
        print(f"Your .zcli File is Located at...\n {self.p}.")


def zoomcli():
    z = ZoomCLI()
    z.runner()


if __name__ == "__main__":
    zoomcli()
