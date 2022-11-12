import requests

def test_create_author():
    request_body = {
        "age": 25,
        "name": "Egor",
        "genre": "string",
        "dateOfBirth": "string",
        "dateOfDeath": "string",
        "dead": False
    }
    response = requests.post('http://127.0.0.1:8080/api/authors/create', json=request_body)
    print(response.text)
    return response.json()

def test_get_author():
    created_author = test_create_author()

    response = requests.get(f"http://127.0.0.1:8080/api/authors/{created_author['id']}")
    assert response.status_code == 200
    assert response.json() == created_author