import codecs
import csv
import gzip
import json
import lzma
import pickle
import platform
import urllib.request
from pathlib import Path
from typing import List, Tuple

if platform.system() == "Windows":
    user = str(Path("~").expanduser()).split("\\")[-1]
else:
    user = str(Path("~").expanduser()).split("/")[-1]

if user == 'jimne' or user == 'rnett':
    data_dir = Path("E:\\508")
elif user == 'JNett':
    data_dir = Path(
        "C:\\Users\\JNett\\Common\\Desktop\\Other "
        "Stuff\\508")
else:
    raise ValueError(f"User {user} not recognized.  Add to the data.py file.")

data_file = data_dir / "review_comments.csv.xz"

prs_file = data_dir / "prs.pickle.gz"
prs_dir = data_dir / "prs"

prs_obj_file = data_dir / "prs_objects.pickle.gz"

# result should be iterable
def load():
    archf = lzma.open(data_file)
    return csv.DictReader(codecs.getreader("utf-8")(archf))


apps = [
    ("f98835efcec776b42a9c", "a73806fc946ced540c208be4320839ecb61c65d5"),
    ("cd2d170e5bdde6a9ec8c", "f10e1d699134140e5735964caf7f915da6ca88ef")
]


def github_api(url):
    text = None
    for app in apps:
        unauth = f"?client_id={app[0]}&client_secret={app[1]}"

        try:
            with urllib.request.urlopen(url + unauth) as api_call:
                text = api_call.read().decode()
                break
        except Exception:
            continue

    if text is None:
        raise ValueError("No apps worked for url: " + url)

    return json.loads(text)


class PR:
    def __init__(self, repo: str, pr_number: int, merged: bool, issue_comments: List[Tuple[str, str]],
                 review_comments: List[Tuple[str, str]]):
        """
        issue_comments and review_comments's first item should be time or order.
        Comments will be sorted by ascending first param.
        """

        self.repo = repo.strip('/')
        self.pr_number = pr_number

        self.merged = merged

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

        dummy = PR(repo, pr_number, True, [], [])

        info = github_api(dummy.api_url)
        merged = info['merged']

        if info['state'] != 'closed':
            raise ValueError("PR is still open")

        issue_comments = github_api(dummy.issue_comments_api_url)
        issue_comments = [(c['created_at'], c['body']) for c in issue_comments]

        review_comments = github_api(dummy.review_comments_api_url)
        review_comments = [(c['created_at'], c['body']) for c in review_comments]

        pr = PR(repo, pr_number, merged, issue_comments, review_comments)
        return pr

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
