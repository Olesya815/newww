import requests

def test_create_author():
    request_body = {
        "age": 0,
        "name": "test",
        "genre": "some",
        "dateOfBirth": "string",
        "dateOfDeath": "string",
        "dead": False
    }
    response = requests.post('http://127.0.0.1:8080/api/authors/create', json=request_body)
    deserialized_response = response.json()

    print(response.text)
    assert response.status_code == 200
    assert deserialized_response['id']
    del deserialized_response['id']
    assert deserialized_response == request_body
    # assert deserialized_response['age'] == request_body['age']