from typing import Iterable

from dataloader.dataloader import DataLoaderBase
from entity.project import Project


class MongoDBProjectLoader(DataLoaderBase):
    def load(self) -> Iterable[Project]:
        """Returns a list of cursors to the projects in MongoDB  that allows
        for lazy loading and parallelization
        """
        from pymongo import MongoClient
        client = MongoClient()
        db = client['github']
        collection = db['projects']
        cursor = collection.find().skip(1000).limit(10)
        return cursor