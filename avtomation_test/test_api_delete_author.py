import requests

def test_create_author():
    request_body = {
        "age": 15,
        "name": "Egor",
        "genre": "string",
        "dateOfBirth": "string",
        "dateOfDeath": "string",
        "dead": False
    }
    response = requests.post('http://127.0.0.1:8080/api/authors/create', json=request_body)
    print(response.text)
    return response.json()

def test_delete():
    created_author = test_create_author()

    delete_response = requests.delete(f"http://127.0.0.1:8080/api/authors/{created_author['id']}")
    assert delete_response.status_code == 200

    get_author_request = requests.get(f"http://127.0.0.1:8080/api/authors/{created_author['id']}")
    assert get_author_request.status_code == 500