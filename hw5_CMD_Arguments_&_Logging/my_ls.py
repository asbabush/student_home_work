import argparse
import os
from datetime import datetime

list_file = os.listdir()


def convert_date(timestamp):
    """Function for converting date and time in user friendly view"""
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime("%d %b %Y %H:%M")
    return formated_date


def my_ls_l(list_for_print):
    """Function to show directories and files, including hidden ones with showing
    mode, length, last write time, and name"""
    max_len_name = 20
    for i in list_file:
        if len(i) > max_len_name:
            max_len_name = len(i)
    print(
        "{:{wight}}".format("Mode", wight=str(max_len_name)),
        "{:{wight}}".format("Length", wight=str(max_len_name)),
        "{:{wight}}".format("LastWriteTime", wight=str(max_len_name)),
        "{:{wight}}".format("Name", wight=str(max_len_name)),
    )
    print(
        "{:{wight}}".format("-" * max_len_name, wight=str(max_len_name)),
        "{:{wight}}".format("-" * max_len_name, wight=str(max_len_name)),
        "{:{wight}}".format("-" * max_len_name, wight=str(max_len_name)),
        "{:{wight}}".format("-" * max_len_name, wight=str(max_len_name)),
    )
    for i in list_for_print:
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
            "{:<{wight}}".format(file_access_right, wight=str(max_len_name)),
            "{:<{wight}}".format(info.st_size, wight=str(max_len_name)),
            "{:<{wight}}".format(convert_date(info.st_mtime), wight=str(max_len_name)),
            "{:<{wight}}".format(i, wight=str(max_len_name)),
        )
    print()


def list_name_for_print(args_all):
    global list_file
    if args_all is False:
        list_file = [i for i in list_file if i[0] != "."]
        return list_file
    else:
        return list_file


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

    if args.long is True:
        my_ls_l(list_name_for_print(args.all))
    else:
        for i in list_name_for_print(args.all):
            print(i)
