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
    return parsed_response

def test_delete_books():
    delete_books = test_post_books()
    request = requests.delete(f'http://127.0.0.1:8080/api/books/{delete_books["id"]}')
    assert request.status_code == 200

    get_request = requests.get(f'http://127.0.0.1:8080/api/books/{delete_books["id"]}')
    assert get_request.status_code == 500