import argparse
import concurrent.futures
import os
import threading

import requests
from PIL import Image

parser = argparse.ArgumentParser(description="Download images and change size")
parser.add_argument("url_list", type=str, help="Url list for download images")
parser.add_argument("--dir", type=str, default="New folder/", help="Output dir for images (default: New folder/)")
parser.add_argument("--threads", type=int, default=1, help="Number of threads (default: 1)")
parser.add_argument("--size", type=str, default="100x100", help="Size images (default: 100x100)")
args = parser.parse_args()

thread_local = threading.local()


def file_naming(index):
    index = str(index)
    file_name_0 = "00000"
    file_name_out = file_name_0[: -(len(index))] + index + ".jpg"
    return file_name_out


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_image(url: str, name: str, size_jpg: str):
    session = get_session()
    size_jpg = tuple(int(i) for i in size_jpg.split("x"))
    global cont_error, cont_complete, count_size
    with session.get(url, stream=True).raw as response:
        try:
            image = Image.open(response)
            compress_image = image.resize(size_jpg)
            compress_image.save(name, "jpeg")
            print(f"saving image {os.path.getsize(name)} bait from {url} completed")
            cont_complete += 1
            count_size += os.path.getsize(name)
        except Exception as e:
            print(f"saving image from {url} failed. Because: ", e)
            cont_error += 1


def download_all_image(sites: list, name: list, size_image: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(download_image, sites, name, size_image)


if __name__ == "__main__":
    with open(args.url_list, "r") as url_list:
        url_list = list(map(lambda s: s.rstrip("\n"), url_list))

    naming_jpg = list(map(file_naming, [i for i in range(0, len(url_list))]))
    size = [args.size for i in range(0, len(url_list))]

    cont_error = 0
    cont_complete = 0
    count_size = 0

    start_dir = os.getcwd()  # save start directory
    if os.path.isdir(args.dir):  # check existence directory
        os.chdir(args.dir)
    else:
        os.mkdir(args.dir)
        os.chdir(args.dir)

    print("\ndownload and compress started\n")

    download_all_image(url_list, naming_jpg, size)

    print("\nCount complete:", cont_complete)
    print("Count error:", cont_error)
    print("total downloads:", count_size, "bytes\n")
    os.chdir(start_dir)  # go to start directory
