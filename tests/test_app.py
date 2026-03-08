import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestACEestAPI:

    # ---------- V1 TESTS ----------

    def test_home(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.get_json()
        assert "message" in data
        assert "endpoints" in data


    def test_get_programs(self, client):
        response = client.get("/programs")
        assert response.status_code == 200

        data = response.get_json()
        assert isinstance(data, dict)
        assert "fat_loss" in data


    def test_get_specific_program(self, client):
        response = client.get("/program/fat_loss")
        assert response.status_code == 200

        data = response.get_json()
        assert "workout" in data
        assert "diet" in data


    def test_program_not_found(self, client):
        response = client.get("/program/unknown")
        assert response.status_code == 404


    # ---------- V2 TESTS ----------

    def test_add_client(self, client):
        new_client = {
            "name": "Rahul",
            "age": 25,
            "height": 175,
            "weight": 70
        }

        response = client.post("/add-client", json=new_client)
        assert response.status_code == 200

        data = response.get_json()
        assert "message" in data


    def test_get_clients(self, client):
        response = client.get("/clients")
        assert response.status_code == 200

        data = response.get_json()
        assert isinstance(data, list)


    def test_bmi_calculation(self, client):
        response = client.get("/bmi?height=170&weight=70")
        assert response.status_code == 200

        data = response.get_json()
        assert "BMI" in data