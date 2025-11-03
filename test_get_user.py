import requests
import pytest

headers = {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"
}

# @pytest.mark.parametrize('page', [1, 2, 3])
# def test_users(page):
#     response_get = requests.get(f'https://reqres.in/api/users?page={page}', headers=headers)
def test_users():
    response_get = requests.get('https://reqres.in/api/users?page=2', headers=headers)
    json_response = response_get.json()
    
    assert response_get.status_code == 200
    