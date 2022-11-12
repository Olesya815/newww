import requests
from classs import Stend
from classs import Api


def test_post_books():
    request_body = {
        "isbn": 4,
        "name": "Игрок",
        "authorId": 1,
        "pagesCount": 0,
        "dateOfCreation": "string",
        "hardCovered": False
    }
    a = Stend()
    b = Api()

    response = requests.post(a.get_stend() + b.get_api(), json=request_body)
    assert response.status_code == 200
    assert response.json()['author']['id'] == request_body['authorId']

