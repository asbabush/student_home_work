import argparse
import os
import threading

from compress_file import compress_file
from files_naming import file_naming

parser = argparse.ArgumentParser(description="Download images and change size")
parser.add_argument("url_list", type=str, help="Url list for download images")
parser.add_argument("--dir", type=str, default="New folder/", help="Output dir for images (default: New folder/)")
parser.add_argument("--threads", type=int, default=1, help="Number of threads (default: 1)")
parser.add_argument("--size", type=str, default="100x100", help="Size images (default: 100x100)")
args = parser.parse_args()


with open(args.url_list, "r") as url_list:
    url_list = list(map(lambda s: s.rstrip("\n"), url_list))

start_dir = os.getcwd()  # save start directory
if os.path.isdir(args.dir):  # check existence directory
    os.chdir(args.dir)
else:
    os.mkdir(args.dir)
    os.chdir(args.dir)

count_error = 0
count_complete = 0
download_bite = 0
print("download and compress started")
print()


for index, line in enumerate(url_list):
    try:
        threading.Thread(target=compress_file, args=(file_naming(index), line, args.size)).run()
        print("saving image from", line, "completed")
        count_complete += 1
    except Exception:
        print("saving image from", line, "failed")
        count_error += 1
print()
print("Count complete:", count_complete)
print("Count error:", count_error)
print("Download bite:", download_bite)
os.chdir(start_dir)  # go to start directory
