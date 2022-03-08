import argparse
import os
from datetime import datetime


def convert_date(timestamp):
    """Function for converting date and time in user friendly view"""
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime("%d %b %Y %H:%M")
    return formated_date


def my_ls():
    """Function to show directories and files, not including hidden ones"""
    list_file = os.listdir()
    for i in list_file:
        if "." not in i[0]:
            print(i)
    print()


def my_ls_a():
    """Function to show directories and files, including hidden ones"""
    list_file = os.listdir()
    for i in list_file:
        print(i)
    print()


def my_ls_l():
    """Function to show directories and files, including hidden ones with showing
    mode, length, last write time, and name"""
    list_file = os.listdir()
    print(
        "{:10}  ".format("Mode"),
        "{:10}  ".format("Length"),
        "{:18}  ".format("LastWriteTime"),
        "{:10}  ".format("Name"),
    )
    print(
        "{:10}  ".format("--------"),
        "{:10}  ".format("--------"),
        "{:18}  ".format("--------"),
        "{:10}  ".format("--------"),
    )
    for i in list_file:
        file_access_right = ""
        if os.path.isfile(i):
            file_access_right += "-"
            if os.access(i, os.R_OK):
                file_access_right += "r"
            else:
                file_access_right += "-"
            if os.access(i, os.W_OK):
                file_access_right += "w"
            else:
                file_access_right += "-"
            file_access_right += "-r--r--"
        else:
            file_access_right += "d"
            if os.access(i, os.R_OK):
                file_access_right += "r"
            else:
                file_access_right += "-"
            if os.access(i, os.W_OK):
                file_access_right += "w"
            else:
                file_access_right += "-"
            if os.access(i, os.X_OK):
                file_access_right += "xr-xr-x"
            else:
                file_access_right += "-r-xr-x"
        info = os.stat(i)
        print(
            "\033[34m{:10}  ".format(file_access_right),
            "{:10}  ".format(info.st_size),
            "{:10}  ".format(convert_date(info.st_mtime)),
            "{:10}  ".format(i),
        )
    print()


if __name__ == "__main__":
    NAME = "my_ls"
    VERSION = "0.0.1"
    EPILOG = "(c) Anton Babushkin 2022 student at EPAM"
    DESCRIPTION = """This program copy functionality from program LS in Linux.
     For starting program write in terminal "python my_ls.py" and you will see files and directories in current path.
     If you want seeing hidden files and directories add argument "-a", for example "python my_ls.py -a".
     IF you want seeing hidden files and directories with showing mode, length, last write time,
     and name you can add argument "-l", for example "python my_ls.py -l"."""
    p = argparse.ArgumentParser(prog=NAME, description=DESCRIPTION, epilog=EPILOG, add_help=False)
    p.add_argument(
        "--all", "-a", action="store_true", help="Start function to show directories and files, including hidden ones"
    )
    p.add_argument(
        "--long",
        "-l",
        action="store_true",
        help="Function to show directories and files, including hidden ones with showing\
                   mode, length, last write time, and name",
    )
    p.add_argument("--help", "-h", action="help", help="Help message")
    p.add_argument("-v", action="version", help="Version", version="%(prog)s {}".format(VERSION))
    args = p.parse_args()

    if args.all:
        my_ls_a()
    elif args.long:
        my_ls_l()
    else:
        my_ls()
