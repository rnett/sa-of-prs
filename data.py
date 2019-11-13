import codecs
import csv
import gzip
import lzma
import pickle
import platform
from pathlib import Path
from typing import List, Tuple

if platform.system() == "Windows":
    user = str(Path("~").expanduser()).split("\\")[-1]
else:
    pass

if user == 'jimne' or user == 'rnett':
    data_dir = Path("E:\\508")
elif user == 'JNett':
    data_dir = Path(
        "C:\\Users\\JNett\\Common\\Desktop\\Other "
        "Stuff\\review_comments.csv.xz")
else:
    # TODO set this for other users
    data_dir = None

data_file = data_dir / "review_comments.csv.xz"

prs_file = data_dir / "prs.pickle.gz"
prs_dir = data_dir / "prs"


# result should be iterable
def load():
    archf = lzma.open(data_file)
    return csv.DictReader(codecs.getreader("utf-8")(archf))


class PR:
    def __init__(self, repo: str, pr_number: int, issue_comments: List[Tuple[int, str]],
                 review_comments: List[Tuple[int, str]]):
        """
        issue_comments and review_comments's first item should be time or order
        """

        self.repo = repo.strip('/')
        self.pr_number = pr_number

        self.issue_comments = [x[1] for x in issue_comments]
        self.review_comments = [x[1] for x in review_comments]

        self.all_comments = issue_comments + review_comments
        self.all_comments.sort(key=lambda x: x[0])
        self.all_comments = [x[1] for x in self.all_comments]

    @property
    def id(self) -> str:
        return self.repo.replace("/", "-") + f"-{self.pr_number}"

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def load(id: str):
        file = prs_dir / (id + ".pickle.gz")
        return pickle.load(gzip.open(file, 'rb', 9))

    @staticmethod
    def load_all():
        l = []
        for f in prs_dir.iterdir():
            if f.name.endswith(".pickle.gz"):
                l.append(pickle.load(gzip.open(f, 'rb', 9)))

        return l

    @staticmethod
    def repo_and_num_from_api_url(api_url: str) -> Tuple[str, int]:
        p = api_url.split('/')
        return p[4] + '/' + p[5], int(p[7])

    @staticmethod
    def create_from_api(repo: str, pr_number: int):
        # TODO
        raise NotImplementedError

    def save(self, force: bool = False):
        file = prs_dir / (self.id + ".pickle.gz")

        if not force and file.exists():
            raise ValueError(f"File for id {self.id} already exists: {file}")

        pickle.dump(self, gzip.open(file, 'wb+', 9))

    @property
    def api_url(self) -> str:
        return f"https://api.github.com/repos/{self.repo}/pulls/{self.pr_number}"

    @property
    def issue_comments_api_url(self) -> str:
        return self.api_url.replace("pulls", "issues") + "/comments"

    @property
    def review_comments_api_url(self) -> str:
        return self.api_url + "/comments"
