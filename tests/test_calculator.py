import pytest
from calculator import add, substract, app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add():
    assert add(2, 3) == 5
    
def test_substract():
    assert substract(5, 3) == 2

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"result" in response.data or b"Result" in response.data

def test_index_post_add(client):
    response = client.post('/', data={'a': '2', 'b': '3', 'operation': '+'})
    assert response.status_code == 200
    assert b"5" in response.data

def test_index_post_substract(client):
    response = client.post('/', data={'a': '5', 'b': '2', 'operation': '-'})
    assert response.status_code == 200
    assert b"3" in response.data

def test_index_post_invalid_operation(client):
    response = client.post('/', data={'a': '2', 'b': '3', 'operation': '*'})
    assert response.status_code == 200
    assert b"Unknown operation" in response.data

def test_index_post_invalid_input(client):
    response = client.post('/', data={'a': 'foo', 'b': 'bar', 'operation': '+'})
    assert response.status_code == 200
    assert b"Error" in response.data
