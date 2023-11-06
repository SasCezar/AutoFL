import unittest

from pymongo import MongoClient

from entity.project import Project, ProjectRepository


class TestMongoDB(unittest.TestCase):
    def setUp(self) -> None:
        self.client = MongoClient("mongodb://user:password@localhost:27017/default_db?authSource=admin")
        self.db = self.client['development']
        self.project_repository = ProjectRepository(database=self.db)

    def test_write_project(self):
        project = Project(name='test', remote='test', languages=['test'])
        self.project_repository.save(project)
        project: Project = self.project_repository.find_one_by({'name': 'test'})
        print(project)
        self.assertEqual(project.name, 'test')
        self.assertEqual(project.remote, 'test')
        self.assertEqual(project.languages, ['test'])
        self.assertEqual(project.versions, [])
        print(project.model_dump_json(exclude={'id'}))

    def write_many_projects(self):
        projects = [
            Project(name='test1', remote='test1', languages=['test1']),
            Project(name='test2', remote='test2', languages=['test2']),
            Project(name='test3', remote='test3', languages=['test3'])
        ]
        self.project_repository.save_many(projects)

    def test_load_many_projects(self):
        self.db.projects.delete_many({})
        self.write_many_projects()
        projects = list(self.project_repository.find_by({'name': {'$in': ['test1', 'test2', 'test3']}}))
        self.assertEqual(len(projects), 3)
        for i, project in enumerate(projects):
            print(project)
            self.assertEqual(project.name, f'test{i + 1}')
            self.assertEqual(project.remote, f'test{i + 1}')
            self.assertEqual(project.languages, [f'test{i + 1}'])
