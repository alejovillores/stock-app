from fastapi.testclient import TestClient
import pytest

from stock_app.main import app


client = TestClient(app)


class TestApp:

    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
