from abc import ABC
from datetime import datetime
from typing import List

from git import Repo


class DateRangeVersionStrategy(ABC):
    def __init__(self, start_date: str, end_date: str, interval_days: int):
        self.start_date = datetime.strptime(start_date, '%d/%m/%y')
        self.end_date = datetime.strptime(end_date, '%d/%m/%y')
        self.interval_days = interval_days

    def get_versions(self, repository: Repo) -> List[str]:
        # start = int(datetime.strptime('01/01/2018', '%d/%m/%Y').timestamp())
        # print(start)
        # end = int(datetime.strptime('01/01/2019', '%d/%m/%Y').timestamp())
        # range_comm = list(repository.iter_commits(f"--min-age={start} --max-age={end}"))
        # print(len(range_comm))
        # raise
        commits = []
        for commit in repository.iter_commits('--all'):
            version_date = datetime.fromtimestamp(commit.authored_date)
            if self.start_date < version_date < self.end_date:
                if not commits or not self.interval_days:
                    commits.append(commit)
                    continue

                delta = datetime.fromtimestamp(commits[-1].authored_date) - version_date
                if delta.days >= self.interval_days:
                    commits.append(commit)

        commits = [commit.hexsha for commit in commits]
        return commits
