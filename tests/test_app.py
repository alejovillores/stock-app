import pytest
from fastapi.testclient import TestClient

from stock_app.main import app
from lib.version import Version

client = TestClient(app)


class TestApp:

    def test_when_request_index_it_should_have_correct_version(self):
        version = Version()
        response = client.get("/")
        data = response.json()
        assert version.correct_version(version=data['version'])
        assert response.status_code == 200
