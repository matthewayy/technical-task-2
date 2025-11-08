import requests


URL = "https://reqres.in/api"

def test_get_users():
    response = requests.get(f"{URL}/users?page=2")

    assert response.status_code == 200
    data_json = response.json()

    assert isinstance(data_json["page"], int)
    assert isinstance(data_json["per_page"], int)
    assert isinstance(data_json["total"], int)
    assert isinstance(data_json["total_pages"], int)
    assert isinstance(data_json["data"], list)

    assert data_json["data"][0]["last_name"] is not None
    assert data_json["data"][1]["last_name"] is not None

    assert data_json["total"] == data_json["per_page"] * data_json["total_pages"]

    for user in data_json["data"]:
        assert isinstance(user["id"], int)
        assert isinstance(user['email'], str)
        assert isinstance(user['first_name'], str)
        assert isinstance(user['last_name'], str)
        assert isinstance(user['avatar'], str)
        assert "@" in user['email']
   