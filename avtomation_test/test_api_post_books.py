import requests

def test_post_books():
    request_body = {
        "isbn": 1,
        "name": "Мастер и Маргарита",
        "authorId": 4,
        "pagesCount": 0,
        "dateOfCreation": "string",
        "hardCovered": False
    }
    response = requests.post('http://127.0.0.1:8080/api/books/create', json=request_body)
    parsed_response = response.json()
    print(response.text)

    assert response.status_code == 200

    assert parsed_response['author']['id'] == request_body['authorId']


