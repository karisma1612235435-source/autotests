import json

import pytest
import requests


@pytest.fixture
def base_url():
    return "https://automationexercise.com"

def test_get_products_list(base_url):
    response = requests.get(f"{base_url}/api/productsList")
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=2))
    assert type(data) == dict
    assert "products" in data
    assert len(data["products"]) > 0
    first=data["products"][0]
    assert "name" in first
    assert "price" in first


def test_verify_login(base_url):
    response = requests.post(
        f"{base_url}/api/verifyLogin",
        data={"email": "derbmo@gmail.com", "password": "wrong"},
    )
    body = response.json()
    assert body["responseCode"] == 404
    assert "User" in body["message"]

    


