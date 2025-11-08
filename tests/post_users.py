import json
import requests
import time

## changed URL, because reqres.in ended up w/ "error": "Missing API key"
URL = "https://690fa92345e65ab24ac47de7.mockapi.io/users/"

def load_test_data():
    with open("data/users_data.json") as file:
        return json.load(file)

def test_create_user():
    data = load_test_data()

    for user in data:
        start_time = time.time()
        end_time = time.time()
        response = requests.post(f"{URL}/users", json=user)
        elapsed_ms = (end_time - start_time) * 1000

        assert response.status_code == 201

        data_json = response.json()

        assert "id" in data_json
        assert "createdAt" in data_json

        assert isinstance(data_json["id"], str)
        assert isinstance(data_json["createdAt"], int)

        assert elapsed_ms < 100, f"Response took too long: {elapsed_ms} ms"
