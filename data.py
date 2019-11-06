import codecs
import csv
import lzma
import platform
from pathlib import Path

if platform.system() == "Windows":
    user = str(Path("~").expanduser()).split("\\")[-1]
else:
    pass

if user == 'jimne' or user == 'rnett':
    data_dir = Path("E:\\autociter")
elif user == 'JNett':
    data_dir = Path(
        "C:\\Users\\JNett\\Common\\Desktop\\Other "
        "Stuff\\review_comments.csv.xz")
else:
    # TODO set this for other users
    data_dir = None

# result should be iterable
def load():
    with lzma.open("review_comments.csv.xz") as archf:
        return csv.DictReader(codecs.getreader("utf-8")(archf))
