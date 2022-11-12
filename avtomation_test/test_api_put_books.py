import requests

def test_post_books():
    request_body = {
        "isbn": 4,
        "name": "Анна Каренина",
        "authorId": 4,
        "pagesCount": 0,
        "dateOfCreation": "string",
        "hardCovered": False
    }
    response = requests.post('http://127.0.0.1:8080/api/books/create', json=request_body)
    print(response.text)
    return response.json()


def test_put_books():
    put_books = test_post_books()

    put_request_body = {
        "isbn": 4,
        "name": "Исповедь",
        "authorId": 5,
        "pagesCount": 0,
        "dateOfCreation": "string",
        "hardCovered": False
    }

    response = requests.put(f'http://127.0.0.1:8080/api/books/{put_books["id"]}')


    assert response.status_code == 200

    assert response.json() == put_request_body
