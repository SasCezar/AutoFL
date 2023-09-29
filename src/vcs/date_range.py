from abc import ABC
from datetime import datetime
from typing import List

from git import Repo

from entity.project import Version


class DateRangeVersionStrategy(ABC):
    """
    Strategy to get the versions of a project from a VCS repository (e.g. git) in a given date range every N days.
    """
    def __init__(self, start_date: str, end_date: str, interval_days: int):
        self.start_date = datetime.strptime(start_date, '%d/%m/%y')
        self.end_date = datetime.strptime(end_date, '%d/%m/%y')
        self.interval_days = interval_days

    def get_versions(self, repository: Repo) -> List[Version]:
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

        commits = [Version(commit_id=commit.hexsha, commit_num=len(commits) - i,
                           commit_date=commit.committed_datetime, files=None) for i, commit in enumerate(commits)]
        return commits
