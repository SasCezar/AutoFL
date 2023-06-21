import unittest

from fastapi.testclient import TestClient

from api.main import app


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
