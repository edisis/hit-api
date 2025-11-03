import requests
import pytest

headers = {
    "Content-Type": "application/json"
    # Hapus x-api-key karena reqres.in tidak butuh API key
}

@pytest.mark.parametrize('page', [1, 2, 3])
def test_users(page):
    response_get = requests.get(f'https://reqres.in/api/users?page={page}', headers=headers)
    json_response = response_get.json()
    
    assert response_get.status_code == 200, f'Request failed on page {page}'
    assert json_response.get('page') == page, f'Wrong page {page}'