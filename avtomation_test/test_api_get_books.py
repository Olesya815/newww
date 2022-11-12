import requests

def test_post_books():
    request_body = {
        "isbn": 3,
        "name": "Воспаление мозгов",
        "authorId": 8,
        "pagesCount": 0,
        "dateOfCreation": "string",
        "hardCovered": False
    }
    response = requests.post('http://127.0.0.1:8080/api/books/create', json=request_body)
    print(response.text)
    return response.json()

def test_get_books():
    books = test_post_books()

    response = requests.get(f'http://127.0.0.1:8080/api/books/{books["id"]}')
    print(response.text)

    assert response.status_code == 200
    assert response == books


