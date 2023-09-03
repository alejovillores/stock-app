import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from stock_app.main import app, get_db
from lib.version import Version
from stock_app.models.user import User
from config.constants import TEST_BD_URL

engine = create_engine(
    TEST_BD_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


User.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestApp:

    def test_when_request_index_it_should_have_correct_version(self):
        version = Version()
        response = client.get("/")
        data = response.json()
        assert version.correct_version(version=data['version'])
        assert response.status_code == 200

    def test_when_post_new_user_it_should_return_saved_user_with_id_1(self):
        response = client.post(
            "/users",
            json={
                "name": "name",
                "last_name": "last_name",
                "email": "deadpool@example.com",
                "password": "chimichangas4life"},
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "name"
        assert data["last_name"] == "last_name"
        assert data["email"] == "deadpool@example.com"
        assert data["id"] == 1

    def test_when_post_new_user_it_should_return_saved_user_with_id_2(self):
        response = client.post(
            "/users",
            json={
                "name": "name2",
                "last_name": "last_name2",
                "email": "deadpool2@example.com",
                "password": "chimichangas4life"},
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "name2"
        assert data["last_name"] == "last_name2"
        assert data["email"] == "deadpool2@example.com"
        assert data["id"] == 2
