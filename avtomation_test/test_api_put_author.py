import requests

def test_create_author():
    request_body = {
            "age": 13,
            "name": "Anton",
            "genre": "string",
            "dateOfBirth": "string",
            "dateOfDeath": "string",
            "dead": False
        }
    response = requests.post('http://127.0.0.1:8080/api/authors/create', json=request_body)
    return response.json()

def test_put_author():
    created_author = test_create_author()

    update_body = {
        "age": 23,
        "name": "Aleksandr",
        "genre": "string",
        "dateOfBirth": "25.10.2010",
        "dateOfDeath": "string",
        "dead": False
    }
    response = requests.put(f'http://127.0.0.1:8080/api/authors/{created_author["id"]}', json=update_body)
    parsed_response = response.json()

    assert response.status_code == 200
    # assert parsed_response['id']
    # del parsed_response['id']
    assert parsed_response == update_body