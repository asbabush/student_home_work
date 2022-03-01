import requests
from PIL import Image


def compress_file(name: str, url: str, size: str):
    """function for compressing and saving file with right name and right size"""
    size = tuple(int(i) for i in size.split("x"))
    file_image = requests.get(url, stream=True).raw
    image = Image.open(file_image)
    compress_image = image.resize(size)
    compress_image.save(name, "jpeg")
